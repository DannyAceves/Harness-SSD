# Estándar de Seguridad

**Versión:** 1.0.0
**Estado:** Activo

## Propósito

Integrar seguridad en SPEC, PLAN, implementación y validación, con controles proporcionales al riesgo.

# 1. Seguridad desde la especificación

Identificar requisitos de seguridad relevantes, explícitos y verificables: autenticación, autorización, datos, privacidad, auditoría, integridad, disponibilidad, sesiones, acceso o cumplimiento.

# 2. Entradas no confiables

Tratar como no confiable toda entrada fuera del límite de confianza: HTTP, formularios, archivos, parámetros, headers, cookies, eventos, mensajes, APIs, webhooks y cliente. Validar antes de operaciones sensibles.

# 3. Autenticación

Definir en PLAN el mecanismo para identificar usuarios o servicios. Preferir soluciones estándar seguras; no improvisar ni guardar credenciales en texto plano.

# 4. Autorización

Separar identidad de permisos. Verificar autorización de cada operación protegida en un límite confiable; ocultar controles en UI no basta.

# 5. Principio de mínimo privilegio

Dar a usuarios, servicios y componentes solo los permisos necesarios; evitar acceso global o administrativo innecesario.

# 6. Secretos

Nunca insertar secretos directamente en código, archivos versionados, pruebas, documentación, logs ni errores. Incluye passwords, keys, tokens, claves privadas y credenciales de BD. Una aplicación o prueba autorizada puede usarlos cuando sea necesario, suministrados por mecanismos seguros del entorno y sin exponerlos en resultados o evidencia.

# 7. Datos sensibles

Identificarlos y planificar acceso, almacenamiento, tránsito, logs, backups, retención y eliminación. No conservar información sensible innecesaria.

# 8. Protección de datos en tránsito

Proteger comunicaciones sobre redes no confiables con mecanismos adecuados a la arquitectura; documentar decisiones relevantes en PLAN.

# 9. Protección de datos almacenados

Evaluar protección adicional según sensibilidad, amenazas, ley, infraestructura e impacto.

# 10. Manejo seguro de errores

No revelar a consumidores stack traces, secretos, consultas, rutas, configuración ni datos sensibles innecesarios. Registrar diagnóstico necesario de forma segura.

# 11. Logging seguro

Evitar passwords, tokens, cookies, headers de autorización, documentos sensibles y datos personales innecesarios en logs. Enmascarar o anonimizar identificadores sensibles cuando proceda.

# 12. Dependencias

Antes de añadir una dependencia evaluar necesidad, mantenimiento, procedencia, vulnerabilidades, impacto y permisos. Mantenerla actualizada conforme al riesgo y necesidades del proyecto.

# 13. Configuración segura

Preferir valores seguros; revisar configuración sensible por entorno y evitar que ajustes de desarrollo lleguen accidentalmente a producción.

# 14. Operaciones destructivas

Controlar eliminación, sobrescritura, cierre de cuentas, revocación y migraciones destructivas. Si el riesgo lo exige, añadir confirmación, autorización o auditoría.

# 15. Integraciones externas

Tratarlas como límites de confianza: validar respuestas cuando proceda, manejar indisponibilidad y respuestas inesperadas, limitar permisos, proteger credenciales y verificar autenticidad si aplica.

# 16. Archivos

Para uploads evaluar tipo real, tamaño, nombre, extensión, contenido, almacenamiento, permisos y acceso posterior. Nombre o extensión del usuario no demuestran el tipo real.

# 17. Base de datos

Reducir inyección y modificaciones no autorizadas con consultas parametrizadas u ORM seguro, validación, restricciones y permisos mínimos cuando aplique.

# 18. Seguridad del cliente

La validación del cliente mejora UX pero no es límite de seguridad. Repetir reglas críticas y autorización en un entorno confiable.

# 19. Fallo seguro

Ante permiso o estado de seguridad incierto, favorecer la opción segura; un permiso desconocido deniega acceso.

# 20. Seguridad y agentes

Un agente no desactiva controles, inserta secretos reales, reduce validaciones sin justificación, concede permisos excesivos, quita autenticación para pasar pruebas ni ignora vulnerabilidades relevantes. Si implementar exige comprometer un control, detenerse y obtener decisión explícita.

# 21. Cambios sensibles

Identificar en PLAN y TASKS cambios de autenticación, autorización, criptografía, secretos, permisos, sesiones, datos sensibles u operaciones destructivas; pueden requerir validación adicional.

# 22. Seguridad verificable

Cada control relevante requiere evidencia enlazada a requisito, AC y prueba o validación (`SEC-[XXX] → AC-[XXX] → TEST-[XXX] → resultado`).

## Ejemplo ilustrativo

`SEC-001`: acceso privado exige autenticación; `AC-004`: sin credenciales se deniega; `TEST-004`: ejecuta ese caso y registra PASS. Es solo ilustrativo.

# 23. Revisión de seguridad

Antes de cerrar una feature con impacto de seguridad, revisar autenticación, autorización, entradas, exposición, secretos, errores, logs, dependencias y operaciones sensibles con profundidad proporcional al riesgo.

# 24. Hallazgos de seguridad

Documentar cada hallazgo como `OPEN`, `MITIGATED`, `ACCEPTED` o `NOT_APPLICABLE`. La ausencia de error funcional no lo resuelve. `MITIGATED` exige evidencia de que el riesgo o bloqueo quedó resuelto. `ACCEPTED` exige decisión explícita con responsable, justificación, alcance y efecto sobre bloqueos; no satisface por sí mismo SEC ni autoriza `PASS`. Una excepción superior o cambio de requisitos/alcance sigue la Constitución y sus gates. El estado del hallazgo solo nunca prueba cumplimiento.

# Checklist de seguridad

Antes de validar, comprobar entradas, autenticación y autorización en límites confiables, privilegio mínimo, ausencia de secretos, protección de datos y logs, errores seguros, controles destructivos, integraciones, dependencias, evidencia de controles y ausencia de hallazgos bloqueantes abiertos.
