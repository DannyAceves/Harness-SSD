# Constitución del SDD Harness

**Versión:** 1.0.0
**Estado:** Activa

## Propósito

Estos principios gobiernan toda SPEC, PLAN, TASKS, implementación y validación del repositorio.

## Artículo I — Especificación antes de implementación

Ninguna funcionalidad se implementa sin `specs/<feature-id>/spec.md`. La SPEC define problema, requisitos funcionales, no funcionales y de seguridad aplicables, criterios de aceptación, restricciones y suposiciones. No introduce diseño salvo una restricción explícita.

## Artículo II — Los requisitos deben ser verificables

Todo requisito funcional, no funcional o de seguridad debe ser explícito, único, verificable y trazable. Usar `FR-[XXX]` y, según corresponda, `NFR-[XXX]`, `SEC-[XXX]` y `BR-[XXX]`; los criterios usan `AC-[XXX]`. Aclarar requisitos ambiguos antes de implementar.

## Artículo III — Planificación antes de implementación

Toda feature del flujo completo contiene `spec.md`, `plan.md` y `tasks.md` aprobados antes de implementar. SPEC define **qué** lograr, PLAN **cómo** y TASKS el trabajo concreto; no mezclar sus decisiones. Cada aprobación requiere decisión humana explícita.

## Artículo IV — Trazabilidad de tareas

Toda tarea de implementación referencia al menos un requisito o criterio de aceptación. Una tarea técnica puede apoyarse en PLAN, pero debe mostrar su cadena hacia un requisito o AC real. No hay tareas huérfanas.

## Artículo V — Trazabilidad completa

Mantener: requisito → AC → PLAN → TASK → código o documentación → prueba o evidencia → validación. Un requisito solo se completa cuando su realización y validación son identificables.

## Artículo VI — La validación es obligatoria

Escribir código o cerrar tareas no termina una feature. La validación documentada comprueba tareas, pruebas, AC, bloqueos, conformidad con SPEC y trazabilidad. Solo `SPEC COMPLIANCE: PASS` permite `FEATURE STATUS: VALIDATED`.

## Artículo VII — Las pruebas forman parte del proceso

Probar comportamientos observables derivados de requisitos y AC, no solo aumentar cobertura. Cada requisito crítico requiere prueba automatizada o validación explícita documentada.

## Artículo VIII — Los cambios deberán resolverse en su nivel responsable

Ante una decisión incorrecta, incompleta, contradictoria o inviable: detener el trabajo afectado, documentar el conflicto, identificar el nivel dueño, actualizarlo, evaluar dependientes, cambiar solo los elementos afectados, recuperar sus aprobaciones y reanudar tras verificar gates.

- Comportamiento o alcance funcional → SPEC.
- Diseño técnico o arquitectura → PLAN.
- Descomposición, dependencias o ejecución → TASKS.
- Defecto local que no altera niveles superiores → implementación.

La propagación sigue SPEC → PLAN → TASKS → implementación → validación; no exige cambiar automáticamente todos los niveles inferiores. Revisar implementación y evidencia cuando puedan perder validez. Si una feature validada queda afectada, repetir su validación. Nunca modificar silenciosamente una decisión superior.

## Artículo IX — Cumplimiento de estándares

Las decisiones técnicas cumplen `.spec/standards/architecture.md`, `coding.md`, `testing.md` y `security.md`. Un PLAN puede añadir restricciones; no ignorar los standards silenciosamente.

## Artículo X — Explícito sobre implícito

Documentar suposiciones importantes. Ni agentes ni desarrolladores inventan reglas de negocio, requisitos, permisos, relaciones de datos o integraciones. Una incertidumbre significativa exige aclaración antes de implementar.

## Artículo XI — Cambios pequeños y revisables

Dividir la implementación en tareas de objetivo, alcance, trazabilidad y finalización explícitos. Dividir tareas excesivas antes de ejecutarlas.

## Artículo XII — Autoridad humana

La persona responsable decide aprobaciones de SPEC, PLAN y TASKS, cambios de requisitos o alcance, excepciones arquitectónicas y ambigüedades sin resolver. Los agentes analizan, proponen, ejecutan trabajo autorizado y aportan evidencia; no autoaprueban ni redefinen comportamiento esperado.

Registrar las decisiones y aprobaciones nuevas, su alcance y artefacto en el repositorio antes de la fase dependiente. El chat transmite la decisión, pero no es el único registro durable; el registro no sustituye a la persona ni por sí mismo aprueba. Silencio no equivale a aprobación. Una TASK individual puede llegar a `DONE` con evidencia objetiva sin otra aprobación humana, salvo regla explícita del proyecto.

# Definición de terminado (Definition of Done)

Una feature alcanza `FEATURE STATUS: VALIDATED` solo si:

- SPEC y PLAN están `APPROVED`; TASKS está `COMPLETED` y las TASK requeridas en `DONE`.
- Requisitos identificados y verificables, AC definidos, ambigüedades bloqueantes resueltas y trazabilidad demostrable.
- Implementación, pruebas y AC tienen evidencia satisfactoria; no quedan bloqueos o inconsistencias impeditivas.
- La validación está documentada, su resultado es `PASS` y `SPEC COMPLIANCE: PASS`.

`DONE` pertenece a una TASK, `COMPLETED` a TASKS y `VALIDATED` a la feature tras validación final.

# Precedencia

1. Decisiones humanas explícitas y aprobadas.
2. Esta Constitución.
3. Standards del repositorio.
4. SPEC.
5. PLAN.
6. TASKS.
7. Implementación.

Aprobar un artefacto no aprueba implícitamente una contradicción superior. Una excepción a una regla superior requiere decisión humana explícita que identifique regla, alcance, justificación y artefactos afectados. Si la precedencia no resuelve el conflicto, detener el trabajo afectado hasta obtener decisión explícita. Ningún nivel inferior puede modificar o ignorar silenciosamente uno superior.
