# Estándar de Arquitectura

**Versión:** 1.0.0
**Estado:** Activo

## Propósito

Mantener una arquitectura comprensible, modular, mantenible y trazable a la SPEC.

# 1. La arquitectura debe derivarse de la especificación

Justificar tecnologías, servicios, patrones e infraestructura por requisitos funcionales o no funcionales, restricciones, seguridad, rendimiento, escalabilidad, mantenimiento u operación. Una preferencia tecnológica sola no basta.

# 2. Separación de responsabilidades

Dar a cada componente una responsabilidad clara. Evitar mezclar sin necesidad presentación, negocio, datos, integraciones, infraestructura y configuración. Documentar la separación elegida en PLAN.

# 3. Dependencias explícitas

Mostrar dependencias entre componentes. Evitar ciclos, acoplamiento innecesario, accesos indirectos no documentados y estado global difícil de probar o sustituir. Abstraer dependencias externas cuando aporte valor.

# 4. Límites del sistema

Identificar en PLAN, cuando apliquen, componentes internos, actores, sistemas externos, BD, APIs, servicios, procesos asíncronos, almacenamiento y límites de confianza. Documentar las interacciones importantes.

# 5. Modelado de dominio

Reflejar conceptos del dominio cuando mejore la comprensión. Usar terminología consistente con SPEC en código, modelos, APIs, eventos y documentación.

# 6. Contratos explícitos

Definir contratos claros y validables cuando sea razonable: tipos, schemas, DTO, interfaces, eventos, HTTP, mensajes o estructuras de datos según el proyecto.

# 7. Gestión de datos

Documentar persistencia relevante: modelo, relaciones, restricciones, índices, migraciones, transacciones, consistencia, retención y eliminación. Identificar cambios destructivos explícitamente.

# 8. Integraciones externas

Documentar propósito, sistema externo, datos enviados y recibidos, autenticación aplicable, errores e indisponibilidad. Evitar que la lógica principal dependa sin necesidad de detalles del proveedor.

# 9. Manejo de errores

Manejar errores explícitamente. Distinguir, cuando aplique, validación, negocio, infraestructura, integraciones y fallos inesperados. Nunca ignorarlos silenciosamente.

# 10. Observabilidad

Considerar logs, métricas, trazas, auditoría y health checks según el proyecto. No exponer datos sensibles innecesarios.

# 11. Configuración

Separar del código, cuando sea posible, valores por entorno como credenciales, URLs, puertos y feature flags. Nunca almacenar secretos directamente en código fuente.

# 12. Simplicidad

Elegir la arquitectura más simple que satisfaga requisitos y restricciones actuales. Justificar cada complejidad; no crear capas o servicios para escenarios hipotéticos.

# 13. Decisiones arquitectónicas importantes

Documentar decisiones de impacto significativo, cuando corresponda, mediante ADR en `docs/decisions/` con ID `ADR-[XXX]`.

# 14. Cambios arquitectónicos

Ante un cambio a una decisión de PLAN: detener trabajo afectado, identificar causa e impacto downstream, actualizar PLAN y ADR si aplica, ajustar TASKS afectadas, recuperar aprobaciones, comprobar gates y solo entonces continuar. Seguir el Artículo VIII de la Constitución; no cambiar arquitectura significativamente en silencio.

# Checklist arquitectónico

Antes de aprobar PLAN, verificar trazabilidad de la arquitectura, responsabilidades, dependencias, límites, contratos, datos, integraciones, errores, observabilidad, secretos, simplicidad y decisiones documentadas.
