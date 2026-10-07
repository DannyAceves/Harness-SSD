# Estándar de Pruebas

**Versión:** 1.0.0
**Estado:** Activo

## Propósito

Las pruebas aportan evidencia verificable de requisitos y criterios de aceptación (AC), además de detectar errores.

# 1. Las pruebas derivan de requisitos

Relacionar cada prueba con comportamiento, requisito, AC o riesgo identificado: requisito → AC → implementación → prueba → evidencia. No crear pruebas solo para subir cobertura.

# 2. Trazabilidad

Relacionar requisitos críticos con una o más pruebas identificables (`TEST-[XXX]`) y sus AC. Debe poder recuperarse la cadena de evidencia.

# 3. Tipos de pruebas

Elegir niveles según PLAN; no todos son obligatorios para cada proyecto.

## Unitarias

Verifican unidades pequeñas aisladas, como reglas, servicios, validadores o transformaciones.

## Integración

Verifican interacción entre componentes, por ejemplo API, servicio, repositorio o BD.

## End-to-End

Verifican un flujo completo desde la perspectiva de usuario o consumidor.

## Contract Tests

Verifican contratos entre componentes o sistemas cuando existan y sea útil.

# 4. Casos positivos y negativos

Derivar de SPEC casos válidos, entradas inválidas, límites, errores, permisos y estados prohibidos cuando correspondan. Una ruta feliz sola no demuestra escenarios exigidos.

# 5. Pruebas deterministas

Controlar tiempo, aleatoriedad, orden, estado global y servicios o datos externos cambiantes para obtener resultados reproducibles.

# 6. Independencia

Evitar depender de otra prueba; preparar el estado requerido y limpiar efectos cuando proceda.

# 7. Datos de prueba

Usar datos explícitos, mínimos y reproducibles. Evitar datos personales y secretos reales salvo necesidad estricta. Si una prueba autorizada necesita secretos, suministrarlos por mecanismos seguros del entorno; nunca guardarlos en pruebas, fixtures, archivos versionados, resultados, logs o documentación. Aplicar el standard de seguridad.

# 8. Pruebas de regresión

Para un defecto reproducible y automatizable, crear o ajustar primero la prueba que falle por ese defecto, según §21; corregirlo, obtener PASS y ejecutar regresión relevante.

# 9. Las pruebas no se modifican para ocultar errores

Si una prueba correcta falla, tratar implementación como incorrecta hasta demostrar lo contrario. No eliminar, saltar, debilitar aserciones ni cambiar expectativas para aceptar código erróneo. Documentar y resolver explícitamente si la prueba contradice SPEC.

# 10. Prohibido ignorar pruebas fallidas

No cerrar una TASK con pruebas relevantes en FAIL. Clasificar causa: implementación, prueba, infraestructura, discrepancia con SPEC o comportamiento pendiente; resolver o registrar bloqueo.

# 11. Tests skipped

`skip`, `disabled`, `pending` y `todo` no son evidencia de PASS. Un requisito con prueba necesaria deshabilitada no está completamente validado.

# 12. Mocks y test doubles

Mocks, stubs y fakes pueden aislar límites externos y acelerar pruebas; no deben sustituir el comportamiento relevante por una simulación irrelevante.

# 13. Pruebas de integración reales

Si un requisito depende de tecnología o integración específica, considerar pruebas con implementación suficientemente representativa. Un mock en PASS no demuestra funcionamiento real.

# 14. Cobertura

La cobertura de código es auxiliar, no prueba de calidad. Priorizar requisitos cumplidos, pruebas útiles y luego porcentaje. Definir umbrales según el proyecto si se necesitan.

# 15. Nombres de pruebas

Nombrar el comportamiento esperado; evitar `test1`, `works` y similares.

# 16. Evidencia de validación

Registrar prueba, requisito/AC, comando, resultado y fecha cuando sea relevante para permitir la validación posterior.

# 17. Matriz de trazabilidad

Cuando la complejidad lo justifique, mapear requisito → AC → TASK → TEST → estado para detectar requisitos sin evidencia.

# 18. Estado de una prueba

Usar `PASS`, `FAIL`, `BLOCKED`, `NOT_RUN` y, cuando aplique, `NOT_APPLICABLE`. Un estado desconocido nunca equivale a PASS.

# 19. Validación manual

Documentar qué se verificó, cómo, resultado y AC para criterios manuales (por ejemplo visuales, accesibilidad, dispositivos o procesos humanos). No sustituir pruebas automatizables sin razón válida.

# 20. Finalización

Una feature no está completamente validada con requisitos obligatorios sin evidencia suficiente. Compilar, iniciar o pasar algunas pruebas no demuestra conformidad con SPEC.

# 21. Test-Driven Development

TDD es obligatorio prospectivamente para comportamiento nuevo automatizable, incluidos defectos reproducibles. PLAN y TASKS preparan casos trazados; solo `/implement`, tras aprobar SPEC, PLAN y TASKS, modifica pruebas.

1. **RED:** escribir o ajustar el caso y ejecutarlo antes de cambiar código productivo. Debe fallar por el comportamiento faltante o incorrecto de la tarea.
2. **GREEN:** aplicar el cambio mínimo y ejecutar el caso y pruebas relevantes hasta PASS.
3. **REFACTOR:** mejorar solo cuando sea útil, conservando PASS; no se exige refactor sin motivo.

Por TASK registrar TEST y requisito/AC, comando y causa del RED, comando y resultado GREEN, y resultado posterior al refactor si lo hubo. Guardar detalle en `specs/<feature-id>/evidence/` y enlazarlo desde TASKS y validación. Una prueba ya verde exige revisar el caso; no fabricar RED. Fallas de sintaxis, configuración, dependencias o infraestructura no son RED válido.

Documentación, validación exclusivamente manual y refactor sin conducta nueva requieren motivo y verificación alternativa. Preferir omitir TDD no es excepción. Si el caso es automatizable pero el entorno impide ejecutarlo, la TASK queda `BLOCKED` hasta resolverlo, sin declarar PASS. `/validate` comprueba RED/GREEN o justificación y alternativa. No reescribir evidencia histórica ni inventar ciclos TDD retrospectivos.

# Checklist de pruebas

Antes de validar, confirmar: requisitos críticos y AC cubiertos; casos positivos/negativos pertinentes; pruebas reproducibles e independientes; ninguna requerida deshabilitada o fallida; integraciones y regresiones comprobadas; evidencia TDD válida o bloqueo; y validación manual motivada cuando aplique.
