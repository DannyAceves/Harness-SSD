# Estándar de Código

**Versión:** 1.0.0
**Estado:** Activo

## Propósito

Producir código comprensible, mantenible, verificable y trazable.

# 1. El código implementa trabajo trazable

Toda modificación requiere TASK autorizada y relación con requisitos o AC; una necesidad técnica debe enlazar PLAN y los requisitos que soporta. No inventar un FR para justificar detalles técnicos ni agregar funciones no solicitadas. Procesar nueva funcionalidad por el cambio SDD de la Constitución.

# 2. Alcance mínimo

Limitar el cambio a la TASK. Registrar por separado refactors, cosmética extensa, funcionalidades, arquitectura o dependencias fuera de alcance.

# 3. Código simple y comprensible

Favorecer código explícito, legible, predecible, comprobable y modificable. Justificar abstracciones y complejidad por requisitos o necesidad técnica documentada.

# 4. Responsabilidad única

Dar a funciones, clases, módulos y componentes una responsabilidad clara. Evaluar división si crecen o mezclan responsabilidades sin justificación.

# 5. Nombres descriptivos

Nombrar por intención y concepto del dominio; evitar nombres vagos como `data`, `temp`, `manager` o `helper` si existe uno específico.

# 6. Funciones pequeñas y enfocadas

Dividir una función con múltiples responsabilidades, demasiadas ramas o difícil de comprender o probar. No hay límite fijo de líneas; prima la claridad.

# 7. Evitar duplicación significativa

Reducir reglas de negocio duplicadas cuando convenga. La similitud visual sola no justifica una abstracción: comprobar que sea el mismo concepto.

# 8. Manejo explícito de errores

Manejar errores esperados sin ignorarlos, convertirlos en éxito ni ocultar información diagnóstica relevante. Dar contexto suficiente sin exponer detalles internos innecesarios al usuario.

# 9. Validación en límites del sistema

Tratar HTTP, formularios, archivos, variables de entorno, APIs externas, eventos, mensajes y entradas de usuario como no confiables. Validar cerca del límite de entrada.

# 10. Tipos y contratos

Usar tipos cuando el lenguaje lo permita; no evadirlos sin justificación. Expresar entradas, salidas, estados válidos y errores esperados de contratos importantes.

# 11. Estado mutable

Localizar y controlar el estado mutable. Evitar globales mutables y efectos secundarios innecesarios; hacer visibles los cambios importantes.

# 12. Comentarios

Explicar motivos, restricciones no evidentes, comportamientos inesperados y decisiones temporales; no narrar literalmente código claro.

# 13. Código muerto

Eliminar código comentado, inalcanzable, obsoleto, duplicado sin uso o creado «por si acaso». Recuperar versiones anteriores desde Git cuando se necesiten.

# 14. Dependencias

Justificar cada dependencia nueva; evaluar alternativa existente, mantenimiento, impacto, seguridad y compatibilidad. No añadir librerías para operaciones triviales.

# 15. Configuración y secretos

Usar configuración adecuada al stack para valores por entorno. Nunca insertar passwords, keys, tokens, claves privadas ni credenciales directamente en código.

# 16. Cambios de base de datos

Usar migraciones o scripts versionados reproducibles cuando la tecnología lo permita. Identificar cambios destructivos antes de ejecutarlos.

# 17. Compatibilidad

Identificar roturas de APIs, schemas, eventos, formatos, interfaces públicas o modelos persistidos antes de implementar; definir migración cuando aplique.

# 18. Formato automático

Configurar y ejecutar de forma consistente formatter, linter y análisis estático estándar cuando existan; definir reglas concretas en la configuración técnica.

# 19. Código generado por agentes

Tiene los mismos estándares que el manual. El agente no inventa requisitos, cambia alcance o contratos en silencio, ignora errores, desactiva pruebas o validaciones ni agrega dependencias injustificadas.

# 20. Prohibido adaptar pruebas para ocultar errores

Si una prueba correcta derivada de requisitos falla, corregir implementación. No eliminar ni debilitar la prueba para obtener PASS. Si contradice SPEC, identificar discrepancia, revisar SPEC, corregir prueba cuando proceda y documentar.

# 21. Refactoring

Preservar comportamiento observable salvo SPEC contraria. Separar refactors grandes cuando facilite revisión y ejecutar pruebas relevantes después.

# 22. TODO y deuda técnica

`TODO`, `FIXME` y `HACK` no sustituyen trabajo requerido. Añadir contexto a esos marcadores y registrar deuda relevante como trabajo pendiente.

# Checklist de implementación

Antes de cerrar una TASK: confirmar trazabilidad y alcance, responsabilidades y nombres claros, entradas y errores controlados, ausencia de secretos o código muerto, dependencias justificadas, contratos respetados y pruebas/controles de calidad relevantes en PASS.
