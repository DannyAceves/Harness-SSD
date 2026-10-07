# Especificación: Gates de validación y estados de tarea coherentes

**ID:** SPEC-010  
**Estado:** APPROVED  
**Versión:** 0.1.0  
**Fecha:** 2026-10-07

# 1. Resumen

## 1.1 Descripción

El Harness debe detectar cierres prematuros de features, mostrar un estado de
tarea inequívoco y demostrar el recorrido completo en un proyecto adoptado.

## 1.2 Problema

El comprobador acepta un reporte `VALIDATED` aunque TASKS siga en `APPROVED`.
En TASKS-009, las fichas dicen `TODO` y la tabla dice `DONE`. Las pruebas de
adopción actuales terminan en el gate de SPEC, sin recorrer PLAN, TASKS y
validación final.

## 1.3 Objetivo

Que un estado `VALIDATED` solo sea aceptado cuando los gates finales y la
evidencia estructural sean coherentes, y que ese comportamiento funcione en
una adopción limpia.

# 2. Alcance

## 2.1 Incluido

- Comprobar las precondiciones del estado final en features con reporte de
  validación, sin inferir conformidad a partir del texto `PASS` únicamente.
- Definir un estado operativo único por tarea y detectar discrepancias con
  tablas o estado global de TASKS, incluida la de SPEC-009.
- Corregir la representación contradictoria de TASKS-009 mediante el gate de
  cambio que corresponda y revalidar cualquier artefacto afectado.
- Probar un ciclo SPEC → PLAN → TASKS → ejecución → validación en un proyecto
  recién adoptado, con casos negativos de gates.
- Actualizar instrucciones y plantillas afectadas para que el formato sea
  reproducible por agentes y humanos.

## 2.2 Fuera de alcance

- Reescribir el contenido sustantivo de features históricas o inventar
  aprobaciones para SPEC-001 a SPEC-006.
- Afirmar que una comprobación automática demuestra la calidad semántica de
  toda evidencia; esa revisión sigue siendo parte de `/validate`.
- Cambiar el flujo de aprobación humana o añadir dependencias externas.

# 3. Actores

## ACT-001 — Agente o responsable que valida

Necesita un resultado de gate fiable y errores que señalen el artefacto y la
condición incumplida.

## ACT-002 — Equipo que adopta el Harness

Necesita comprobar el ciclo completo desde una copia limpia.

# 4. Requisitos funcionales

## FR-001 — Gate de validación final

**Prioridad:** MUST. Si un reporte declara `SPEC COMPLIANCE: PASS` y
`FEATURE STATUS: VALIDATED`, el comprobador debe exigir SPEC y PLAN
`APPROVED`, TASKS `COMPLETED`, todas las tareas requeridas `DONE`, resultado
final `PASS` y ausencia de bloqueos declarados. Ante incumplimiento debe
devolver FAIL con diagnóstico específico y no proyectar la feature como
validada.

## FR-002 — Evidencia estructural del cierre

**Prioridad:** MUST. Para aceptar `VALIDATED`, la validación debe identificar
los AC obligatorios y su resultado, las tareas requeridas y su evidencia
localizable, y las pruebas o verificaciones que sustentan el cierre. Una
referencia ausente, rota o un resultado distinto de PASS debe impedir el
cierre; el comprobador no debe presentar esta revisión estructural como
garantía de calidad semántica.

## FR-003 — Estado de tarea inequívoco

**Prioridad:** MUST. Cada TASK tendrá un estado operativo identificable; si
también aparece en una tabla de resumen, ambos valores deben coincidir. TASKS
`COMPLETED` exige todas las tareas requeridas `DONE`. Estados ausentes,
desconocidos o contradictorios deberán producir FAIL con el ID de tarea.

## FR-004 — Resolución de SPEC-009

**Prioridad:** MUST. La discrepancia `TODO`/`DONE` de TASKS-009 debe quedar
resuelta sin cambiar retroactivamente el trabajo aprobado en silencio. Si la
corrección cambia contenido protegido por su huella, registrar la nueva
decisión humana y reevaluar su validación según la Constitución.

## FR-005 — Adopción de extremo a extremo

**Prioridad:** MUST. Una prueba en un proyecto adoptado desde cero debe
recorrer los gates de SPEC, PLAN y TASKS, ejecución y validación final; debe
demostrar tanto el cierre válido como el rechazo de al menos un cierre
prematuro y un estado de tarea contradictorio.

# 5. Requisitos no funcionales

## NFR-001 — Compatibilidad histórica

**Prioridad:** MUST. La comprobación debe conservar la exención de
aprobaciones legado documentada para SPEC-001 a SPEC-006, sin extenderla a
proyectos adoptados ni ocultar contradicciones de estado detectables. El
repositorio actual debe seguir siendo comprobable tras resolver SPEC-009.

## NFR-002 — Diagnóstico reproducible

**Prioridad:** MUST. Con los mismos archivos, la comprobación debe producir
el mismo resultado; cada rechazo debe identificar feature, artefacto y causa.

# 6. Requisitos de seguridad

## SEC-001 — Evidencia sin secretos

**Prioridad:** MUST. Las pruebas y registros nuevos deben usar datos
sintéticos y no almacenar credenciales, tokens o datos sensibles reales.

# 7. Reglas de negocio

## BR-001 — Autoridad de los gates

Un reporte de validación no sustituye SPEC, PLAN, TASKS ni aprobación humana.
Una mejora del comprobador no autoriza modificar un artefacto aprobado sin
aplicar su gate de cambio.

# 8. Criterios de aceptación

## AC-001 — Cierre prematuro rechazado

**Relacionado con:** FR-001, BR-001. Dado un reporte que declara PASS y
VALIDATED con TASKS en APPROVED o una tarea pendiente, el comprobador falla,
identifica la causa y no incluye la feature entre las validadas.

## AC-002 — Cierre con evidencia verificable

**Relacionado con:** FR-001, FR-002. Dado un cierre completo con AC, tareas,
pruebas y referencias existentes en PASS, el comprobador acepta VALIDATED;
si falta un elemento requerido o apunta a un archivo inexistente, falla.

## AC-003 — Contradicción detectada

**Relacionado con:** FR-003, FR-004. Dada una tarea con `TODO` en su ficha y
`DONE` en tabla, el comprobador la rechaza por ID. Tras corregir TASKS-009
mediante el gate aplicable, ambas vistas y su validación son coherentes.

## AC-004 — Adopción completa

**Relacionado con:** FR-005, NFR-001. En una adopción limpia, una prueba
recorre todos los gates y obtiene PASS al finalizar; los casos de cierre
prematuro y contradicción obtienen FAIL. El repositorio fuente conserva su
tratamiento de legado y pasa las verificaciones relevantes.

## AC-005 — Seguridad y diagnóstico

**Relacionado con:** NFR-002, SEC-001. Las fallas son reproducibles, señalan
feature/artefacto/causa y las fixtures y evidencias no contienen secretos.

# 9. Casos límite y escenarios de error

- Reporte `VALIDATED` sin SPEC, PLAN o TASKS: FAIL, sin proyección validada.
- TASK duplicada, estado ilegible o resumen incompleto: FAIL explícito.
- Reporte `BLOCKED` o en progreso: permanece activo; nunca se proyecta como
  validado.
- Feature histórica con formato distinto: preservar la exención de
  aprobaciones legado, documentar cualquier límite de lectura de estados y no
  atribuirle aprobación nueva.

# 10. Datos involucrados

Artefactos SDD, estados de TASK, reporte de validación, referencias de
evidencia y ledger de decisiones. No hay datos personales nuevos.

# 11. Dependencias

Constitución; `.spec/commands/validate.md`,
`.spec/templates/tasks.template.md`, `docs/state-reconstruction.md` y el
formato vigente de los artefactos de SPEC-009.

# 12. Restricciones

- Aplicar la precedencia y los gates del repositorio. Código y pruebas solo
  tras SPEC, PLAN y TASKS aprobados.
- No alterar el contenido autorizado de TASKS-009 sin registrar la decisión
  humana correspondiente y reevaluar dependientes.

# 13. Suposiciones

No se requieren suposiciones que cambien el comportamiento solicitado.

# 14. Preguntas abiertas y necesidades de aclaración

Ninguna bloqueante. PLAN definirá el formato mínimo y la estrategia de
compatibilidad para comprobar evidencia y estados.

# 15. Matriz inicial de trazabilidad

| Requisito | AC | Prioridad |
|-----------|----|-----------|
| FR-001, BR-001 | AC-001, AC-002 | MUST |
| FR-002 | AC-002 | MUST |
| FR-003, FR-004 | AC-003 | MUST |
| FR-005, NFR-001 | AC-004 | MUST |
| NFR-002, SEC-001 | AC-005 | MUST |

# 16. Criterios para avanzar a planificación

- [x] Alcance, actores, requisitos, límites y casos de error definidos.
- [x] Todos los MUST tienen AC; no hay aclaraciones bloqueantes.
- [x] Aprobación humana explícita de esta SPEC y registro en `decisions.json`.

# 17. Estado de aprobación

**Estado actual:** APPROVED  
**Aprobado por:** Usuario responsable del proyecto  
**Fecha de aprobación:** 2026-10-07  
**Decisión explícita y alcance:** «Revisado y Aprobado» en respuesta a SPEC-010 v0.1.0; autoriza preparar PLAN-010.  
**Registro durable:** `specs/010-validation-gates/decisions.json`.
