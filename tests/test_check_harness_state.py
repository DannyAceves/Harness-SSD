import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from check_harness_state import audit_repository, canonical_bytes, projected_state


class HarnessStateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.feature = self.root / "specs" / "008-example"
        self.feature.mkdir(parents=True)
        self.spec = self.feature / "spec.md"
        self.spec.write_text(
            "# Feature\n**Estado:** APPROVED  \n## FR-001\nRequired behavior.\n",
            encoding="utf-8",
        )
        self._write_events([self._approval()])
        (self.root / "handoff.md").write_text(
            '# Live\n```json harness-state\n'
            '{"schema_version": 1, "active": [{"id": "SPEC-008", '
            '"phase": "PLAN", "next": "/plan"}], "validated": []}\n'
            '```\n', encoding="utf-8",
        )
        docs = self.root / "docs"
        docs.mkdir()
        (docs / "index.md").write_text(
            '- `specs/008-example/spec.md`\n', encoding="utf-8"
        )

    def _approval(self, artifact=None, **changes):
        artifact = artifact or self.spec
        event = {
            "id": "DECISION-001",
            "kind": "APPROVAL",
            "actor": "Project owner",
            "date": "2026-09-30",
            "decision": "Approved SPEC-008",
            "scope": "SPEC-008 v0.1",
            "artifact": (
                artifact.relative_to(self.root).as_posix()
                if isinstance(artifact, Path) else artifact
            ),
            "artifact_sha256": hashlib.sha256(canonical_bytes(self.spec)).hexdigest(),
            "source": "Explicit human decision recorded in this file",
        }
        event.update(changes)
        return event

    def _write_events(self, events):
        (self.feature / "decisions.json").write_text(
            json.dumps({"schema_version": 1, "events": events}), encoding="utf-8"
        )

    def _codes(self):
        return {issue.code for issue in audit_repository(self.root)}

    def _closed_feature(self, report=None):
        self.spec.write_text(
            "# Feature\n**Estado:** APPROVED\n## AC-001 — Check\nExpected.\n",
            encoding="utf-8",
        )
        (self.feature / "plan.md").write_text(
            "# Plan\n**Estado:** APPROVED\n", encoding="utf-8"
        )
        (self.feature / "tasks.md").write_text(
            "# Tasks\n**Estado:** COMPLETED\n"
            "## TASK-001 — Work\n**Estado:** DONE\n"
            "**TEST-001:** Verify AC-001.\n"
            "| Orden | Tarea | Estado |\n| 1 | TASK-001 | DONE |\n",
            encoding="utf-8",
        )
        evidence = self.feature / "evidence"
        evidence.mkdir()
        (evidence / "result.md").write_text("Synthetic evidence\n", encoding="utf-8")
        (self.feature / "validation.md").write_text(
            report or (
                "**Result:** PASS\n"
                "| AC | Verification | Result |\n"
                "| AC-001 | TEST-001; `evidence/result.md` | PASS |\n"
                "| TASK | Evidence | Result |\n"
                "| TASK-001 | `evidence/result.md` | PASS |\n"
                "| TEST | Evidence | Result |\n"
                "| TEST-001 | `evidence/result.md` | PASS |\n"
                "**SPEC Compliance:** PASS\n**Feature Status:** VALIDATED\n"
            ), encoding="utf-8",
        )

    def test_valid_approval_is_self_contained(self):
        self.assertEqual(self._codes(), set())

    def test_missing_or_stale_handoff_fails(self):
        handoff = self.root / "handoff.md"
        handoff.write_text("# Live\n", encoding="utf-8")
        self.assertIn("INVALID_HANDOFF", self._codes())
        handoff.write_text(
            '```json harness-state\n'
            '{"schema_version": 1, "active": [], "validated": []}\n'
            '```\n', encoding="utf-8",
        )
        self.assertIn("STALE_HANDOFF", self._codes())

    def test_missing_index_link_fails(self):
        (self.root / "docs/index.md").write_text("# Empty\n", encoding="utf-8")
        self.assertIn("STALE_INDEX", self._codes())

    def test_extra_index_link_and_duplicate_handoff_block_fail(self):
        index = self.root / "docs/index.md"
        index.write_text(
            index.read_text(encoding="utf-8") + "- `specs/999-gone/spec.md`\n",
            encoding="utf-8",
        )
        self.assertIn("STALE_INDEX", self._codes())
        handoff = self.root / "handoff.md"
        handoff.write_text(
            handoff.read_text(encoding="utf-8") * 2, encoding="utf-8"
        )
        self.assertIn("INVALID_HANDOFF", self._codes())

    def test_operational_state_and_checkmarks_do_not_change_digest(self):
        tasks = self.feature / "tasks.md"
        tasks.write_text(
            "# Tasks\n**Estado:** APPROVED  \n- [ ] Gate ready\n"
            "## TASK-001\n**Estado:** TODO  \nDepends on: None\n"
            "| 1 | TASK-001 | TODO |\n",
            encoding="utf-8",
        )
        expected = hashlib.sha256(canonical_bytes(tasks)).hexdigest()
        tasks.write_text(
            "# Tasks\n**Estado:** IN_PROGRESS  \n- [x] Gate ready\n"
            "## TASK-001\n**Estado:** DONE  \nDepends on: None\n"
            "| 1 | TASK-001 | DONE |\n",
            encoding="utf-8",
        )
        self.assertEqual(hashlib.sha256(canonical_bytes(tasks)).hexdigest(), expected)
        tasks.write_text(tasks.read_text(encoding="utf-8").replace("None", "TASK-002"))
        self.assertNotEqual(hashlib.sha256(canonical_bytes(tasks)).hexdigest(), expected)

    def test_four_column_task_order_status_is_operational(self):
        tasks = self.feature / "tasks.md"
        tasks.write_text(
            "# Tasks\n**Estado:** APPROVED\n"
            "| Orden | Tarea | Depende de | Estado |\n"
            "| 1 | TASK-001 | ninguna | TODO |\n",
            encoding="utf-8",
        )
        before = hashlib.sha256(canonical_bytes(tasks)).hexdigest()
        tasks.write_text(
            tasks.read_text(encoding="utf-8").replace("| TODO |", "| IN_PROGRESS |"),
            encoding="utf-8",
        )
        self.assertEqual(hashlib.sha256(canonical_bytes(tasks)).hexdigest(), before)
        tasks.write_text(
            tasks.read_text(encoding="utf-8").replace("ninguna", "TASK-002"),
            encoding="utf-8",
        )
        self.assertNotEqual(hashlib.sha256(canonical_bytes(tasks)).hexdigest(), before)

    def test_requirement_state_is_not_operational_metadata(self):
        self.spec.write_text(
            "# Feature\n**Estado:** APPROVED\n## FR-001\n"
            "**Estado:** TODO\nRequired behavior.\n", encoding="utf-8"
        )
        before = hashlib.sha256(canonical_bytes(self.spec)).hexdigest()
        self.spec.write_text(
            self.spec.read_text(encoding="utf-8").replace(
                "## FR-001\n**Estado:** TODO", "## FR-001\n**Estado:** DONE"
            ), encoding="utf-8"
        )
        self.assertNotEqual(hashlib.sha256(canonical_bytes(self.spec)).hexdigest(), before)

    def test_changed_requirement_invalidates_approval(self):
        self.spec.write_text(
            self.spec.read_text(encoding="utf-8").replace("Required", "Different"),
            encoding="utf-8",
        )
        self.assertIn("HASH_MISMATCH", self._codes())

    def test_missing_record_is_not_approval(self):
        (self.feature / "decisions.json").unlink()
        self.assertIn("MISSING_LEDGER", self._codes())

    def test_invalid_ledger_and_duplicate_id_fail(self):
        self._write_events([self._approval(), self._approval()])
        self.assertIn("DUPLICATE_ID", self._codes())
        (self.feature / "decisions.json").write_text("{bad", encoding="utf-8")
        self.assertIn("INVALID_JSON", self._codes())

    def test_invalid_path_or_conflicting_approval_fails(self):
        self._write_events([self._approval(artifact="../secret")])
        self.assertIn("INVALID_ARTIFACT", self._codes())
        self._write_events([
            self._approval(),
            self._approval(id="DECISION-002", decision="Rejected SPEC-008"),
        ])
        self.assertIn("CONFLICTING_APPROVAL", self._codes())

    def test_symlinked_feature_outside_repository_is_rejected(self):
        with tempfile.TemporaryDirectory() as outside:
            external = Path(outside) / "008-external"
            external.mkdir()
            (self.root / "specs" / "009-external").symlink_to(external, target_is_directory=True)
            self.assertIn("INVALID_FEATURE", self._codes())

    def test_unknown_operational_state_fails_closed(self):
        self.spec.write_text(
            self.spec.read_text(encoding="utf-8").replace("APPROVED", "MAYBE"),
            encoding="utf-8",
        )
        self.assertIn("INVALID_STATE", self._codes())

    def test_task_card_and_order_row_must_agree(self):
        tasks = self.feature / "tasks.md"
        tasks.write_text(
            "# Tasks\n**Estado:** DRAFT\n"
            "## TASK-001 — Work\n**Estado:** TODO\n"
            "| Orden | Tarea | Estado |\n| 1 | TASK-001 | DONE |\n",
            encoding="utf-8",
        )
        issues = audit_repository(self.root)
        self.assertIn("TASK_STATE_MISMATCH", {issue.code for issue in issues})
        self.assertTrue(any("TASK-001" in issue.detail for issue in issues))

    def test_duplicate_or_missing_task_order_row_fails(self):
        tasks = self.feature / "tasks.md"
        tasks.write_text(
            "# Tasks\n**Estado:** DRAFT\n"
            "## TASK-001 — Work\n**Estado:** TODO\n"
            "| Orden | Tarea | Estado |\n| 1 | TASK-001 | TODO |\n"
            "| 2 | TASK-001 | TODO |\n",
            encoding="utf-8",
        )
        self.assertIn("DUPLICATE_TASK_ROW", self._codes())
        tasks.write_text(
            tasks.read_text(encoding="utf-8").replace(
                "| 1 | TASK-001 | TODO |\n| 2 | TASK-001 | TODO |\n", ""
            ), encoding="utf-8",
        )
        self.assertIn("MISSING_TASK_ROW", self._codes())

    def test_completed_tasks_document_rejects_pending_task(self):
        tasks = self.feature / "tasks.md"
        tasks.write_text(
            "# Tasks\n**Estado:** COMPLETED\n"
            "## TASK-001 — Work\n**Estado:** TODO\n"
            "| Orden | Tarea | Estado |\n| 1 | TASK-001 | TODO |\n",
            encoding="utf-8",
        )
        self.assertIn("INCOMPLETE_TASKS", self._codes())

    def test_task_state_must_be_a_standalone_field(self):
        tasks = self.feature / "tasks.md"
        tasks.write_text(
            "# Tasks\n**Estado:** DRAFT\n"
            "## TASK-001 — Work\n**Estado:** TODO. **Tipo:** TEST.\n"
            "| Orden | Tarea | Estado |\n| 1 | TASK-001 | TODO |\n",
            encoding="utf-8",
        )
        self.assertIn("INVALID_TASK_FORMAT", self._codes())

    def test_validated_report_cannot_close_approved_tasks(self):
        plan = self.feature / "plan.md"
        plan.write_text("# Plan\n**Estado:** APPROVED\n", encoding="utf-8")
        tasks = self.feature / "tasks.md"
        tasks.write_text(
            "# Tasks\n**Estado:** APPROVED\n"
            "## TASK-001 — Work\n**Estado:** TODO\n"
            "| Orden | Tarea | Estado |\n| 1 | TASK-001 | TODO |\n",
            encoding="utf-8",
        )
        (self.feature / "validation.md").write_text(
            "**Result:** PASS\n**SPEC Compliance:** PASS\n"
            "**Feature Status:** VALIDATED\n",
            encoding="utf-8",
        )
        issues = audit_repository(self.root)
        self.assertIn("PREMATURE_VALIDATION", {issue.code for issue in issues})
        self.assertNotIn("SPEC-008", projected_state(self.root)[0]["validated"])

    def test_validated_report_needs_final_pass_result(self):
        plan = self.feature / "plan.md"
        plan.write_text("# Plan\n**Estado:** APPROVED\n", encoding="utf-8")
        tasks = self.feature / "tasks.md"
        tasks.write_text(
            "# Tasks\n**Estado:** COMPLETED\n"
            "## TASK-001 — Work\n**Estado:** DONE\n"
            "| Orden | Tarea | Estado |\n| 1 | TASK-001 | DONE |\n",
            encoding="utf-8",
        )
        (self.feature / "validation.md").write_text(
            "**Result:** BLOCKED\n**SPEC Compliance:** PASS\n"
            "**Feature Status:** VALIDATED\n",
            encoding="utf-8",
        )
        self.assertIn("INVALID_VALIDATION_RESULT", self._codes())
        self.assertNotIn("SPEC-008", projected_state(self.root)[0]["validated"])

    def test_later_blocked_result_overrides_earlier_pass(self):
        self._closed_feature()
        validation = self.feature / "validation.md"
        validation.write_text(
            validation.read_text() + "**Result:** BLOCKED\n",
            encoding="utf-8",
        )
        self.assertIn("INVALID_VALIDATION_RESULT", self._codes())
        self.assertNotIn("SPEC-008", projected_state(self.root)[0]["validated"])

    def test_declared_blocking_findings_prevent_validation(self):
        (self.feature / "plan.md").write_text(
            "# Plan\n**Estado:** APPROVED\n", encoding="utf-8"
        )
        (self.feature / "tasks.md").write_text(
            "# Tasks\n**Estado:** COMPLETED\n"
            "## TASK-001 — Work\n**Estado:** DONE\n"
            "| Orden | Tarea | Estado |\n| 1 | TASK-001 | DONE |\n",
            encoding="utf-8",
        )
        (self.feature / "validation.md").write_text(
            "**Result:** PASS\nBlocking findings: 1\n"
            "**SPEC Compliance:** PASS\n**Feature Status:** VALIDATED\n",
            encoding="utf-8",
        )
        self.assertIn("BLOCKING_VALIDATION_FINDING", self._codes())

    def test_structural_evidence_accepts_complete_report(self):
        self._closed_feature()
        self.assertIn("SPEC-008", projected_state(self.root)[0]["validated"])
        self.assertFalse({
            issue.code for issue in audit_repository(self.root)
        } & {"MISSING_AC_EVIDENCE", "MISSING_TASK_EVIDENCE", "MISSING_TEST_RESULT", "INVALID_EVIDENCE_PATH"})

    def test_missing_ac_result_rejects_validation(self):
        self._closed_feature()
        validation = self.feature / "validation.md"
        validation.write_text(
            validation.read_text().replace(
                "| AC-001 | TEST-001; `evidence/result.md` | PASS |\n", ""
            ), encoding="utf-8",
        )
        self.assertIn("MISSING_AC_EVIDENCE", self._codes())
        self.assertNotIn("SPEC-008", projected_state(self.root)[0]["validated"])

    def test_broken_evidence_path_rejects_validation(self):
        self._closed_feature()
        validation = self.feature / "validation.md"
        validation.write_text(
            validation.read_text().replace("evidence/result.md", "evidence/missing.md"),
            encoding="utf-8",
        )
        self.assertIn("INVALID_EVIDENCE_PATH", self._codes())

    def test_evidence_path_cannot_escape_feature(self):
        self._closed_feature()
        validation = self.feature / "validation.md"
        validation.write_text(
            validation.read_text().replace(
                "| AC-001 | TEST-001; `evidence/result.md` | PASS |",
                "| AC-001 | TEST-001; `../evidence/result.md` | PASS |",
            ), encoding="utf-8",
        )
        self.assertIn("INVALID_EVIDENCE_PATH", self._codes())

    def test_missing_test_result_rejects_validation(self):
        self._closed_feature()
        validation = self.feature / "validation.md"
        validation.write_text(
            validation.read_text().replace(
                "| TEST-001 | `evidence/result.md` | PASS |\n", ""
            ), encoding="utf-8",
        )
        self.assertIn("MISSING_TEST_RESULT", self._codes())

    def test_failed_test_row_cannot_be_counted_as_pass(self):
        self._closed_feature()
        validation = self.feature / "validation.md"
        validation.write_text(
            validation.read_text().replace(
                "| TEST-001 | `evidence/result.md` | PASS |",
                "| TEST-001 | PASS | FAIL |",
            ), encoding="utf-8",
        )
        self.assertIn("MISSING_TEST_RESULT", self._codes())

    def test_conflicting_pass_and_fail_rows_reject_validation(self):
        self._closed_feature()
        validation = self.feature / "validation.md"
        validation.write_text(
            validation.read_text()
            + "| AC-001 | `evidence/result.md` | FAIL |\n"
            + "| TASK-001 | `evidence/result.md` | FAIL |\n"
            + "| TEST-001 | `evidence/result.md` | FAIL |\n",
            encoding="utf-8",
        )
        codes = self._codes()
        self.assertIn("CONFLICTING_AC_RESULT", codes)
        self.assertIn("CONFLICTING_TASK_RESULT", codes)
        self.assertIn("CONFLICTING_TEST_RESULT", codes)
        self.assertNotIn("SPEC-008", projected_state(self.root)[0]["validated"])

    def test_missing_task_evidence_rejects_validation(self):
        self._closed_feature()
        validation = self.feature / "validation.md"
        validation.write_text(
            validation.read_text().replace(
                "| TASK-001 | `evidence/result.md` | PASS |\n", ""
            ), encoding="utf-8",
        )
        self.assertIn("MISSING_TASK_EVIDENCE", self._codes())

    def test_legacy_is_not_promoted_to_new_approval(self):
        (self.root / "docs/audit-history.md").write_text(
            "Source audit marker\n", encoding="utf-8"
        )
        transition = self.root / "specs/007-chat-independent-state"
        transition.mkdir()
        (transition / "decisions.json").write_text(
            '{"schema_version": 1, "events": []}', encoding="utf-8"
        )
        legacy = self.root / "specs" / "006-tdd-workflow"
        legacy.mkdir()
        (legacy / "spec.md").write_text("**Estado:** APPROVED\n", encoding="utf-8")
        (legacy / "plan.md").write_text("**Estado:** APPROVED\n", encoding="utf-8")
        (legacy / "tasks.md").write_text(
            "# Tasks\n**Estado:** COMPLETED\n"
            "## TASK-001 — Work\n**Estado:** DONE\n"
            "| Orden | Tarea | Estado |\n| 1 | TASK-001 | DONE |\n",
            encoding="utf-8",
        )
        (legacy / "evidence").mkdir()
        (legacy / "evidence/result.md").write_text(
            "Synthetic legacy evidence\n", encoding="utf-8"
        )
        (legacy / "validation.md").write_text(
            "**Result:** PASS\n**SPEC COMPLIANCE:** PASS\n"
            "**FEATURE STATUS:** VALIDATED\n"
            "`evidence/result.md`\n| TASK-001 | evidence | PASS |\n",
            encoding="utf-8",
        )
        handoff = self.root / "handoff.md"
        handoff.write_text(
            handoff.read_text(encoding="utf-8").replace(
                '"validated": []', '"validated": ["SPEC-006"]'
            ), encoding="utf-8"
        )
        index = self.root / "docs/index.md"
        index.write_text(
            index.read_text(encoding="utf-8") + "- `specs/006-tdd-workflow/validation.md`\n",
            encoding="utf-8",
        )
        self.assertEqual(self._codes(), set())

    def test_new_project_first_feature_requires_ledger(self):
        first = self.root / "specs" / "001-new-project"
        first.mkdir()
        (first / "spec.md").write_text("**Estado:** DRAFT\n", encoding="utf-8")
        self.assertIn("MISSING_LEDGER", self._codes())

    def test_empty_directory_is_not_a_feature(self):
        (self.root / "specs" / "009-empty").mkdir()
        self.assertEqual(self._codes(), set())

    def test_revocation_removes_gate_authorization(self):
        self._write_events([
            self._approval(),
            self._approval(
                id="DECISION-002", kind="REVOCATION", supersedes="DECISION-001",
                decision="Approval revoked", artifact_sha256="",
            ),
        ])
        self.assertIn("MISSING_APPROVAL", self._codes())

    def test_new_approval_supersedes_old_content(self):
        old = self._approval()
        self.spec.write_text(
            self.spec.read_text(encoding="utf-8").replace("Required", "Revised"),
            encoding="utf-8",
        )
        new = self._approval(id="DECISION-002", supersedes="DECISION-001")
        self._write_events([old, new])
        self.assertEqual(self._codes(), set())


if __name__ == "__main__":
    unittest.main()
