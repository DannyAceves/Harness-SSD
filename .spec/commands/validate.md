# Comando: Validate

## Propósito

Comprobar con evidencia que la implementación cumple SPEC aprobada. Es el gate final: reconstruir requisito → AC → PLAN → TASK → cambio → prueba → evidencia → resultado `PASS|FAIL|BLOCKED`.

# 1. Entrada

`/validate SPEC-[XXX]` o carpeta de feature con `spec.md`, `plan.md`, `tasks.md` e implementación.

# 2. Precondiciones

SPEC/PLAN `APPROVED`, TASKS `COMPLETED`, TASK requeridas `DONE`, sin bloqueos pendientes y con trabajo verificable. Ejecutar checker y revisar ledger vigente; aprobación ausente, revocada o huella incorrecta impide PASS. Legado SPEC-001 a SPEC-006 se reporta no verificable sin inventar aprobación. Si falla precondición: `VALIDATION STATUS: BLOCKED`.

# 3. Contexto obligatorio

Leer Constitución, cuatro standards, SPEC, PLAN, TASKS, ADR, implementación, pruebas y evidencia. SPEC define comportamiento esperado. Un MUST sin evidencia es `TRACEABILITY GAP` bloqueante.

## Regla normativa de validación

Usar todos los gates, estados, findings y reglas aplicables de `.spec/templates/validation.template.md`, aunque no se repitan aquí. Ante contradicción aplicar precedencia y registrar inconsistencia; no resolverla en silencio.

# 4. Requirement Coverage

Revisar cada FR/NFR/SEC con `PASS|FAIL|BLOCKED|NOT_APPLICABLE`; justificar N/A. Todos los MUST deben estar PASS para resultado final PASS.

# 5. Acceptance Criteria Validation

Verificar cada AC contra conducta real y registrar evidencia/resultados. Código relacionado, sin verificación observable, no basta.

# 6. Validación de pruebas

Revisar TEST requeridos por SPEC/PLAN/TASKS/standard: ID, tipo (`UNIT|INTEGRATION|CONTRACT|E2E|SECURITY|OTHER`), FR/AC/SEC y resultado `PASS|FAIL|BLOCKED|NOT_RUN`. Ningún FAIL/BLOCKED/NOT_RUN requerido demuestra cumplimiento.

# 7. Calidad de evidencia

Detectar tests vacíos, deshabilitados, aserciones débiles, mocks que ocultan conducta, desajustes con SPEC y AC sin prueba. PASS técnico no equivale a PASS funcional. Para conducta automatizable, revisar RED auténtico anterior al cambio, GREEN posterior y resultado tras refactor; test ya verde o fallo de entorno no son RED. Fuera de TDD, comprobar motivo y alternativa; caso automatizable bloqueado por entorno sigue `BLOCKED`.

# 8. Quality Gates

Ejecutar controles relevantes disponibles (formato, lint, tipos, unit/integration/contract/E2E/security, build) y registrar `PASS|FAIL|BLOCKED|NOT_APPLICABLE` con justificación para N/A.

# 9. Security Validation

Validar SEC y, cuando aplique, identidad, permisos/ownership, entradas, datos, secretos, destrucción, uploads, integraciones, logs, errores y acceso. Cada SEC obligatorio exige evidencia y PASS.

## Security Findings

Registrar `SEC-FINDING-[XXX]` como `OPEN|MITIGATED|ACCEPTED|NOT_APPLICABLE`.

### OPEN

Riesgo aún no resuelto; si bloquea, impide PASS.

### MITIGATED

Control aplicado con evidencia verificable de eficacia.

### ACCEPTED

Riesgo aceptado por autoridad correspondiente y documentado; no equivale automáticamente a cumplimiento ni PASS.

### NOT_APPLICABLE

No aplica al alcance, con justificación explícita. Si resolver/aceptar cambia requisitos, alcance o diseño, volver al artefacto dueño y recuperar gates.

# 10. Scope Validation

Comparar archivos creados/modificados/eliminados, dependencias, migraciones, configuración, contratos y conducta con alcance aprobado.

## AUTHORIZED

Respaldado por SPEC/PLAN/TASKS.

## MINOR DEVIATION

Cambio menor necesario y documentado.

## UNAUTHORIZED CHANGE

Cambio significativo sin trazabilidad/aprobación; eliminar o incorporarlo al flujo SDD antes de PASS.

# 11. Scope Creep Check

Detectar funciones, endpoints, refactors, dependencias, arquitectura o conducta no solicitada; registrar `SCOPE CREEP DETECTED` y elemento.

# 12. Architecture Validation

Comparar límites, responsabilidades, dependencias, contratos, datos e integraciones con PLAN, standard y ADR. Registrar `ARCHITECTURE DEVIATION`; resolver bloqueo antes de PASS.

# 13. Regression Validation

Ejecutar pruebas existentes relevantes. Regresión conocida sin resolver produce FAIL salvo reemplazo explícito por SPEC aprobada.

# 14. Task Validation

Cotejar cada TASK `DONE` con objetivo, archivos, TEST, FR/AC, calidad y evidencia. Si falta evidencia suficiente: `TASK VALIDATION: FAIL`.

# 15. Discoveries

Clasificar `DISCOVERY-[XXX]` como `NON_BLOCKING` o `BLOCKING`; bloquea si revela incumplimiento, riesgo SEC obligatorio, regresión, contradicción o invalidez. Lo no bloqueante puede ir a trabajo futuro.

# 16. Matriz final de trazabilidad

Registrar por requisito/AC su DEC/PLAN, TASK, cambio, TEST/evidencia y resultado. Toda fila obligatoria termina PASS.

# 17. Missing Traceability

Marcar `TRACEABILITY GAP` por requisito sin AC, AC sin TASK, TASK sin fuente, cambio sin TASK, conducta requerida sin prueba equivalente o TEST sin conducta relevante. Los gaps obligatorios impiden PASS.

# 18. Resultado final

`PASS` exige todos los MUST, AC, TEST, gates y SEC obligatorios en PASS; TASKS COMPLETED, ninguna TASK incompleta; evidencia suficiente; sin regresión, gap, cambio no autorizado, desviación arquitectónica ni finding `OPEN` bloqueantes.

## FAIL

Evidencia demuestra incumplimiento de requisito, AC, SEC, prueba, regresión o contradicción con SPEC.

## BLOCKED

No puede determinarse cumplimiento por entorno, dependencia, prueba no ejecutable, evidencia o decisión pendiente. Nunca tratar como PASS.

# 19. Manejo de fallos

Escalar al nivel que posee la decisión; repetir validación tras corrección.

## Implementation defect

Volver a `/implement` §17.1: vincular finding, reabrir TASKS/TASK afectadas, conservar evidencia previa, verificar gates, corregir y volver a cerrar antes de `/validate`.

## Task decomposition defect

Volver a `/tasks` y recuperar aprobación si cambia trabajo autorizado.

## Technical design defect

Volver a `/plan` y evaluar dependientes/gates.

## Requirement defect

Volver a `/specify` o `/clarify` y evaluar dependientes/gates.

# 20. Artefacto de validación

Crear `specs/<feature-id>/validation.md` desde `.spec/templates/validation.template.md` sin modificarla durante esta fase. Registrar versiones, cobertura, AC, TEST/TDD, SEC, calidad, alcance, trazabilidad, findings y resultado.
Para `VALIDATED`, incluir una fila PASS por cada AC, TASK y TEST requerido,
con ruta de evidencia existente en `evidence/` o ruta del repo cuando aplique.
El checker comprueba presencia, estados y rutas; `/validate` comprueba además
contenido, calidad y cumplimiento real. Una marca `PASS` sola no basta.

# 21. Salida

Informar cobertura FR/NFR/SEC/AC, pruebas y calidad, gaps, regresiones, cambios no autorizados, findings, resultado `SPEC COMPLIANCE` y `FEATURE STATUS`, con siguiente acción. Solo `SPEC COMPLIANCE: PASS` permite `FEATURE STATUS: VALIDATED`; en otro caso la feature sigue sin validar.

# 22. Self-check

Revisar cada MUST/AC, trazabilidad, TEST/TDD y calidad de evidencia, gates, SEC, regresión, scope, arquitectura, TASK, discoveries y gaps; documentar causas de FAIL/BLOCKED. PASS solo con evidencia suficiente.

# 23. Acciones prohibidas

No declarar PASS sin evidencia, ignorar fallos/SEC/MUST/regresiones/cambios no autorizados, tratar BLOCKED como PASS, adaptar AC a implementación, borrar evidencia desfavorable, cambiar SPEC/PLAN en silencio ni declarar VALIDATED antes del gate.
