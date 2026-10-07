# Especificación: [Nombre de la funcionalidad]

**ID:** SPEC-[XXX]
**Estado:** DRAFT
**Versión:** 0.1.0
**Fecha:** [YYYY-MM-DD]

# 1. Resumen

## 1.1 Descripción

[Resultado esperado en pocas frases.]

## 1.2 Problema

[Problema y por qué importa; sin diseño prematuro.]

## 1.3 Objetivo

[Resultado observable.]

# 2. Alcance

## 2.1 Incluido

- [Comportamientos incluidos.]

## 2.2 Fuera de alcance

- [Exclusiones; no implementarlas en esta feature.]

# 3. Actores

## ACT-001 — [Nombre del actor]

**Descripción:** [Quién es.]
**Responsabilidades o necesidades:** [Qué necesita.]

# 4. Requisitos funcionales

## FR-001 — [Nombre del requisito]

**Descripción:** [Comportamiento verificable.]
**Prioridad:** [MUST | SHOULD | COULD]
**Origen:** [Petición o decisión.]

## FR-002 — [Nombre del requisito]

**Descripción:** [Comportamiento verificable.]
**Prioridad:** [MUST | SHOULD | COULD]
**Origen:** [Petición o decisión.]

# 5. Requisitos no funcionales

## NFR-001 — [Nombre]

**Categoría:** [Rendimiento | Disponibilidad | Escalabilidad | Usabilidad | Observabilidad | Mantenibilidad | Otra]
**Descripción:** [Condición medible.]
**Métrica o condición:** [Cómo verificar.]

# 6. Requisitos de seguridad

## SEC-001 — [Nombre]

**Descripción:** [Control verificable.]
**Riesgo mitigado:** [Riesgo.]

# 7. Reglas de negocio

## BR-001 — [Nombre]

**Regla:** [Regla aplicable.]
**Ejemplo:** [Solo si elimina ambigüedad.]

# 8. Criterios de aceptación

## AC-001 — [Nombre]

**Relacionado con:** FR-001

### Given

[Precondición.]

### When

[Acción.]

### Then

[Resultado observable.]

## AC-002 — [Nombre]

**Relacionado con:** FR-002

### Given

[Precondición.]

### When

[Acción.]

### Then

[Resultado observable.]

# 9. Casos límite y escenarios de error

## EDGE-001 — [Escenario]

**Condición:** [Caso.]
**Comportamiento esperado:** [Resultado.]

# 10. Datos involucrados

Describir conceptos funcionales; no diseñar BD física.

## [Entidad o concepto]

Información requerida: [Campos/conceptos]. Reglas relevantes: [Restricciones].

# 11. Dependencias

[Dependencias conocidas o «Ninguna».]

# 12. Restricciones

[Restricciones de negocio, seguridad, operación o técnica ya decidida.]

# 13. Suposiciones

## ASM-001

[Suposición no bloqueante.]

## ASM-002

[Otra suposición, si aplica.]

# 14. Preguntas abiertas y necesidades de aclaración

Usar `[NEEDS CLARIFICATION]` cuando una decisión faltante pueda cambiar conducta o alcance; no sustituirla con una suposición.

## Q-001 — [Título de la pregunta]

**Estado:** [NEEDS CLARIFICATION]
**Pregunta:** [Pregunta concreta.]
**Contexto:** [Origen de la duda.]
**Impacto:** [FR/AC/SEC afectados.]
**Bloqueante:** [YES | NO]
**Opciones conocidas:** [Alternativas neutrales o ninguna.]
**Respuesta:** [PENDIENTE]
**Resuelto por:** [PENDIENTE]
**Fecha de resolución:** [PENDIENTE]

# 14.1 Ciclo de vida de una aclaración

`[NEEDS CLARIFICATION] → [CLARIFIED]`: registrar respuesta, responsable y fecha; actualizar FR/AC/SEC afectados. Resolver Q sin propagar su contenido no basta.

# 15. Matriz inicial de trazabilidad

| Requisito | Criterios de aceptación | Prioridad |
|-----------|-------------------------|-----------|
| FR-001 | AC-001 | MUST |
| FR-002 | AC-002 | SHOULD |
| SEC-001 | [AC aplicable] | MUST |

# 16. Criterios para avanzar a planificación

- [ ] Problema, alcance, actores, FR/NFR/SEC/BR y casos límite aplicables definidos.
- [ ] MUST con AC verificables y matriz consistente; sin aclaraciones bloqueantes.
- [ ] Suposiciones/restricciones visibles; no hay diseño innecesario.
- [ ] SPEC aprobada por humano y decisión durable registrada.

# 17. Estado de aprobación

**Estado actual:** DRAFT

Estados: `DRAFT → IN_REVIEW → APPROVED → SUPERSEDED`.

## Aprobación

Solo decisión humana explícita permite `APPROVED`.

**Aprobado por:** [PENDIENTE]
**Fecha de aprobación:** [PENDIENTE]
**Decisión explícita y alcance:** [PENDIENTE; contenido de la decisión humana.]
**Registro durable:** `specs/<feature-id>/decisions.json` con huella, según `docs/state-reconstruction.md`, antes de PLAN.
