# TASK-003 — Gate final y proyección

**Traza:** FR-001, BR-001, NFR-002, AC-001/002/005.
**TEST-003:** PASS.

- RED: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p test_check_harness_state.py -q` falló por cierre `VALIDATED` con TASKS `APPROVED`, resultado final `BLOCKED` y un finding bloqueante declarado.
- GREEN: mismo comando → 25 tests PASS. `audit_repository()` emite `PREMATURE_VALIDATION`, `INVALID_VALIDATION_RESULT` o `BLOCKING_VALIDATION_FINDING`; `projected_state()` solo proyecta VALIDATED cuando pasa el mismo gate.
- El fixture de legado ahora aporta PLAN, TASKS y resultado final coherentes: conserva la exención de aprobación histórica, sin eximir el cierre estructural.
- El checker del repo permanece en FAIL por TASKS-009; su handoff actual queda desactualizado hasta TASK-007. No se corrigió historia sin aprobación.

Archivos: `src/check_harness_state.py`, `tests/test_check_harness_state.py`.
