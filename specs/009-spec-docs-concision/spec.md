# Especificación: Concisión de los documentos `.spec`

**ID:** SPEC-009  
**Estado:** APPROVED  
**Versión:** 0.1.0  
**Fecha:** 2026-10-07

# 1. Resumen

## 1.1 Descripción

Reducir el costo de lectura de todos los Markdown de `.spec` mediante textos
más breves y directos, manteniendo las reglas y campos necesarios para operar
el Harness con seguridad y trazabilidad.

## 1.2 Problema

Los 15 documentos actuales suman 8,672 líneas; diez superan 500 líneas.
Repeticiones, ejemplos extensos y plantillas prolijas consumen contexto del
agente y dificultan localizar la instrucción aplicable.

## 1.3 Objetivo

Que un agente pueda consultar los documentos normativos y las plantillas de
`.spec` con menos contexto, sin perder decisiones, gates, trazabilidad ni
instrucciones operativas necesarias.

# 2. Alcance

## 2.1 Incluido

- Los 15 archivos Markdown actuales de `.spec/constitution.md`,
  `.spec/commands/`, `.spec/standards/` y `.spec/templates/`.
- Consolidar redundancias, acortar ejemplos y simplificar redacción.
- Comprobar la coherencia de referencias, identificadores y formatos que
  consumen agentes, documentación o verificadores del Harness.

## 2.2 Fuera de alcance

- Cambiar las reglas de aprobación, precedencia, límites de mutación o fases SDD.
- Cambiar el comportamiento del comprobador, código de aplicación o pruebas.
- Reescribir documentos históricos de `specs/` o `docs/` por estilo.

# 3. Actores

## ACT-001 — Agente que opera el Harness

Necesita instrucciones breves, completas y localizables por fase.

## ACT-002 — Responsable humano

Necesita revisar que la reducción no altere las obligaciones aprobadas.

# 4. Requisitos funcionales

## FR-001 — Cobertura completa

**Prioridad:** MUST. Revisar y optimizar los 15 Markdown actuales de `.spec`,
incluidos los que hoy tienen menos de 500 líneas. Cada archivo deberá tener una
función clara y evitar repeticiones que ya tengan una fuente autoritativa.

## FR-002 — Equivalencia normativa

**Prioridad:** MUST. Conservar el efecto operativo de las reglas actuales:
precedencia, aprobaciones humanas, ownership, gates, estados, límites de
mutación, trazabilidad, TDD, seguridad y validación. Una abreviación no deberá
convertir una obligación en sugerencia ni eliminar una excepción vigente.

## FR-003 — Instrucciones utilizables

**Prioridad:** MUST. Los commands deberán conservar entradas, precondiciones,
artefactos, flujo, decisiones de estado, salidas y prohibiciones necesarios
para ejecutar cada fase. Los standards deberán conservar controles aplicables
y las templates los campos obligatorios, identificadores y relaciones que
necesitan las features.

## FR-004 — Referencias coherentes

**Prioridad:** MUST. Las referencias vigentes a secciones, campos, estados y
archivos de `.spec` deberán seguir siendo correctas. Cuando una referencia
actual dependa de un número de sección, conservarlo o actualizar la referencia
afectada dentro del alcance autorizado.

# 5. Requisitos no funcionales

## NFR-001 — Reducción verificable

**Prioridad:** MUST. Cada Markdown de `.spec` deberá quedar en 300 líneas o
menos y el conjunto en 4,500 líneas o menos, medidos con `wc -l`. La claridad
y la equivalencia de FR-002 prevalecen ante cualquier conflicto con la cifra:
si una sección no cabe sin pérdida, se documenta el caso y se revisa la SPEC
antes de omitirla.

## NFR-002 — Lectura dirigida

**Prioridad:** MUST. Los documentos deberán permitir encontrar las reglas de
una fase sin abrir otros archivos salvo las fuentes obligatorias o las
referencias explícitas aplicables. Las remisiones deberán nombrar la fuente y
la sección cuando la precisión sea necesaria.

# 6. Requisitos de seguridad

No se introduce manejo de datos o permisos nuevo. La equivalencia de FR-002
incluye íntegramente las obligaciones de `.spec/standards/security.md`,
incluida la protección de secretos y la revisión de hallazgos.

# 7. Reglas de negocio

## BR-001 — Autoridad existente

La reducción editorial no equivale a permiso para cambiar política SDD. Toda
alteración sustantiva detectada debe resolverse en su nivel dueño y gate.

# 8. Criterios de aceptación

## AC-001 — Todos los documentos

**Relacionado con:** FR-001, NFR-001. Dado el inventario de 15 Markdown de
`.spec`, cuando termine la edición, los 15 tendrán una reducción revisable,
ninguno superará 300 líneas y el total no superará 4,500.

## AC-002 — Reglas preservadas

**Relacionado con:** FR-002, BR-001. Dado el texto previo y el nuevo, cuando
se comparen por regla aplicable, ningún gate, obligación, excepción o control
vigente habrá desaparecido o cambiado de fuerza sin una decisión humana
explícita y el gate correspondiente.

## AC-003 — Uso de fases y plantillas

**Relacionado con:** FR-003, NFR-002. Dada una ejecución de cada command y la
creación de SPEC, PLAN, TASKS y validación con sus templates, la documentación
reducida permitirá localizar los pasos y producir artefactos válidos sin
deducir instrucciones ausentes.

## AC-004 — Referencias y estado

**Relacionado con:** FR-004. Dadas las referencias internas y externas a
`.spec`, cuando se comprueben, no habrá rutas, secciones ni campos vigentes
rotos; `python3 src/check_harness_state.py` seguirá en PASS.

# 9. Casos límite y escenarios de error

## EDGE-001 — Texto breve pero ambiguo

Si condensar dos reglas crea una interpretación nueva, conservar la distinción
y priorizar la equivalencia sobre el límite de longitud.

## EDGE-002 — Referencia histórica

Las referencias en artefactos históricos aprobados se respetan; si apuntan a
una sección normativa vigente, conservar su identificador o registrar el
impacto y resolverlo antes de cambiarlo.

# 10. Datos involucrados

Los conceptos son documentos Markdown, secciones normativas, campos de
plantillas y referencias entre archivos. No hay datos de usuario nuevos.

# 11. Dependencias

Constitución y reglas actuales del Harness; comandos y standards relevantes;
registro de estado y checker vigentes.

# 12. Restricciones

- Mantener el flujo SDD y las aprobaciones humanas explícitas.
- Tratar los Markdown de `.spec` como read-only hasta `/implement` con SPEC,
  PLAN y TASKS aprobados para esta feature.
- Mantener el alcance de mutación de cada fase.

# 13. Suposiciones

El inventario de 15 archivos es la base de esta feature. Si aparecen nuevos
Markdown de `.spec` antes de implementar, se evaluará su inclusión en SPEC.

# 14. Preguntas abiertas y necesidades de aclaración

No hay aclaraciones funcionales bloqueantes conocidas.

# 15. Matriz inicial de trazabilidad

| Requisito | Criterios de aceptación | Prioridad |
|-----------|-------------------------|-----------|
| FR-001 | AC-001 | MUST |
| FR-002 | AC-002 | MUST |
| FR-003 | AC-003 | MUST |
| FR-004 | AC-004 | MUST |
| NFR-001 | AC-001 | MUST |
| NFR-002 | AC-003 | MUST |
| BR-001 | AC-002 | MUST |

# 16. Criterios para avanzar a planificación

- [x] Problema, objetivo, alcance, actores y exclusiones definidos.
- [x] Requisitos MUST y controles normativos cubiertos por AC verificables.
- [x] Casos límite y seguridad considerados; sin decisión técnica prematura.
- [x] Aprobación humana explícita y registro durable de esta SPEC.

# 17. Estado de aprobación

**Estado actual:** APPROVED  
**Aprobado por:** Usuario responsable del proyecto  
**Fecha de aprobación:** 2026-10-07  
**Decisión explícita y alcance:** "Aprobado" en respuesta a la solicitud de
aprobación de SPEC-009 v0.1.0 para resumir los 15 Markdown de `.spec` con los
límites y obligaciones definidos en esta SPEC.  
**Registro durable:** `decisions.json`, DECISION-001.
