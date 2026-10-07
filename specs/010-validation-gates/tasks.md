# Tareas: Gates de validación y estados de tarea coherentes

**ID:** TASKS-010  
**SPEC relacionada:** SPEC-010 v0.1.0  
**PLAN relacionado:** PLAN-010 v0.1.0  
**Estado:** COMPLETED  
**Versión:** 0.1.0  
**Fecha:** 2026-10-07

# 1. Precondiciones

- [x] SPEC y PLAN `APPROVED`, DECISION-001/002 vigentes; checker PASS.
- [x] Todos los MUST y AC tienen estrategia en PLAN, sin aclaración
  bloqueante ni ADR pendiente.

# 2. Objetivo y convenciones

Implementar PLAN-010 en tareas pequeñas. Cada `**Estado:**` bajo un encabezado
TASK es el estado operativo; la tabla §8 debe repetirlo. `TASK-001` a
`TASK-008` y `TEST-001` a `TEST-008` son locales a SPEC-010. Ninguna tarea
inicia antes de aprobar este documento. Evidencia de ejecución en
`specs/010-validation-gates/evidence/`.

# 3. Tareas

## TASK-001 — Inventario de formatos y baseline

**Estado:** DONE  
**Tipo:** TEST. **Prioridad:** P1.  
**Depende de:** ninguna.  
**Traza:** FR-002/003, NFR-001, AC-002/003/004, DEC-002/003.  
**Alcance:** leer SPEC/TASKS/validación de las nueve features; registrar
variantes de AC, TASK, TEST, evidencia y reporte final. Crear solo evidencia
de inventario; no editar código ni historia.  
**TEST-001:** matriz por feature con formatos y faltantes reales; baseline del
checker y suite existentes. **TDD:** no aplica, inventario documental; el
cotejo reproducible es la alternativa.  
**DONE:** matriz verificable, riesgos de compatibilidad concretos y evidencia
en `evidence/task-001.md`.

## TASK-002 — Estados de TASK y coherencia de tabla

**Estado:** DONE  
**Tipo:** FEATURE. **Prioridad:** P1.  
**Depende de:** TASK-001.  
**Traza:** FR-003/004, NFR-002, AC-003/005, DEC-002/004.  
**Alcance:** modificar `src/check_harness_state.py` y
`tests/test_check_harness_state.py`. Leer fichas/tabla por ID y rechazar
duplicados, ausentes, desconocidos o estados distintos. No editar TASKS-009
en esta tarea.  
**TEST-002:** estados iguales PASS; `TODO`/`DONE`, tabla incompleta,
duplicado o `COMPLETED` con pendiente FAIL con ID/ruta. **TDD:** RED del
caso contradictorio antes de código; GREEN dirigido y regresión, registrados
en `evidence/task-002.md`.  
**DONE:** parser y errores estables; tests relevantes PASS, sin debilitar
huellas ni exención legado.

## TASK-003 — Gate final y proyección compartida

**Estado:** DONE  
**Tipo:** FEATURE. **Prioridad:** P1.  
**Depende de:** TASK-002.  
**Traza:** FR-001, BR-001, NFR-002, AC-001/002/005, DEC-001.  
**Alcance:** checker y sus tests; exigir SPEC/PLAN aprobados, TASKS COMPLETED,
tareas DONE, resultado final PASS y sin bloqueo declarado antes de proyectar
VALIDATED. Mantener diagnóstico explícito.  
**TEST-003:** reporte `VALIDATED` con TASKS `APPROVED` o tarea `TODO` produce
FAIL y proyección activa; cierre válido conserva VALIDATED. **TDD:** RED de
cierre prematuro; GREEN dirigido y regresión en `evidence/task-003.md`.  
**DONE:** audit y proyección coinciden para casos válidos e inválidos.

## TASK-004 — Evidencia estructural de AC, TASK y TEST

**Estado:** DONE  
**Tipo:** FEATURE. **Prioridad:** P1.  
**Depende de:** TASK-001, TASK-003.  
**Traza:** FR-002, NFR-001/002, SEC-001, AC-002/004/005, DEC-003.  
**Alcance:** checker y tests; interpretar formatos inventariados sin
dispensar faltantes, comprobar resultados y rutas locales seguras. No
declarar calidad semántica por parser.  
**TEST-004:** AC/TASK/TEST/evidencia completos PASS; AC ausente o FAIL,
referencia rota, ruta externa o TEST requerido sin PASS producen FAIL.
**TDD:** RED adversos antes de código; GREEN dirigido y regresión en
`evidence/task-004.md`.  
**DONE:** source repo y fixtures válidas pasan; condiciones negativas fallan
con ID/ruta/causa; no hay filtración de secretos.

## TASK-005 — Contrato documental de estados y validación

**Estado:** DONE  
**Tipo:** DOCUMENTATION. **Prioridad:** P1.  
**Depende de:** TASK-002, TASK-004.  
**Traza:** FR-002/003, NFR-001, AC-002/003/004, DEC-002/003.  
**Alcance:** actualizar solo commands/templates de TASKS y validación que
requieran formato explícito, más `docs/state-reconstruction.md`; mantener
Constitución y normas vigentes.  
**TEST-005:** cotejo de formato con parser, campos obligatorios, ejemplos de
estados y distinción entre verificación estructural y `/validate` humano.
**TDD:** no aplica a texto normativo; checker y cotejo son alternativa,
registrados en `evidence/task-005.md`.  
**DONE:** instrucciones y formato coinciden, sin ambigüedad sobre autoridad de
la ficha, tabla o aprobación.

## TASK-006 — Recorrido completo en proyecto adoptado

**Estado:** DONE  
**Tipo:** TEST. **Prioridad:** P1.  
**Depende de:** TASK-004, TASK-005.  
**Traza:** FR-005, NFR-001/002, SEC-001, AC-004/005, DEC-001/003.  
**Alcance:** modificar `tests/test_adopt_harness.py`; fixture temporal con
aprobaciones sintéticas identificadas como tales, nunca como decisiones
humanas reales. No modificar `src/adopt_harness.py` salvo defecto demostrado
que requiera revisión de alcance.  
**TEST-006:** recorrer SPEC, PLAN, TASKS, ejecución y VALIDATED, verificando
PASS por etapa; cierre prematuro y contradicción dan FAIL. **TDD:** no aplica
a esta prueba de integración sobre conducta ya implementada en TASK-002 a
004; comprobar aserciones positivas y negativas, sin fabricar RED, y
registrar resultado en `evidence/task-006.md`.  
**DONE:** flujo completo reproducible en adopción limpia y casos negativos
sin exención de legado.

## TASK-007 — Reparación gobernada de TASKS-009

**Estado:** DONE  
**Tipo:** DOCUMENTATION. **Prioridad:** P1.  
**Depende de:** TASK-002, TASK-004.  
**Traza:** FR-004, BR-001, AC-003, DEC-004.  
**Alcance:** preparar diff mínimo de once estados de TASKS-009 y evaluación
de dependientes en `evidence/task-007.md`; solicitar aprobación humana
específica de la versión corregida. Solo tras recibirla, modificar
`specs/009-spec-docs-concision/tasks.md`, registrar supersesión en su
`decisions.json` y revalidar en su `validation.md`. No alterar alcance,
dependencias, TEST ni evidencia histórica.  
**TEST-007:** antes, detectar contradicción; después de la decisión, 11/11
fichas y tabla DONE, hash/aprobación vigentes, SPEC-009 revalidada. **TDD:**
no aplica al cambio documental; checker y revisión de diff son alternativa.
**DONE:** aprobación específica registrada, reparación mínima, validación y
evidencia en PASS. Sin aprobación, tarea `BLOCKED` y no modificar TASKS-009.

## TASK-008 — Regresión y validación integrada

**Estado:** DONE  
**Tipo:** TEST. **Prioridad:** P1.  
**Depende de:** TASK-005, TASK-006, TASK-007.  
**Traza:** FR-001 a FR-005, NFR-001/002, SEC-001, AC-001 a AC-005,
DEC-001 a DEC-004.  
**Alcance:** ejecutar suite completa, checker, diff check; revisar ledger,
proyecciones, nueve features y trazabilidad de SPEC-010. Registrar evidencia
en `evidence/task-008.md`; no añadir funciones nuevas.  
**TEST-008:** todos los checks relevantes PASS y cero bloqueos; casos
negativos siguen rechazados. **TDD:** no aplica a consolidación; alternativa
es regresión e inspección trazada.  
**DONE:** resultado reproducible, sin tests omitidos, y listo para `/validate`.

# 4. Dependencias y conflictos

`001 → 002 → 003 → 004 → 005 → 006`; `002/004 → 007`; `005/006/007 → 008`.
TASK-002 a 004 comparten checker/tests: ejecutar secuencialmente.
TASK-005/006/007 pueden avanzar en paralelo solo si no comparten archivos;
TASK-007 depende además de decisión humana para mutar SPEC-009. No hay ciclo
ni tarea huérfana.

# 5. Cobertura

| Requisito/AC | Tarea | Prueba |
|--------------|-------|--------|
| FR-001, BR-001; AC-001 | 003, 008 | TEST-003/008 |
| FR-002; AC-002 | 001, 004, 005, 008 | TEST-001/004/005/008 |
| FR-003/004; AC-003 | 002, 005, 007 | TEST-002/005/007 |
| FR-005, NFR-001; AC-004 | 001, 004, 006, 008 | TEST-001/004/006/008 |
| NFR-002, SEC-001; AC-005 | 002/003/004/006/008 | TEST-002/003/004/006/008 |

# 6. Bloqueos y descubrimientos

No hay bloqueo previo a aprobar TASKS-010. La aprobación adicional de
TASKS-009 es precondición futura de la mutación en TASK-007, no está implícita
en esta aprobación. Una falta real de evidencia histórica se documentará;
no se inventará ni se convertirá en PASS. Descubrimientos fuera del alcance
se registran como `DISCOVERY-[XXX]` sin implementarlos automáticamente.

# 7. Criterios para implementación

- [x] SPEC/PLAN aprobados; MUST/AC, dependencias, archivos y TEST cubiertos.
- [x] Sin tareas huérfanas, ciclos ni aclaraciones bloqueantes.
- [x] Aprobación humana explícita de TASKS-010 y ledger/checker PASS.

# 8. Orden y estado de ejecución

| Orden | Tarea | Depende de | Estado |
|------:|-------|------------|--------|
| 1 | TASK-001 | — | DONE |
| 2 | TASK-002 | TASK-001 | DONE |
| 3 | TASK-003 | TASK-002 | DONE |
| 4 | TASK-004 | TASK-001, TASK-003 | DONE |
| 5 | TASK-005 | TASK-002, TASK-004 | DONE |
| 6 | TASK-006 | TASK-004, TASK-005 | DONE |
| 7 | TASK-007 | TASK-002, TASK-004 | DONE |
| 8 | TASK-008 | TASK-005, TASK-006, TASK-007 | DONE |

# 9. Estado del documento

**Estado actual:** COMPLETED  
**Aprobado por:** Usuario responsable del proyecto  
**Fecha de aprobación:** 2026-10-07  
**Decisión explícita y alcance:** «Revisado y aprobado» en respuesta a TASKS-010 v0.1.0; autoriza ejecutar TASK-001 a TASK-008 según dependencias.  
**Registro durable:** `specs/010-validation-gates/decisions.json`.
