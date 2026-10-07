# TASK-004 — Evidencia estructural

**Traza:** FR-002, NFR-001/002, SEC-001, AC-002/004/005.
**TEST-004:** PASS.

- RED: casos de AC ausente, TEST requerido sin resultado, TASK sin evidencia,
  archivo de evidencia inexistente y ruta `../evidence/...` no fueron
  rechazados por el checker previo. Comando:
  `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p test_check_harness_state.py -q`.
- GREEN: mismo comando → 31 tests PASS; suite completa → 51 tests PASS.
- El checker compara AC de SPEC, TASK y TEST de TASKS con resultados PASS
  del reporte y exige al menos un archivo de evidencia local existente.
  Rechaza rutas rotas o fuera del repo. Los nueve formatos históricos se
  interpretan sin exención de resultados; las únicas fallas actuales del
  repositorio pertenecen a la discrepancia aprobada de TASKS-009 y a sus
  proyecciones derivadas.
- La comprobación es estructural. La calidad de TEST, evidencia y cobertura
  real sigue requiriendo `/validate`.

Revisión posterior: se añadió RED para una fila TEST con `PASS` en una celda
y `FAIL` como resultado. Antes contaba erróneamente como PASS; ahora se
rechaza cualquier fila con `FAIL|BLOCKED|PENDING|NOT_RUN`. Suite completa:
53 tests PASS. Se reabrió y cerró TASK-004 durante esta corrección local.

FINDING-001 posterior a `/validate`: un mismo AC/TASK/TEST podía tener una
fila PASS y otra FAIL. RED: el caso de tres resultados contradictorios falló
en `test_conflicting_pass_and_fail_rows_reject_validation`. GREEN: el checker
ahora da prioridad a cualquier FAIL/BLOCKED/PENDING/NOT_RUN de ese ID y
emite `CONFLICTING_AC_RESULT`, `CONFLICTING_TASK_RESULT` o
`CONFLICTING_TEST_RESULT`; 33 tests dirigidos PASS. Se conservó el reporte
anterior y se reabrió TASK-004 sin cambiar trabajo autorizado.

FINDING-002: RED de `test_later_blocked_result_overrides_earlier_pass`
demostró que un `**Result:** BLOCKED` posterior no reemplazaba el PASS
inicial. GREEN: se usa el último resultado explícito; suite completa 55/55
PASS. El checker del repositorio permanece PASS durante la reapertura.

Archivos: `src/check_harness_state.py`, `tests/test_check_harness_state.py`.
No hay secretos reales ni dependencias nuevas.
