# Comando: Plan

## Propósito

Convertir SPEC aprobada en diseño técnico implementable y trazable (`plan.md`); no crear código ni TASKS.

# 1. Entrada

`/plan SPEC-[XXX]` o ruta de `spec.md`. Si SPEC no está `APPROVED`, `PLANNING STATUS: BLOCKED`; no generar PLAN.

# 2. Contexto obligatorio

Leer Constitución, cuatro standards, template de PLAN, SPEC, documentación técnica, ADR y código relacionado. Basarse en el estado real del repo.

# 3. Inspección del repositorio

Identificar stack, módulos, datos, interfaces, autenticación/autorización, tests, configuración, observabilidad, CI e infraestructura relevantes. Integrar con patrones existentes.

## Regla de reutilización

Antes de crear servicio, repository, módulo, helper, middleware, abstracción o dependencia, buscar equivalente existente; reutilizarlo cuando sea coherente y sin acoplamiento indebido.

# 4. Contexto técnico detectado

Registrar solo tecnologías, componentes y restricciones comprobados; no inventar runtime, framework, BD o infraestructura.

# 5. Mapa de requisitos

Mapear cada FR/NFR/SEC MUST y AC que necesita implementación a una estrategia técnica. Ningún MUST queda sin cobertura.

# 6. Diseño de la solución

Elegir solución mínima, simple, segura y comprobable que satisfaga SPEC; justificar infraestructura, capas y complejidad actuales, sin anticipación especulativa.

# 7. Decisiones técnicas

Registrar `DEC-[XXX]` con decisión, justificación, requisitos/AC, alternativas, consecuencias y necesidad de ADR.

# 8. Evaluación de ADR

Considerar ADR para cambios arquitectónicos, tecnología importante, límites, persistencia o trade-offs de impacto significativo. Registrar `ADR-[XXX]` y ruta `docs/decisions/ADR-[XXX]-<slug>.md`; documentarlo antes de implementar cuando sea necesario. No crear ADR para detalles locales menores.

# 9. Diseño de datos

Si hay persistencia, analizar entidades, relaciones, campos, constraints, índices, integridad, migraciones y compatibilidad; derivar cada cambio de SPEC.

## Cambios destructivos

Marcar `DESTRUCTIVE CHANGE: YES` para eliminación o alteración incompatible de datos/esquema y definir migración, rollback o mitigación antes de ejecutar.

# 10. Diseño de contratos

Definir solo endpoints, eventos, interfaces, schemas e integraciones necesarios, cada uno trazado a requisitos y con entradas, salidas y errores relevantes.

# 11. Diseño de seguridad

Evaluar identidad, permisos, entradas, datos sensibles, secretos, auditoría y destrucción. Mapear controles a SEC aplicables según `.spec/standards/security.md`.

# 12. Estrategia de pruebas

Dar a cada AC una verificación y nivel de prueba. Para comportamiento automatizable, indicar caso, herramienta/comando, viabilidad de RED antes del cambio y evidencia GREEN; si TDD no aplica, motivo y alternativa según testing §21. TEST concretos pueden asignarse en TASKS. PLAN no autoriza editar pruebas.

# 13. Análisis de impacto

Clasificar archivos/componentes `CREATE`, `MODIFY`, `REUSE`, `REMOVE`. TASKS puede ajustar detalle menor; cambio estructural vuelve a PLAN.

# 14. Nuevas dependencias

Justificar necesidad, alternativas existentes, mantenimiento, compatibilidad y seguridad de cada dependencia; no instalarla durante PLAN.

# 15. Aclaraciones técnicas

Usar `Q-TECH-[XXX] [NEEDS CLARIFICATION]` con pregunta, impacto y `Bloqueante: YES | NO` si SPEC/Constitución/standards/arquitectura/ADR no resuelven diseño. Una pregunta funcional regresa a SPEC, no se esconde en PLAN.

# 16. Deficiencias descubiertas en la SPEC

Ante ambigüedad, contradicción, conducta faltante o riesgo funcional que impide diseñar: `PLANNING STATUS: BLOCKED`, `SPEC REVISION REQUIRED`; indicar requisito, problema y aclaración. No corregir SPEC en silencio.

# 17. Análisis de riesgos

Registrar riesgos técnicos relevantes `RISK-[XXX]` con descripción, impacto, probabilidad (`LOW|MEDIUM|HIGH`) y mitigación; no inventar riesgos triviales para llenar campos.

# 18. Self-check

Verificar SPEC aprobada, repo y reutilización inspeccionados, MUST cubiertos, decisiones justificadas, datos/contratos/seguridad cuando apliquen, AC con pruebas y TDD, impacto, dependencias, destrucción, riesgos, ADR y cero preguntas bloqueantes.

# 19. Creación del artefacto

Crear `specs/<feature-id>/plan.md` desde `.spec/templates/plan.template.md`; no modificar la template.

# 20. Estado resultante

Bloqueo técnico: PLAN `DRAFT`, `RESULT: NEEDS CLARIFICATION`; defecto funcional: `PLANNING STATUS: BLOCKED`, `SPEC REVISION REQUIRED`; PLAN completo pendiente de humano: `IN_REVIEW`, `READY FOR REVIEW`. `BLOCKED` es resultado, no estado de PLAN. Solo humano aprueba; registrar alcance y huella en `decisions.json` y exigir checker PASS antes de TASKS. En PLAN solo se modifican PLAN, ledger y proyecciones de estado/enlaces en handoff/índice.

# 21. Salida

Informar SPEC/PLAN y ruta, MUST cubiertos, decisiones y ADR, impacto CREATE/MODIFY/REUSE/REMOVE, Q-TECH, riesgos, estado y siguiente acción.

# 22. Acciones prohibidas

No implementar, instalar, migrar, generar TASKS, cambiar SPEC en silencio, crear arquitectura injustificada o autoaprobar PLAN.
