# TASK-006 — Ciclo adoptado

**Traza:** FR-005, NFR-001/002, SEC-001, AC-004/005. **TEST-006:** PASS.

`tests/test_adopt_harness.py` ahora instala el Harness en un destino temporal
y recorre SPEC DRAFT→APPROVED, PLAN DRAFT→APPROVED, TASKS DRAFT→APPROVED→
IN_PROGRESS→COMPLETED y reporte final VALIDATED. Usa eventos de aprobación
rotulados como fixtures sintéticas, huellas reales y proyecciones/índice
recalculados por fase. Rechaza cierre prematuro y contradicción ficha/tabla.

No se exige RED nuevo: esta TASK añade una prueba de integración después de
implementar las reglas en TASK-002 a 004; fabricar fallo previo sería
engañoso. Alternativa: aserciones de exit code, estado proyectado y código de
issue en escenarios positivos/negativos. Comandos:
`PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p
test_adopt_harness.py -q` → 10 PASS;
`PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -q`
→ 52 PASS. No se modificó `src/adopt_harness.py` ni se usaron secretos reales.
