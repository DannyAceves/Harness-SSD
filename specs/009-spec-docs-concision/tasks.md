# Tareas: Concisión de los documentos `.spec`

**ID:** TASKS-009  
**SPEC relacionada:** SPEC-009 v0.1.0  
**PLAN relacionado:** PLAN-009 v0.1.0  
**Estado:** COMPLETED  
**Versión:** 0.1.0  
**Fecha:** 2026-10-07

# 1. Precondiciones

- [x] SPEC y PLAN aprobados; DECISION-001/002 vigentes y checker PASS.
- [x] Sin aclaraciones bloqueantes; requisitos MUST y orden cubiertos.

# 2. Objetivo

Reducir los 15 Markdown de `.spec` sin cambiar reglas ni contratos. Cada tarea
documental aplica PLAN DEC-001 a DEC-004. Ninguna tarea autoriza `src/`,
`tests/`, dependencias o cambios de política SDD.

# 3. Estados de tarea

`TODO → IN_PROGRESS → DONE`; `BLOCKED` requiere causa y resolución en el
nivel dueño. La ejecución empieza solo tras aprobar este documento.

# 4. Prioridades

P1 para la equivalencia normativa y compatibilidad; P2 para reducción y
comprobación. Las dependencias, no la prioridad, fijan el orden.

# 5. Convención de identificadores

`TASK-001` a `TASK-011` y `TEST-001` a `TEST-011` son únicos dentro de
SPEC-009. No se reutilizan ni renumeran.

# 6. Tareas

En todas las tareas, **TDD no aplica**: cambia documentación, sin conducta
ejecutable nueva. La verificación alternativa es la indicada como TEST y la
evidencia se guarda en `specs/009-spec-docs-concision/evidence/` durante
`/implement`. Cada tarea termina solo con su TEST en PASS, alcance respetado,
trazabilidad y evidencia revisable.

## TASK-001 — Inventario y reglas de referencia

**Estado:** DONE  
**Tipo:** DOCUMENTATION. **Prioridad:** P1.  
**Depende de:** ninguna.  
**Traza:** FR-001/FR-002/FR-004, NFR-001, AC-001/AC-002/AC-004,
DEC-001/DEC-004.  
**Alcance:** leer los 15 Markdown, citas vigentes, checker y documentos que
consumen secciones; crear solo evidencia de baseline bajo la feature.  
**TEST-001:** inventario exacto con líneas previas, secciones/campos citados y
matriz inicial de obligaciones de gates, TDD, seguridad y validación.  
**DONE:** baseline y matriz enlazados, sin edición de `.spec` en esta tarea.

## TASK-002 — Constitución

**Estado:** DONE  
**Tipo:** DOCUMENTATION. **Prioridad:** P1.  
**Depende de:** TASK-001.  
**Traza:** FR-001/FR-002, NFR-001, AC-001/AC-002, DEC-001/DEC-002.  
**Alcance:** modificar solo `.spec/constitution.md`; preservar artículos,
precedencia, autoridad humana, gates y reglas de cambio.  
**TEST-002:** cotejo artículo por artículo con baseline; conteo <=300 líneas.  
**DONE:** ninguna obligación constitucional ausente y evidencia registrada.

## TASK-003 — Standards de arquitectura y código

**Estado:** DONE  
**Tipo:** DOCUMENTATION. **Prioridad:** P1.  
**Depende de:** TASK-002.  
**Traza:** FR-001/FR-002/FR-003, NFR-001/002, AC-001/002/003,
DEC-001/DEC-002.  
**Alcance:** modificar solo `.spec/standards/architecture.md` y `coding.md`;
conservar controles, excepciones y números de sección.  
**TEST-003:** cotejo por control; cada archivo reducido y <=300 líneas.  
**DONE:** controles aplicables y evidencia completos.

## TASK-004 — Standards de pruebas y seguridad

**Estado:** DONE  
**Tipo:** DOCUMENTATION. **Prioridad:** P1.  
**Depende de:** TASK-002.  
**Traza:** FR-001/FR-002/FR-003/FR-004, NFR-001/002, AC-001/002/003/004,
DEC-001/DEC-002.  
**Alcance:** modificar solo `.spec/standards/testing.md` y `security.md`;
conservar testing §21, TDD, secretos, hallazgos y demás controles.  
**TEST-004:** cotejo por control y citas, cada archivo <=300 líneas.  
**DONE:** políticas y evidencia completas, sin debilitar requisitos.

## TASK-005 — Commands de especificación y aclaración

**Estado:** DONE  
**Tipo:** DOCUMENTATION. **Prioridad:** P1.  
**Depende de:** TASK-003, TASK-004.  
**Traza:** FR-001/FR-002/FR-003, NFR-001/002, AC-001/002/003,
DEC-001/DEC-002.  
**Alcance:** modificar solo `.spec/commands/specify.md` y `clarify.md`;
conservar entradas, precondiciones, límites y estados de ambas fases.  
**TEST-005:** recorrido documental de SPEC nueva y aclaración con template;
ambos archivos <=300 líneas.  
**DONE:** recorrido y cotejo de obligaciones en PASS.

## TASK-006 — Commands de planificación y tareas

**Estado:** DONE  
**Tipo:** DOCUMENTATION. **Prioridad:** P1.  
**Depende de:** TASK-003, TASK-004.  
**Traza:** FR-001/FR-002/FR-003, NFR-001/002, AC-001/002/003,
DEC-001/DEC-002.  
**Alcance:** modificar solo `.spec/commands/plan.md` y `tasks.md`;
conservar gates, trazabilidad, TDD, dependencias y estados.  
**TEST-006:** recorrido documental PLAN→TASKS y cotejo; ambos <=300 líneas.  
**DONE:** pasos y prohibiciones localizables, evidencia en PASS.

## TASK-007 — Command de implementación

**Estado:** DONE  
**Tipo:** DOCUMENTATION. **Prioridad:** P1.  
**Depende de:** TASK-003, TASK-004.  
**Traza:** FR-001/FR-002/FR-003/FR-004, NFR-001/002, AC-001/002/003/004,
DEC-001/DEC-002.  
**Alcance:** modificar solo `.spec/commands/implement.md`; conservar §17.1,
preflight, TDD, scope, reapertura, evidencia y estados.  
**TEST-007:** recorrido de tarea normal y reapertura tras finding; cotejo de
obligaciones y <=300 líneas.  
**DONE:** ambos recorridos y referencias en PASS.

## TASK-008 — Command de validación

**Estado:** DONE  
**Tipo:** DOCUMENTATION. **Prioridad:** P1.  
**Depende de:** TASK-003, TASK-004.  
**Traza:** FR-001/FR-002/FR-003, NFR-001/002, AC-001/002/003,
DEC-001/DEC-002.  
**Alcance:** modificar solo `.spec/commands/validate.md`; conservar
cobertura, seguridad, hallazgos, traceability gaps y gates finales.  
**TEST-008:** recorrido de PASS/BLOCKED/FAIL y cotejo; <=300 líneas.  
**DONE:** criterios de salida y evidencia en PASS.

## TASK-009 — Templates de SPEC y PLAN

**Estado:** DONE  
**Tipo:** DOCUMENTATION. **Prioridad:** P2.  
**Depende de:** TASK-005, TASK-006.  
**Traza:** FR-001/FR-003/FR-004, NFR-001/002, AC-001/003/004,
DEC-001/DEC-003.  
**Alcance:** modificar solo `.spec/templates/specification.template.md` y
`plan.template.md`; conservar campos, IDs y estados.  
**TEST-009:** cotejo de campos y uso con commands; ambos <=300 líneas.  
**DONE:** artefactos de ejemplo pueden completarse sin campo faltante.

## TASK-010 — Templates de TASKS y validación

**Estado:** DONE  
**Tipo:** DOCUMENTATION. **Prioridad:** P2.  
**Depende de:** TASK-006, TASK-007, TASK-008.  
**Traza:** FR-001/FR-002/FR-003/FR-004, NFR-001/002,
AC-001/002/003/004, DEC-001/DEC-003.  
**Alcance:** modificar solo `.spec/templates/tasks.template.md` y
`validation.template.md`; conservar TASK/TEST, estado, TDD, evidencia y gate.  
**TEST-010:** cotejo de campos y uso con commands; ambos <=300 líneas.  
**DONE:** plantillas completas y evidencia en PASS.

## TASK-011 — Integración y verificación final de edición

**Estado:** DONE  
**Tipo:** TEST. **Prioridad:** P1.  
**Depende de:** TASK-002 a TASK-010.  
**Traza:** FR-001/002/003/004, NFR-001/002, BR-001,
AC-001/002/003/004, DEC-001/002/003/004.  
**Alcance:** verificar los 15 Markdown; corregir solo referencias vigentes
afectadas en `AGENTS.md` o `docs/` si hace falta; crear evidencia de cierre.
No modificar históricos aprobados, `src/` ni `tests/`.  
**TEST-011:** cada archivo reducido y <=300, total <=4,500; matriz normativa
completa, citas/rutas válidas, `python3 src/check_harness_state.py`, suite
existente de estado/adopción y `git diff --check` en PASS.  
**DONE:** AC-001 a AC-004 cubiertos con resultados y enlaces; cero gaps
bloqueantes. La validación final sigue en `/validate`.

# 7. Tareas técnicas

TASK-001 y TASK-011 son documentales/de prueba y trazan a FR, AC y DEC
reales. No hay tareas técnicas huérfanas ni infraestructura nueva.

# 8. Grafo de dependencias

`001 → 002 → {003,004} → {005,006,007,008} → {009,010} → 011`.
TASK-009 requiere 005/006; TASK-010 requiere 006/007/008; TASK-011 requiere
todas las tareas editoriales. No hay ciclos.

# 9. Orden sugerido de ejecución

| Orden | Tarea | Depende de | Estado |
|------:|-------|------------|--------|
| 1 | TASK-001 | — | DONE |
| 2 | TASK-002 | TASK-001 | DONE |
| 3 | TASK-003 | TASK-002 | DONE |
| 4 | TASK-004 | TASK-002 | DONE |
| 5 | TASK-005 | TASK-003, TASK-004 | DONE |
| 6 | TASK-006 | TASK-003, TASK-004 | DONE |
| 7 | TASK-007 | TASK-003, TASK-004 | DONE |
| 8 | TASK-008 | TASK-003, TASK-004 | DONE |
| 9 | TASK-009 | TASK-005, TASK-006 | DONE |
| 10 | TASK-010 | TASK-006, TASK-007, TASK-008 | DONE |
| 11 | TASK-011 | TASK-002 a TASK-010 | DONE |

TASK-003/004 y TASK-005/006/007/008 pueden progresar por pares sin conflicto
de archivos, respetando dependencias. No se exige paralelización.

# 10. Bloqueos

Ninguno conocido. Si abreviar una regla cambia su sentido, detener la tarea
afectada y resolver según SPEC/PLAN. Un límite de líneas nunca autoriza omitir
una obligación; se revisa SPEC si el conflicto persiste.

# 11. Descubrimientos fuera de alcance

Registrar como `DISCOVERY-[XXX]` en evidencia; no modificar reglas, código ni
documentos históricos fuera de estas tareas.

# 12. Matriz de trazabilidad

| Tarea | Requisitos/AC principales | Decisión | Verificación |
|-------|---------------------------|----------|--------------|
| TASK-001 | FR-001/002/004; AC-001/002/004 | DEC-001/004 | TEST-001 |
| TASK-002 a TASK-004 | FR-001/002/003; AC-001/002/003 | DEC-001/002 | TEST-002 a 004 |
| TASK-005 a TASK-008 | FR-001/002/003/004; AC-001 a 004 | DEC-001/002 | TEST-005 a 008 |
| TASK-009 a TASK-010 | FR-001/003/004; AC-001/003/004 | DEC-001/003 | TEST-009/010 |
| TASK-011 | Todos los MUST y BR-001; AC-001 a 004 | DEC-001 a 004 | TEST-011 |

# 13. Cambios durante implementación

Desviaciones editoriales locales se registran. Una modificación de alcance,
contrato o regla regresa al artefacto dueño y recupera sus gates antes de
ejecutarse. Evidencia de progreso no reabre aprobaciones.

# 14. Criterios para comenzar implementación

- [x] SPEC y PLAN aprobados, requisitos y AC cubiertos, sin tareas huérfanas.
- [x] Dependencias, archivos, verificaciones y DoD definidos; sin bloqueos.
- [x] Aprobación humana explícita de TASKS y registro durable en ledger.

# 15. Estado del documento

**Estado actual:** COMPLETED  
**Aprobado por:** Usuario responsable del proyecto  
**Fecha de aprobación:** 2026-10-07  
**Decisión explícita y alcance:** "Aprobadas las tareas" en respuesta a la
solicitud de aprobación de TASKS-009 v0.1.0; autoriza ejecutar TASK-001 a
TASK-011 conforme a sus dependencias.  
**Registro durable:** `decisions.json`, DECISION-004 (supersedes DECISION-003). El documento
pasará a `IN_PROGRESS` al iniciar TASK-001 y a `COMPLETED` solo con todas las
tareas `DONE` y su evidencia. `/validate` determina la validación final.
