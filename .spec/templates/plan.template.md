# Plan Técnico: [Nombre de la funcionalidad]

**ID:** PLAN-[XXX]
**SPEC relacionada:** SPEC-[XXX]
**Estado:** DRAFT
**Versión:** 0.1.0
**Fecha:** [YYYY-MM-DD]

# 1. Precondiciones

- [ ] SPEC existe, está `APPROVED`, sin aclaraciones bloqueantes y con MUST→AC.
- [ ] Alcance y restricciones conocidos; checker de estado en PASS.

Si falla una precondición: `PLANNING STATUS: BLOCKED` (resultado operativo, no estado de PLAN).

# 2. Resumen técnico

## 2.1 Objetivo

[Qué se construirá técnicamente.]

## 2.2 Enfoque

[Estrategia mínima y reutilización existente.]

# 3. Requisitos cubiertos

| Requisito | Tipo | Cobertura en el plan |
|-----------|------|----------------------|
| FR-001 | Funcional | [Estrategia] |
| NFR-001 | No funcional | [Estrategia] |
| SEC-001 | Seguridad | [Control] |

Todo MUST debe tener cobertura.

# 4. Contexto técnico existente

## Stack actual

[Lenguaje, runtime, framework, BD, paquete y testing relevantes o «No aplica».]

## Componentes existentes relacionados

[Componentes reutilizables.]

## Restricciones técnicas existentes

[Restricciones verificadas, sin inventar tecnología.]

# 5. Decisiones técnicas

## DEC-001 — [Nombre de la decisión]

**Decisión:** [Elección.]
**Justificación:** [Relación con requisitos.]
**Requisitos relacionados:** [FR/NFR/SEC/AC.]
**Alternativas consideradas:** [Opciones reales.]
**Consecuencias:** [Efectos y trade-offs.]
**Requiere ADR:** [YES | NO]

# 6. Arquitectura propuesta

## 6.1 Componentes involucrados

| Componente | Responsabilidad | Cambio |
|------------|-----------------|--------|
| [Nombre] | [Responsabilidad] | CREATE / MODIFY / REUSE / REMOVE |

## 6.2 Flujo principal

[Secuencia técnica principal.]

## 6.3 Dependencias entre componentes

[Dependencias y límites; sin ciclos injustificados.]

# 7. Modelo de datos

Si no hay persistencia, indicar «No aplica».

## 7.1 Entidades afectadas

### [Entidad]

[Campos y reglas justificados.]

## 7.2 Relaciones

[Relaciones afectadas.]

## 7.3 Restricciones

[Constraints, índices e integridad.]

## 7.4 Migraciones

**¿Requiere migración?:** [YES | NO]
[Compatibilidad, rollback y marca `DESTRUCTIVE CHANGE: YES` si corresponde.]

# 8. Interfaces y contratos

## API / Endpoint

### [METHOD] /[path]

**Propósito:** [Conducta.]
**Requisito relacionado:** [FR/AC.]

### Entrada

[Datos y validación.]

### Salida exitosa

[Contrato.]

### Errores esperados

[Casos y respuesta.]

Si no hay API, describir contrato afectado o «No aplica».

# 9. Validación de entradas

[Fuentes no confiables, reglas y límite de validación.]

# 10. Seguridad

## Requisitos relacionados

[SEC/AC o «No aplica» justificado.]

## Autenticación

[Identidad y mecanismo.]

## Autorización

[Permisos y límite confiable.]

## Datos sensibles

[Datos y protección.]

## Secretos

[Mecanismo seguro; no insertar valores reales.]

## Riesgos relevantes

[Riesgo → control y evidencia.]

# 11. Estrategia de pruebas

[Tipos de prueba relevantes según AC y riesgo.]

## Unitarias

[Casos o N/A.]

## Integración

[Casos o N/A.]

## End-to-End

[Casos o N/A.]

## Seguridad

[Casos o N/A.]

## 11.1 Mapeo inicial

| Criterio | Tipo de prueba previsto |
|----------|-------------------------|
| AC-001 | [Tipo/comando] |

## 11.2 Estrategia TDD

| Criterio | Automatizable | Caso y comando/nivel | RED viable antes de cambio | Motivo y alternativa si no aplica |
|----------|---------------|----------------------|----------------------------|----------------------------------|
| AC-001 | YES/NO | [Caso/comando] | [YES/NO] | [Motivo/alternativa] |

Preparar casos no autoriza modificar pruebas antes de `/implement`.

# 12. Observabilidad

## Logs

[Eventos sin secretos o N/A.]

## Métricas

[Señales o N/A.]

## Auditoría

[Eventos o N/A.]

## Health checks

[Comprobaciones o N/A.]

# 13. Impacto en el repositorio

## Archivos o módulos a crear

[Rutas o ninguno.]

## Archivos o módulos a modificar

[Rutas o ninguno.]

## Elementos a reutilizar

[Rutas.]

## Elementos a eliminar

[Rutas o ninguno; señalar destrucción.]

# 14. Dependencias

## Nuevas dependencias

| Dependencia | Propósito | Justificación/seguridad |
|-------------|-----------|------------------------|
| [Nombre o ninguna] | [Uso] | [Motivo] |

# 15. Configuración

[Variables, propósito y marca de secreto; nunca guardar valor sensible.]

# 16. Migración y compatibilidad

[Compatibilidad de API, esquema, formato, datos y configuración.]

## Breaking changes

**¿Existen?:** [YES | NO]
[Impacto y estrategia si YES.]

# 17. Manejo de errores

[Error esperado → tratamiento, sin exposición sensible.]

# 18. Riesgos técnicos

## RISK-001 — [Nombre]

**Descripción:** [Riesgo.]
**Impacto:** [LOW | MEDIUM | HIGH]
**Probabilidad:** [LOW | MEDIUM | HIGH]
**Mitigación:** [Acción.]

# 19. Aclaraciones técnicas

## Q-TECH-001 — [Pregunta]

**Estado:** [NEEDS CLARIFICATION]
**Pregunta:** [Decisión técnica faltante.]
**Impacto:** [Parte afectada.]
**Bloqueante:** [YES | NO]
**Respuesta:** [PENDIENTE]

# 20. ADR requeridos

| ADR | Decisión | Estado |
|-----|----------|--------|
| ADR-[XXX] o ninguno | [Decisión] | PENDING |

# 21. Orden de implementación

[Dependencias entre bloques para generar TASKS; no tareas detalladas.]

# 22. Criterios para avanzar a Tasks

- [ ] SPEC aprobada; MUST cubiertos; diseño, archivos, datos/contratos aplicables definidos.
- [ ] Seguridad, pruebas/TDD, dependencias, compatibilidad, riesgos y ADR revisados.
- [ ] Sin aclaraciones técnicas bloqueantes; aprobación humana de PLAN registrada.

# 23. Estado del plan

**Estado actual:** DRAFT

Estados: `DRAFT → IN_REVIEW → APPROVED → SUPERSEDED`.

## Aprobación

Solo aprobación humana explícita permite `APPROVED`.

**Aprobado por:** [PENDIENTE]
**Fecha de aprobación:** [PENDIENTE]
**Decisión explícita y alcance:** [PENDIENTE; contenido de la decisión humana.]
**Registro durable:** `specs/<feature-id>/decisions.json` con huella antes de TASKS.
