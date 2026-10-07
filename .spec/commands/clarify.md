# Comando: Clarify

## Propósito

Resolver ambigüedades de SPEC entre `/specify` y `/plan`, sin implementar ni generar PLAN.

# 1. Entradas

Una SPEC existente: `/clarify SPEC-[XXX]` o su ruta `spec.md`.

# 2. Contexto obligatorio

Leer Constitución, SPEC, template de especificación, documentos y SPEC aprobadas relacionados; consultar standards aplicables. Mantener precedencia.

# 3. Localización de aclaraciones existentes

Buscar `[NEEDS CLARIFICATION]`; anotar por `Q-[XXX]` pregunta, contexto, impacto, FR/AC afectados, carácter bloqueante y estado.

# 4. Segunda revisión de ambigüedad

Revisar actores, permisos, ownership, estados, transiciones, destrucción, errores, límites, negocio, datos, casos límite, contradicciones y AC. Crear `Q-[XXX] [NEEDS CLARIFICATION]` para dudas relevantes omitidas; no inventar respuesta.

# 5. Resolución mediante contexto existente

Antes de preguntar, buscar respuesta explícita en SPEC, Constitución, standards, requisitos/reglas, otras SPEC aprobadas, restricciones y decisiones humanas registradas. Solo reutilizar una decisión anterior si aplica al mismo comportamiento y alcance, sigue vigente y no contradice autoridad superior o posterior. Si hay duda razonable, preguntar. Si es explícita y válida, registrar origen, actualizar SPEC y marcar `[CLARIFIED]`; no inferir permiso nuevo.

### Condiciones para resolver mediante contexto existente

Respuesta explícita, aplicable, vigente y no contradictoria; las cuatro condiciones son necesarias.

# 6. Priorización de aclaraciones

Atender primero bloqueos de alcance, negocio, seguridad/permisos, comportamiento y datos; luego no bloqueantes y preferencias. Agrupar preguntas relacionadas sin redundancia.

# 7. Presentación de aclaraciones

Cada `Q-[XXX]` indica pregunta breve y neutral, contexto, impacto, `Bloqueante: YES | NO` y opciones conocidas cuando ayuden.

# 8. Opciones de respuesta

Mostrar alternativas reales sin inducir ni preseleccionar decisión funcional; dejar respuesta abierta cuando sea necesario. Decide la autoridad humana.

# 9. Aclaraciones derivadas

Una respuesta puede abrir otra pregunta; registrarla y continuar hasta resolver ambigüedades bloqueantes relevantes.

# 10. Registro de resolución

Registrar `[CLARIFIED]`, respuesta, quién decidió, fecha y FR/AC/BR/SEC afectados. Guardar resultado y alcance de decisiones humanas de requisitos o gates en `decisions.json`.

# 11. Propagación de la decisión

Incorporar la respuesta a requisitos y AC verificables afectados. Marcar Q como resuelta sin actualizar la SPEC no basta.

# 12. Análisis de impacto

Revisar otros requisitos, AC, negocio, seguridad, casos límite, alcance y suposiciones; corregir contradicciones en la SPEC.

# 13. Conversión de suposiciones

Convertir una suposición `ASM-[XXX]` que afecta significativamente conducta en `Q-[XXX] [NEEDS CLARIFICATION]`; no ocultar decisiones de negocio.

# 14. Contradicciones

Marcar `CONFLICT DETECTED`, identificar reglas opuestas y resolver antes de continuar. No alterar silenciosamente un requisito para ocultarlo.

# 15. Self-check

Confirmar preguntas existentes y nuevas, respuestas y su origen, propagación a FR/AC/BR/SEC, ausencia de contradicciones o respuestas inventadas y matriz consistente. Evitar diseño técnico innecesario.

# 16. Gate de salida

Bloqueo pendiente: `SPEC STATUS: DRAFT`, `RESULT: NEEDS CLARIFICATION`. Contradicción: `DRAFT`, `CONFLICT DETECTED`. Sin bloqueos: `IN_REVIEW`, `READY FOR REVIEW`; sigue revisión humana.

# 17. Aprobación

Solo aprobación humana explícita lleva SPEC a `APPROVED` y permite `/plan`. Si cambia contenido aprobado, evaluar downstream, recuperar gates afectados y comprobar huellas. Registrar decisión, resultado y alcance en SPEC y `decisions.json` según `docs/state-reconstruction.md`; chat solo no es registro durable. Durante `/clarify` solo se modifican SPEC, ledger y estado/enlaces de `handoff.md` y `docs/index.md`.

# 18. Salida

Informar SPEC, Q revisadas/resueltas/pendientes, bloqueantes, conflictos, FR/AC actualizados, estado y siguiente acción.

# 19. Acciones prohibidas

No implementar, generar PLAN/TASKS, instalar, migrar, cambiar arquitectura, seleccionar respuestas en silencio, convertir preferencias técnicas en requisitos, ignorar conflictos ni autoaprobar SPEC.
