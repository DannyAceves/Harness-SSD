# TASK-002 — Estados de TASK

**Traza:** FR-003/004, NFR-002, AC-003/005. **TEST-002:** PASS.

- RED: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p test_check_harness_state.py -q` falló con tres aserciones conductuales: el checker no detectaba ficha/tabla distinta, fila duplicada o ausente, ni TASKS `COMPLETED` con TASK pendiente. Un cuarto RED detectó que aceptaba un campo de estado combinado con `Tipo`.
- GREEN: mismo comando → 22 tests PASS. El checker ahora lee la ficha por ID, exige fila única, campo de estado independiente y `DONE` para TASKS `COMPLETED`. Diagnósticos incluyen TASK y ruta.
- Regresión de huella: tests existentes de `canonical_bytes()` permanecen PASS; no se cambió la normalización.
- Comprobación del repo: el checker devuelve FAIL por once fichas `TODO` frente a filas `DONE` de TASKS-009, más `INCOMPLETE_TASKS`; es el hallazgo esperado que reparará TASK-007 tras aprobación específica. No se alteró SPEC-009.

Archivos: `src/check_harness_state.py`, `tests/test_check_harness_state.py`.
No hay dependencias ni secretos nuevos.
