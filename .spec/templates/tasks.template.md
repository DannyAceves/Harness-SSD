# Tareas: [Nombre de la funcionalidad]

**ID:** TASKS-[XXX]
**SPEC relacionada:** SPEC-[XXX]
**PLAN relacionado:** PLAN-[XXX]
**Estado:** DRAFT
**Versión:** 0.1.0
**Fecha:** [YYYY-MM-DD]

# 1. Precondiciones

- [ ] SPEC y PLAN `APPROVED`, sin aclaraciones bloqueantes; MUST cubiertos y orden general definido.
- [ ] Checker de estado en PASS.

Si falla: `TASK GENERATION STATUS: BLOCKED`; no crear tareas dependientes de decisiones pendientes.

# 2. Objetivo

Dividir PLAN en TASK pequeñas, trazables, verificables, con alcance, dependencias, DoD y evidencia.

# 3. Estados de tarea

`TODO → IN_PROGRESS → BLOCKED/DONE`; BLOCKED requiere motivo. `DONE → TODO` solo para reapertura según `/implement` §17.1, conservando finding/evidencia. `CANCELLED` reserva un ID retirado, no es estado activo; requiere revisión y gates si cambia trabajo autorizado.
La línea `**Estado:**` de cada ficha es la fuente operativa: no agregarle
otros campos. La tabla §9 la repite una vez por TASK. `COMPLETED` exige todas
las fichas `DONE` y la misma información en la tabla.

# 4. Prioridades

`P0` crítica/bloqueante, `P1` alta, `P2` normal, `P3` baja; no sustituyen dependencias.

# 5. Convención de identificadores

`TASK-[XXX]`, `TEST-[XXX]` únicos y estables; no renumerar ni reutilizar.

# 6. Tareas

## TASK-001 — [Nombre de la tarea]

**Estado:** TODO
**Tipo:** [FEATURE | TECHNICAL | TEST | MIGRATION | SECURITY | CONFIGURATION | DOCUMENTATION | REFACTOR]
**Prioridad:** P1

### Objetivo

[Resultado concreto.]

### Trazabilidad

**Requisitos:** [FR/NFR/SEC/BR reales.]
**Criterios de aceptación:** [AC reales.]
**Decisiones del plan:** [DEC/ADR aplicables.]

### Dependencias

**Depende de:** [TASK-[XXX] o ninguna.]

### Alcance permitido

Crear: [Rutas o ninguna]. Modificar: [Rutas o ninguna]. Reutilizar: [Rutas]. No modificar: [Límite relevante].

### Implementación esperada

[Resultado, sin código detallado ni arquitectura nueva.]

### Pruebas requeridas

- `TEST-001` — [Caso derivado de FR/AC y resultado esperado.]

### TDD

**Aplicabilidad:** [OBLIGATORIO para conducta automatizable | NO APLICA]
**Caso RED previsto:** [TEST, conducta faltante y comando a ejecutar en `/implement`.]
**Evidencia GREEN esperada:** [Comando, resultado y enlace en evidence/.]
**Si no aplica:** [Motivo y verificación alternativa.]

Un entorno que impide prueba automatizable deja la TASK `BLOCKED`; no habilita NO APLICA.

### Validaciones

- [ ] Objetivo, requisitos y AC cubiertos; TEST y regresión relevantes en PASS.
- [ ] Controles de calidad, seguridad y alcance respetados.

### Evidencia esperada

[Archivos, comandos, resultados, RED/GREEN o alternativa, enlaces a evidence/.]

### Definition of Done

- [ ] Resultado cumple SPEC, PLAN y TASK; pruebas requeridas en PASS.
- [ ] RED/GREEN válidos o motivo/alternativa suficiente; sin bloqueos.
- [ ] Evidencia disponible y enlazada.

# 7. Tareas técnicas

Una TASK técnica cita necesidad `DEC/ADR/NFR/SEC` de PLAN y al menos un requisito o AC real soportado, directo o vía cadena explícita. No inventar FR ni usar solo otra TASK como justificación.

# 8. Grafo de dependencias

[Representar TASK→TASK sin ciclos; no iniciar dependientes antes de completar prerrequisitos.]

# 9. Orden sugerido de ejecución

| Orden | Tarea | Depende de | Estado |
|------:|-------|------------|--------|
| 1 | TASK-001 | — | TODO |

La tabla registra progreso; el grafo de dependencias manda sobre el orden sugerido.

# 10. Bloqueos

## BLOCK-001

**Tarea:** TASK-[XXX]
**Estado:** [NEEDS CLARIFICATION]
**Pregunta:** [Decisión faltante.]
**Impacto:** [Trabajo afectado.]
**Bloqueante:** YES
**Origen probable:** [SPEC | PLAN | TASK | EXTERNAL]

Poner TASK `BLOCKED`; actualizar el artefacto dueño, registrar resolución y volver a `TODO/IN_PROGRESS` solo con gates aplicables.

# 11. Descubrimientos fuera de alcance

## DISCOVERY-001

**Detectado durante:** TASK-[XXX]
**Descripción:** [Hallazgo.]
**Impacto:** [LOW | MEDIUM | HIGH]
**Acción recomendada:** [Nueva SPEC | tarea futura | revisión.]

No implementarlo automáticamente.

# 12. Matriz de trazabilidad

| Tarea | Requisito | Criterio | Decisión | Prueba |
|-------|-----------|----------|----------|--------|
| TASK-001 | FR-001 | AC-001 | DEC-001 | TEST-001 |

Todos los MUST que requieren implementación tienen TASK; ninguna tarea huérfana.

# 13. Cambios durante implementación

Cambio de requisito → revisar SPEC; diseño → PLAN; trabajo/dependencias → TASKS. Detener trabajo afectado, evaluar downstream, recuperar aprobación de cada contenido autorizado modificado y comprobar gates antes de continuar. Estado/evidencia sin cambio de trabajo no exige aprobación nueva.

# 14. Criterios para comenzar implementación

- [ ] SPEC/PLAN/TASKS aprobados; MUST, AC, dependencias, alcance, TEST y DoD cubiertos.
- [ ] Sin tareas huérfanas, ciclos, dudas o bloqueos impeditivos; checker PASS.

# 15. Estado del documento

**Estado actual:** DRAFT

`DRAFT → IN_REVIEW → APPROVED → IN_PROGRESS → COMPLETED`. La primera TASK inicia `IN_PROGRESS`; todas las requeridas `DONE`, sin bloqueos y con evidencia permiten `COMPLETED`. Esto no valida la feature. Tras finding de implementación, `COMPLETED → IN_PROGRESS` y reapertura según `/implement` §17.1, sin nueva aprobación si el trabajo autorizado no cambia.

## Aprobación

Solo aprobación humana explícita permite `APPROVED`; ejecución inicial requiere ese estado y ledger/checker PASS.

**Aprobado por:** [PENDIENTE]
**Fecha de aprobación:** [PENDIENTE]
**Decisión explícita y alcance:** [PENDIENTE; contenido de la decisión humana.]
**Registro durable:** `specs/<feature-id>/decisions.json` con huella normalizada.
