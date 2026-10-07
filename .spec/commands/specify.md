# Comando: Specify

## Propósito

Convertir una petición en `specs/<feature-id>/spec.md`, según la Constitución. Describe **qué** y **por qué**; no implementa.

# 1. Entradas

Una idea, problema, mejora, nueva función o cambio de comportamiento expresado por el usuario (`/specify <descripción>`).

# 2. Contexto obligatorio

Leer `.spec/constitution.md`, los cuatro `.spec/standards/`, `.spec/templates/specification.template.md` y documentación relevante. Rige la precedencia constitucional.

# 3. Regla principal

Definir resultado observable y motivo. No anticipar arquitectura, BD física, endpoints, clases, framework, librerías o algoritmos salvo restricción explícita existente.

# 4. Identificación de la SPEC

Asignar `SPEC-[XXX]` único y carpeta `specs/<feature-id>/`. No reutilizar IDs.

# 5. Nombre de la feature

Usar `<NNN>-<slug-descriptivo>` en minúsculas y guiones; evitar nombres vagos o largos.

# 6. Análisis de la petición

Identificar problema, objetivo, actores, comportamientos, restricciones, seguridad y casos límite sin inventar requisitos.

## Problema

Qué necesidad origina la petición.

## Objetivo

Qué resultado se espera.

## Actores

Quién usa o recibe el comportamiento.

## Comportamientos

Qué debe poder hacer el sistema.

## Restricciones

Qué límites ya existen.

## Seguridad

Revisar autenticación, autorización, datos sensibles, permisos y operaciones destructivas.

## Casos límite

Identificar escenarios que puedan cambiar el comportamiento.

# 7. Detección de ambigüedad

Marcar `[NEEDS CLARIFICATION]` si falta una decisión que cambie alcance, comportamiento, permisos, seguridad, datos o AC. No elegirla en silencio.

# 8. Cuándo NO utilizar NEEDS CLARIFICATION

Resolver con petición explícita, Constitución, standards, SPEC aprobada relacionada, regla documentada o restricción existente. Dejar los detalles puramente técnicos para PLAN.

# 9. Clasificación de aclaraciones

Registrar ID, pregunta, contexto, impacto y `Bloqueante: YES | NO`.

## Bloqueante

Si afecta comportamiento, alcance, permisos, negocio, seguridad, datos importantes o AC; impide `APPROVED`.

## No bloqueante

No impide definir el comportamiento principal; permanece documentada.

# 10. Generación de requisitos

Usar `FR-[XXX]`, `NFR-[XXX]`, `SEC-[XXX]` y `BR-[XXX]` cuando apliquen. Cada requisito debe ser explícito, verificable y trazable; no usar frases vagas.

# 11. Generación de criterios de aceptación

Cubrir cada MUST con `AC-[XXX]` suficiente. Relacionarlo con requisito y, cuando ayude, formular Given/When/Then para comportamiento observable.

# 12. Priorización

`MUST`: indispensable; `SHOULD`: omitible solo con justificación; `COULD`: opcional. No usar prioridad para eliminar alcance solicitado silenciosamente.

# 13. Suposiciones

Registrar suposiciones no bloqueantes como `ASM-[XXX]`; si cambian significativamente conducta, abrir aclaración en vez de asumir.

# 14. Creación del artefacto

Asignar ID, crear carpeta y `spec.md` con `.spec/templates/specification.template.md`; completar secciones aplicables, preguntas y matriz inicial. No modificar la template. Crear `decisions.json` con `{"schema_version": 1, "events": []}`.

# 15. Self-check

Comprobar problema, objetivo, alcance/fuera de alcance, actores, FR verificables, MUST→AC, SEC, casos límite, suposiciones, ambigüedades y matriz coherente. Evitar decisiones técnicas o funciones inventadas.

# 16. Estado resultante

Con aclaración bloqueante: `SPEC STATUS: DRAFT`, `RESULT: NEEDS CLARIFICATION`, sin PLAN. Sin bloqueos pero pendiente de revisión: `SPEC STATUS: IN_REVIEW`, `RESULT: READY FOR REVIEW`. Solo aprobación humana explícita cambia a `APPROVED`. Registrar decisión, alcance y huella en `decisions.json` según `docs/state-reconstruction.md`; `python3 src/check_harness_state.py` debe dar PASS antes de `/plan`. No reinterpretar legado SPEC-001 a SPEC-006.

# 17. Salida del comando

Informar ID, feature, ruta, cantidades FR/NFR/SEC y AC, aclaraciones bloqueantes/no bloqueantes, estado y siguiente fase.

# 18. Acciones prohibidas

Durante `/specify`, no escribir código, instalar dependencias, migrar, crear endpoints, PLAN o TASKS, decidir negocio sin base ni autoaprobar. Modificar solo SPEC, ledger de la feature y proyecciones de estado/enlaces en `handoff.md` y `docs/index.md`; no alterar contenido sustantivo ajeno.
