# TASK-007 — Propuesta de reparación de TASKS-009

**Estado:** DONE tras aprobación humana específica. **Traza:** FR-004,
BR-001, AC-003, DEC-004.

Propuesta exacta: [task-007-proposal.diff](task-007-proposal.diff). Convierte
los once campos combinados `**Estado:** TODO. **Tipo:** ...` en campos
independientes `**Estado:** DONE` y `**Tipo:** ...`, alineados con la tabla
operativa 11/11 DONE. Actualiza la referencia de ledger de DECISION-003 a
DECISION-004 con supersesión. No cambia objetivo, alcance, dependencia,
prioridad, TEST ni evidencia de las tareas. La propuesta cambia la huella
canónica de TASKS-009:

- Vigente: `84f4bf46ec215130f143c78579aec205c3aba0a5d693ba50f61ec0582bd78ead`.
- Propuesta: `167668f1716df1c015a39e9586296870156726f27853199b49d77ed82f8b9984`.

Ensayo aislado: se copió el repositorio SDD a un directorio temporal, se
aplicó la propuesta, se creó un evento de aprobación **sintético** con
`supersedes: DECISION-003`, se reconstruyeron proyecciones y
`audit_repository()` devolvió 0 issues; SPEC-009 se proyectó VALIDATED. Ese
evento no se escribió en el repositorio real y no representa aprobación.

Tras la decisión real: aplicar exactamente el diff, registrar el alcance y
huella en DECISION-004, ejecutar checker/tests, cotejar SPEC/PLAN y añadir
una nota de revalidación a `specs/009-spec-docs-concision/validation.md`
que sustituya la lectura de los TODO como instantánea inicial. Registrar
resultado y huella final aquí. Hasta entonces TASKS-009 permanece intacto.

**Resultado real (2026-10-07):** el responsable respondió «Sí, apruebo esa
corrección» para el diff y la huella propuestos. `patch --dry-run` y la
aplicación exacta pasaron. La huella final fue
`167668f1716df1c015a39e9586296870156726f27853199b49d77ed82f8b9984`;
DECISION-004 tiene `supersedes: DECISION-003`. El checker regresó a PASS,
la suite dio 53/53 PASS y `git diff --check` PASS. Se añadió §28 de
revalidación a SPEC-009. La frase anterior describe el gate previo a esta
decisión y queda conservada como historial.
