# Comando: Implement

## Propósito

Ejecutar solo TASKS autorizadas por SPEC → PLAN → TASKS, con cambios mínimos y evidencia. Es la primera fase que puede modificar implementación.

# 1. Entrada

Una o varias TASK (`/implement TASK-[XXX]`) o todas las pendientes de una feature (`/implement SPEC-[XXX]`), respetando dependencias.

# 2. Precondiciones

SPEC y PLAN `APPROVED`; TASKS `APPROVED` o `IN_PROGRESS`; TASK objetivo `TODO` o `IN_PROGRESS`, dependencias satisfechas y sin aclaraciones/bloqueos independientes. Para features nuevas, `python3 src/check_harness_state.py` debe dar PASS con aprobaciones y huellas vigentes. SPEC-007 conserva su protocolo transitorio documentado. Si falla un gate: `IMPLEMENTATION STATUS: BLOCKED`, sin cambios.

# 3. Contexto obligatorio

Leer Constitución, cuatro standards, SPEC, PLAN, TASKS, ADR, código y pruebas relacionadas. Comprender estado real antes de editar.

# 4. Preflight

Comprobar lo siguiente antes de editar:

## Task

ID, objetivo, tipo, estado y prioridad.

## Traceability

Requisitos, AC, DEC y TEST requeridos.

## Dependencies

TASK obligatorias ya completadas.

## Scope

Archivos previstos y componentes reutilizables.

## Repository State

Archivos presentes y estructura coherente con PLAN, sin cambios inesperados.

## Blocking Conditions

Sin aclaraciones, conflictos ni revisiones superiores pendientes.

# 5. Inicio de tarea

## Estado del documento TASKS

Antes o junto con la primera TASK, cambiar TASKS `APPROVED → IN_PROGRESS`; no repetir la transición en tareas posteriores.

## Estado de la TASK

Cambiar TASK `TODO → IN_PROGRESS` antes de editar cuando el mecanismo lo permita.

# 6. Implementación

Hacer el cambio mínimo que cumpla TASK respetando SPEC, PLAN, TASKS, Constitución, standards, ADR y patrones existentes.

## Regla de mínimo cambio

Evitar funciones «por si acaso», refactors/cosmética ajenos, renombres y dependencias innecesarias.

# 7. Control de alcance

Verificar `CREATE|MODIFY|REUSE|REMOVE` antes de editar.

## Cambio menor no previsto

Archivo adicional solo si es necesario, no altera requisitos, arquitectura, contratos importantes ni dependencias, permanece en objetivo y se registra.

## Cambio estructural no previsto

Detener trabajo: `PLAN REVISION REQUIRED` o `SPEC REVISION REQUIRED`.

# 8. Pruebas durante implementación

Para conducta automatizable aplicar testing §21: RED con TEST aprobado ejecutado antes de código productivo y fallo por conducta faltante; GREEN con cambio mínimo y pruebas relevantes; REFACTOR solo si aporta valor, manteniendo PASS. Registrar TEST/FR/AC, comandos, causa y resultados. Una prueba previamente verde exige revisar caso; sintaxis, entorno, configuración o dependencias rotas no son RED. Entorno que impide prueba automatizable deja TASK `BLOCKED`. Para documentación, validación solo manual o refactor sin conducta nueva, registrar motivo y alternativa; no exceptuar TDD por preferencia.

# 9. Manejo de pruebas fallidas

Clasificar causa sin ocultar fallos.

## A --- Implementación incorrecta

Corregir código, no debilitar la prueba.

## B --- Test incorrecto

Si contradice SPEC, corregirlo y documentar motivo.

## C --- Problema en SPEC

Detener trabajo: `SPEC REVISION REQUIRED`.

## D --- Problema en PLAN

Detener trabajo: `PLAN REVISION REQUIRED`.

## E --- Problema externo

Registrar `BLOCK-[XXX]` y TASK `BLOCKED` si impide continuar.

# 10. Integridad de pruebas

No eliminar, saltar, debilitar aserciones correctas, usar mocks irrelevantes, capturar errores silenciosamente ni hardcodear solo para PASS. Una prueba vale si verifica la conducta requerida.

# 11. Quality checks

Ejecutar los controles relevantes disponibles: formatter, linter, tipos, unit/integration/contract/security tests y build según el cambio.

# 12. Regresión

Ejecutar pruebas existentes relevantes. Resolver una regresión causada por el cambio antes de `DONE`.

# 13. Security check

Para autenticación, autorización, datos, secretos, uploads, destrucción, integraciones, queries o entradas externas, revisar standard de seguridad y aportar evidencia para SEC.

# 14. Descubrimientos

Registrar mejora, bug o deuda fuera de TASK como `DISCOVERY-[XXX]`; no implementarla automáticamente.

# 15. Aclaraciones durante implementación

Registrar `BLOCK-[XXX] [NEEDS CLARIFICATION]` con TASK, pregunta, impacto y origen SPEC/PLAN/TASK/EXTERNAL; poner TASK `BLOCKED` cuando impide trabajar. No asumir una decisión de conducta.

# 16. Escalamiento

Detener trabajo afectado y asignar la decisión a su dueño:

## Problema funcional

Comportamiento, permisos o alcance → SPEC, `SPEC REVISION REQUIRED`.

## Problema arquitectónico o técnico

Arquitectura, contratos, datos o dependencia → PLAN, `PLAN REVISION REQUIRED`.

## Problema de descomposición

Tamaño, dependencias o conflicto de archivos → TASKS, `TASK REVISION REQUIRED`.

## Problema exclusivamente de implementación

Corregir dentro de la TASK autorizada.

# 17. Reanudación después de revisión

No reanudar automáticamente. Confirmar cambio del artefacto dueño, impacto downstream, actualización solo de afectados, nuevos approval gates para contenido autorizado modificado, TASKS ajustado si cambia trabajo, evidencia/pruebas invalidadas revisadas, precondiciones y preflight otra vez válidos. Cambios solo de estado/evidencia no requieren nueva aprobación.

# 17.1 Reapertura después de validación

Si `/validate` detecta defecto exclusivamente de implementación en trabajo cerrado:

1. Registrar `FINDING-[XXX]` o `SEC-FINDING-[XXX]` y TASK afectadas; verificar que corregirlo cabe en SPEC/PLAN/TASKS aprobados. Si no, volver al nivel dueño y gates de §16-17.
2. Conservar validación desfavorable y evidencia previa; identificar qué quedó invalidado.
3. Reabrir TASKS `COMPLETED → IN_PROGRESS` y TASK afectadas `DONE → TODO` con motivo/finding. Reabrir dependientes solo si su cierre o evidencia ya no vale.
4. Repetir precondiciones y preflight. El finding que motiva la corrección no la bloquea; otros bloqueos y dependencias pendientes sí.
5. Pasar TASK a `IN_PROGRESS`, corregir, repetir tests, calidad y regresión afectados; registrar nueva evidencia, cumplir DoD, cerrar TASKS y repetir `/validate`.

Reapertura y evidencia sin cambio de trabajo autorizado no exigen aprobación nueva. La feature sigue sin validar hasta un nuevo PASS final.

# 18. Evidencia de implementación

Guardar detalle por TASK en `specs/<feature-id>/evidence/`.

## Files

Archivos creados, modificados y eliminados.

## Tests

TEST, comando y resultado `PASS|FAIL|BLOCKED`.

## TDD

RED/GREEN y causa; si no aplica, motivo y alternativa.

## Quality checks

Resultados de lint, tipos, build y otros controles aplicables.

## Requirements

FR, NFR y SEC cubiertos.

## Acceptance Criteria

AC con evidencia y resultado.

## Discoveries

`DISCOVERY-[XXX]` fuera de alcance.

## Deviations

Cambios menores respecto al alcance previsto y justificación.

# 19. Definition of Done de TASK

`DONE` requiere objetivo, SPEC/PLAN/alcance cumplidos, AC con evidencia, TEST y regresión/calidad relevantes en PASS, RED/GREEN válido o excepción documentada, SEC cubiertos, ningún bloqueo y evidencia registrada.

# 20. Ejecución de múltiples tareas

Respetar dependencias; una TASK dependiente no comienza mientras su requisito esté `TODO`, `IN_PROGRESS` o `BLOCKED`.

# 21. Paralelización

Solo si no hay dependencia, conflicto de archivos ni decisión compartida y hay aislamiento seguro. Mantener trazabilidad y evidencia; ejecución secuencial siempre es válida.

# 22. Control de versiones

Mantener cambios pequeños y revisables, relacionados con TASK cuando sea útil. No hacer commits automáticamente sin autorización del usuario o del entorno.

# 23. Finalización de implementación

Con todas las TASK requeridas `DONE`, sin pendientes/bloqueos, MUST y AC cubiertos y evidencia/DoD completos, pasar TASKS `IN_PROGRESS → COMPLETED` y reportar `IMPLEMENTATION STATUS: COMPLETED`. Siguiente paso: `/validate`; implementación completa no implica `SPEC COMPLIANCE: PASS`.

# 24. Self-check

Verificar tareas autorizadas y orden, alcance, pruebas/TDD, regresión, calidad, SEC, discoveries/bloqueos y evidencia por TASK; ningún cambio funcional o arquitectónico silencioso.

# 25. Salida

Informar SPEC/PLAN/TASKS, TASK `DONE/BLOCKED`, progreso, archivos, TEST, calidad, discoveries, bloqueos, estado y siguiente acción.

# 26. Acciones prohibidas

No inventar requisitos, cambiar SPEC/PLAN/TASKS o arquitectura sin gate, añadir dependencias importantes no aprobadas, hacer refactors ajenos, debilitar pruebas, ignorar fallos/regresiones/seguridad, decidir ambigüedades, cerrar TASK sin evidencia ni declarar la feature validada.
