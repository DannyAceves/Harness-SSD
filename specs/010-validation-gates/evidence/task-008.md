# TASK-008 — Regresión integrada

**Traza:** FR-001 a FR-005, NFR-001/002, SEC-001, AC-001 a AC-005.
**TEST-008:** PASS. **Fecha:** 2026-10-07.

| Control | Resultado |
|---------|-----------|
| `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v` | 53/53 PASS, 0 skipped |
| `PYTHONDONTWRITEBYTECODE=1 python3 src/check_harness_state.py` | HARNESS STATE: PASS |
| `git diff --check` | PASS |
| Nueve features históricas en proyección | SPEC-001 a SPEC-009 VALIDATED |
| `.spec` | 15 Markdown, 2,257 líneas; máximo 298 |
| TASKS-009 | 11/11 fichas y filas DONE; DECISION-004 vigente; revalidación §28 |

Los negativos de cierre prematuro, ficha/tabla distinta, AC/TEST faltante,
ruta de evidencia rota o escapada y resultado FAIL se rechazan en tests.
El flujo completo de adopción pasa desde un destino limpio. No quedan
bloqueos ni cambios fuera de SPEC-010/PLAN-010/TASKS-010; la evidencia TDD
de conducta nueva está en task-002/003/004, y las alternativas documentales
o de integración en task-001/005/006/007. Esta tarea consolida resultados;
TDD no aplica porque no cambia conducta.

**Regresión tras FINDING-001:** TASK-008 se reabrió porque cambió el checker
después del reporte inicial. `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest
discover -s tests -q` → 54/54 PASS;
`PYTHONDONTWRITEBYTECODE=1 python3 src/check_harness_state.py` → PASS;
`git diff --check` → PASS. El nuevo negativo de resultados contradictorios
rechaza PASS/FAIL simultáneos para AC, TASK y TEST; las nueve features
históricas conservan su proyección válida.

**Regresión tras FINDING-002:** el negativo del resultado final posterior
`BLOCKED` también falla correctamente; suite completa 55/55 PASS, checker
PASS y `git diff --check` PASS. TASK-004 y TASK-008 vuelven a DONE, sin
bloqueos ni regresiones conocidas.
