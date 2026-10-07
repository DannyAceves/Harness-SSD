# TASK-005 — Contrato documental

**Traza:** FR-002/003, NFR-001, AC-002/003/004. **TEST-005:** PASS.

Se actualizaron `.spec/commands/tasks.md`, `.spec/commands/validate.md`,
`.spec/templates/tasks.template.md`, `.spec/templates/validation.template.md`
y `docs/state-reconstruction.md`. Ahora declaran ficha TASK como estado
operativo, tabla como espejo, cierre solo con TASKS/TASK coherentes y
validación estructural distinta de revisión semántica. La template de
validación ofrece una fila por AC con TEST/evidencia/resultado y conserva
Given/When/Then de cada AC.

Verificación alternativa a TDD: cotejo con el parser y PLAN DEC-002/003;
`PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -q`
→ 51 tests PASS; `git diff --check` → PASS. La template de validación queda
en 298 líneas, dentro del límite vigente de SPEC-009. No se modificó
Constitución ni se añadió dependencia.
