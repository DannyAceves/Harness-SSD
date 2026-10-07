# Validation Report

## Metadata

**Validation ID:** VALIDATION-[XXX]
**SPEC:** SPEC-[XXX]
**PLAN:** PLAN-[XXX]
**TASKS:** TASKS-[XXX]
**Status:** DRAFT
**Result:** PENDING
**Date:** YYYY-MM-DD
**Validated by:** [PENDING]

# 1. Objetivo

[Qué feature y versión se valida, contra qué SPEC y con qué evidencia. Resultado permitido: PASS, FAIL o BLOCKED.]

# 2. Artefactos validados

## Specification

**ID:** SPEC-[XXX]
**Version:** [X.Y.Z]
**Status:** APPROVED
**Path:** [spec.md]

## Plan

**ID:** PLAN-[XXX]
**Version:** [X.Y.Z]
**Status:** APPROVED
**Path:** [plan.md]

## Tasks

**ID:** TASKS-[XXX]
**Version:** [X.Y.Z]
**Status:** COMPLETED
**Path:** [tasks.md]

## Implementation

**Reference:** [Archivos/commit/evidence.]

# 3. Precondition Check

| Gate | Result | Evidence |
|------|--------|----------|
| SPEC/PLAN aprobados, ledger y huellas vigentes | PENDING | [Checker/decisions.json] |
| TASKS COMPLETED y TASK requeridas DONE | PENDING | [tasks.md] |
| Sin bloqueos pendientes e implementación presente | PENDING | [Evidencia] |

El legado SPEC-001 a SPEC-006 se identifica como no verificable sin inventar aprobación. Precondición fallida → BLOCKED, no PASS.

# 4. Functional Requirement Coverage

| FR | AC | TASK/cambio | TEST/evidencia | Result |
|----|----|-------------|----------------|--------|
| FR-001 | AC-001 | TASK-001 | TEST-001 | PENDING |

# 5. Non-Functional Requirement Coverage

| NFR | AC | Evidencia/métrica | Result |
|-----|----|------------------|--------|
| NFR-001 | AC-001 | [Medición] | PENDING |

# 6. Security Requirement Coverage

| SEC | AC | Control/evidencia | Result |
|-----|----|------------------|--------|
| SEC-001 | AC-001 | [TEST/validación] | PENDING |

Cada MUST y SEC aplicable debe estar PASS; justificar NOT_APPLICABLE.

# 7. Acceptance Criteria Validation

Registrar una fila por AC con ID, verificación/TEST, ruta local de evidencia
entre backticks y resultado `PASS|FAIL|BLOCKED`. El checker exige todos los
AC de SPEC en PASS antes de `VALIDATED`; el análisis humano revisa su calidad.

| AC | TEST/verificación y evidencia | Result |
|----|-------------------------------|--------|
| AC-001 | TEST-001; `evidence/task-001.md` | PENDING |

## AC-001 — [Título]
**Related requirements:** [FR/NFR/SEC]
### Given
[Precondición aprobada.]
### When
[Acción.]
### Then
[Resultado esperado.]
### Evidence
[TEST y enlace verificable.]
### Result
[PASS | FAIL | BLOCKED]

# 8. Test Results

Cada TEST requerido en TASKS debe aparecer con ID, resultado PASS y referencia
comprobable. Usar rutas locales existentes entre backticks, por ejemplo
`evidence/task-001.md`; no usar rutas externas ni rutas con `..`.

| TEST | Type | FR/AC/SEC | Command/evidence | Result |
|------|------|-----------|------------------|--------|
| TEST-001 | UNIT / INTEGRATION / CONTRACT / E2E / SECURITY / OTHER | FR-001, AC-001 | [Comando/enlace] | PENDING |

FAIL, BLOCKED y NOT_RUN no prueban cumplimiento.

## 8.1 TDD Evidence Review

Para features posteriores a la política, comprobar RED anterior al cambio y causado por conducta faltante, GREEN posterior y prueba tras refactor cuando hubo. No exigir RED retroactivo a features ya validadas.

| TASK / TEST | Aplicabilidad | RED y causa | GREEN / refactor | Motivo y alternativa si N/A | Resultado |
|-------------|---------------|-------------|------------------|-----------------------------|-----------|
| TASK-001 / TEST-001 | OBLIGATORIO / NO APLICA | [Enlace/N/A] | [Enlace/N/A] | [Motivo/verificación] | PENDING |

Fallo de entorno no es RED y mantiene BLOCKED; excepción sin evidencia suficiente no permite PASS.

# 9. Evidence Quality Review

- [ ] Aserciones significativas, tests requeridos habilitados, mocks representativos.
- [ ] Pruebas verifican conducta y AC de la SPEC vigente; no se debilitó evidencia para PASS.

Findings: [Ninguno / referencias.]

# 10. Quality Gates

| Gate | Result | Evidence |
|------|--------|----------|
| Format/Lint/Types | PENDING / NOT_APPLICABLE | [Comando/razón] |
| Unit/Integration/Contract/E2E/Security | PENDING / NOT_APPLICABLE | [Comando/razón] |
| Build | PENDING / NOT_APPLICABLE | [Comando/razón] |

Justificar gates inexistentes o no aplicables.

# 11. Security Validation

[Revisar autenticación, autorización/ownership, entradas, datos, secretos, destrucción, uploads, integraciones, logs, errores y acceso cuando aplique.]

## Findings

| ID | Requirement | Finding | Severity | Status | Evidence/decision |
|----|-------------|---------|----------|--------|-------------------|
| SEC-FINDING-001 | SEC-[XXX] | [Riesgo] | LOW / MEDIUM / HIGH | OPEN | [Enlace] |

`OPEN`: no resuelto; `MITIGATED`: mitigación con evidencia; `ACCEPTED`: aceptación por autoridad con alcance/justificación, sin equivaler a SEC PASS; `NOT_APPLICABLE`: justificar. Excepción o cambio funcional/técnico vuelve al artefacto dueño y sus gates. Si no hay hallazgos, escribirlo expresamente.

# 12. Scope Validation

## Files Created

[Rutas o ninguno.]

## Files Modified

[Rutas o ninguno.]

## Files Removed

[Rutas o ninguno.]

## Dependencies Added

[Dependencias o ninguna.]

## Migrations

[Migraciones o ninguna.]

## Configuration Changes

[Cambios o ninguno.]

Comparar también contratos y conducta con alcance aprobado.

# 13. Scope Deviations

| ID | Change | Classification | Reason | Blocking |
|----|--------|----------------|--------|----------|
| DEV-001 | [Cambio] | AUTHORIZED / MINOR DEVIATION / UNAUTHORIZED CHANGE | [Motivo] | YES / NO |

Cambio significativo no autorizado impide PASS hasta retirarlo o integrarlo en SDD.

# 14. Architecture Validation

[Cotejar PLAN, standard y ADR: límites, responsabilidades, dependencias, contratos, datos e integraciones.]

## Architecture Deviations

[Desviaciones y resolución, o ninguna.]

# 15. Regression Validation

| TEST/flujo | Resultado | Evidencia |
|------------|-----------|-----------|
| [Regresión relevante] | PENDING | [Comando/enlace] |

Una regresión conocida sin resolver impide PASS salvo reemplazo aprobado en SPEC.

# 16. Task Validation

Registrar una fila por TASK requerida con ID, evidencia local y resultado
PASS. Debe coincidir con la ficha `DONE` y la tabla de orden de TASKS.

| TASK | DoD y evidencia | Result |
|------|----------------|--------|
| TASK-001 | [Enlace] | PENDING |

# 17. Discoveries

| ID | Hallazgo | Blocking | Acción |
|----|----------|----------|--------|
| DISCOVERY-001 | [Descripción] | YES / NO | [Acción] |

# 18. Final Traceability Matrix

| Requirement | AC | Plan | Task | Implementation | Test/Evidence | Result |
|-------------|----|------|------|----------------|---------------|--------|
| FR-001 | AC-001 | DEC-001 | TASK-001 | [Ruta] | TEST-001 | PENDING |

# 19. Traceability Gaps

## Gaps

| ID | Type | Artifact | Description | Blocking |
|----|------|----------|-------------|----------|
| GAP-001 | [Tipo] | [Referencia] | [Falta] | YES / NO |

Si no hay gaps, declararlo; uno bloqueante impide PASS.

# 20. Validation Findings

Registrar todo problema relevante.

## FINDING-001 — [Title]

**Type:** [IMPLEMENTATION | TASK | PLAN | SPEC | SECURITY | REGRESSION | TRACEABILITY | SCOPE | ARCHITECTURE | ENVIRONMENT]
**Severity:** [LOW | MEDIUM | HIGH]
**Related artifacts:** [Rutas/IDs]
**Description:** [Problema.]
**Evidence:** [Enlace.]
**Status:** [OPEN | RESOLVED]
**Required action:** [Acción.]

# 21. Findings Summary

| Severity | Open | Resolved |
|----------|-----:|---------:|
| HIGH | 0 | 0 |
| MEDIUM | 0 | 0 |
| LOW | 0 | 0 |

Blocking findings: [Número.]

# 22. Requirement Summary

| Grupo | PASS | FAIL | BLOCKED |
|-------|-----:|-----:|--------:|
| FR | 0 | 0 | 0 |
| NFR | 0 | 0 | 0 |
| SEC | 0 | 0 | 0 |
| AC | 0 | 0 | 0 |

# 23. Test Summary

| Tipo | PASS | FAIL | BLOCKED |
|------|-----:|-----:|--------:|
| Unit | 0 | 0 | 0 |
| Integration | 0 | 0 | 0 |
| Contract | 0 | 0 | 0 |
| E2E | 0 | 0 | 0 |
| Security | 0 | 0 | 0 |
| Regression | 0 | 0 | 0 |

# 24. Final Gate

- [ ] MUST, AC, TEST, calidad y SEC obligatorios en PASS; evidencia TDD aplicable válida o N/A justificado con alternativa.
- [ ] TASKS COMPLETED, todas las TASK requeridas DONE y evidencia suficiente.
- [ ] Sin regresiones, gaps, cambios no autorizados, desviaciones arquitectónicas ni findings OPEN bloqueantes.

# 25. Final Result
**Validation Status:** DRAFT
**SPEC Compliance:** PENDING
Resultados permitidos: `PASS | FAIL | BLOCKED`.
**Feature Status:** NOT_VALIDATED

Solo con `SPEC Compliance: PASS` usar `Feature Status: VALIDATED`. Registrar ambos campos en el reporte final.

# 26. Required Next Action

PASS → cierre; defecto de implementación → `/implement` §17.1 (finding, reapertura, evidencia anterior, precondiciones, corrección y nueva validación); desglose → `/tasks`; diseño → `/plan`; requisito → `/specify` o `/clarify`; bloqueo externo → resolver y repetir `/validate`.

# 27. Approval

**Validated by:** [Human / authorized validator]
**Date:** YYYY-MM-DD
**Notes:** [Notas opcionales.]
