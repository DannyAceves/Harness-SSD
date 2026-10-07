# TASK-001 — Inventario y baseline

**Fecha:** 2026-10-07. **TEST-001:** PASS. **Traza:** FR-002/003,
NFR-001, AC-002/003/004.

Se inspeccionaron las nueve carpetas con `spec.md`, `tasks.md` y
`validation.md`. `specs/005-changelog-filesystem/` no contiene SPEC y no es
una feature. Baseline: `PYTHONDONTWRITEBYTECODE=1 python3
src/check_harness_state.py` → PASS; `PYTHONDONTWRITEBYTECODE=1 python3 -m
unittest discover -s tests -q` → 38 tests, PASS.

| Feature | AC en SPEC | Formato de AC en validación | TASK | Formato de evidencia |
|---------|-----------:|-----------------------------|-----:|----------------------|
| 001 | 9 | tabla por AC | 4 | filas por TASK; archivos de evidencia específicos |
| 002 | 5 | secciones `## AC` y tablas de requisito | 4 | filas por TASK; `evidence/implementation.md` |
| 003 | 6 | secciones `## AC` y tablas de requisito | 4 | filas por TASK; `evidence/implementation.md` |
| 004 | 5 | tabla por AC | 4 | filas por TASK; `evidence/implementation.md` |
| 005 | 3 | tabla por AC | 3 | filas por TASK; `evidence/implementation.md` |
| 006 | 5 | tabla por AC | 5 | filas por TASK; `evidence/implementation.md` |
| 007 | 6 | tabla por AC | 5 | filas por TASK; `evidence/task-*.md` |
| 008 | 7 | matriz por requisito; AC en segunda columna | 7 | rango TASK-001 a TASK-007; `evidence/implementation.md` |
| 009 | 4 | tabla por AC | 11 | rangos/agrupaciones; cinco archivos en `evidence/` |

Todas las SPEC usan encabezados `## AC-[XXX]`; TASKS usan
`## TASK-[XXX]` y tablas de orden de tres o cuatro columnas. En 009,
`**Estado:** TODO. **Tipo:** ...` en las once fichas contradice `DONE` en la
tabla. Los reportes finales alternan campos Markdown, valores en línea
siguiente y marcas de texto plano. Las validaciones 001–006 son legado de
aprobación no verificable; 007–009 tienen ledger.

**Riesgos concretos:** buscar AC solo en primera columna perdería 002/003/008;
exigir una fila por TASK perdería 008/009; leer únicamente una marca final
perdería 002/003 y variantes en 001/004. El parser debe aceptar únicamente
las variantes observadas, con resultado por AC/TASK/TEST y ruta de evidencia
existente, sin declarar calidad semántica. No se cambió código ni historia.
