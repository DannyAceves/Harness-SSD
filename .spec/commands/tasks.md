# Comando: Tasks

## Propósito

Descomponer un PLAN aprobado en tareas pequeñas, trazables y verificables (`tasks.md`), sin implementar.

# 1. Entrada

`/tasks PLAN-[XXX]` o ruta de PLAN. SPEC y PLAN deben estar `APPROVED`; de otro modo `TASK GENERATION STATUS: BLOCKED` y no se generan tareas.

# 2. Contexto obligatorio

Leer Constitución, cuatro standards, template de TASKS, SPEC, PLAN, ADR y código relacionado necesario. Derivar tareas de PLAN sin añadir arquitectura nueva.

# 3. Análisis del PLAN

Identificar MUST, AC, DEC, componentes, archivos, datos/migraciones, contratos, SEC, pruebas/TDD, configuración, dependencias, ADR, riesgos y orden.

# 4. Tamaño de tarea

Cada TASK expresa un objetivo, alcance y evidencia cohesivos. Dividir trabajo con objetivos independientes o difícil de validar; evitar fragmentación trivial.

# 5. Identificadores

Usar `TASK-[XXX]` únicos; no reutilizarlos ni renumerarlos tras referenciarlos. `CANCELLED` es anotación histórica, no estado activo: conservar ID/evidencia, registrar motivo y revisión, recuperar gates si cambia trabajo autorizado; nunca omitir trabajo requerido por SPEC/PLAN.

# 6. Tipos de tarea

Clasificar cuando ayude: FEATURE, TECHNICAL, TEST, MIGRATION, SECURITY, CONFIGURATION, DOCUMENTATION o REFACTOR. El tipo no sustituye trazabilidad.

## FEATURE

Implementa conducta requerida por SPEC.

## TECHNICAL

Prepara infraestructura necesaria y justificada en PLAN.

## TEST

Aporta evidencia automatizada o verificaciones previstas.

## MIGRATION

Cambia estructuras o datos persistentes.

## SECURITY

Implementa control de seguridad.

## CONFIGURATION

Cambia configuración requerida.

## DOCUMENTATION

Actualiza documentación necesaria.

## REFACTOR

Cambia estructura interna conservando comportamiento observable.

# 7. Trazabilidad

Cada TASK cita fuente autorizada (`FR`, `NFR`, `SEC`, `AC`, `DEC`, `ADR`) y al menos un requisito o AC real que soporta directa o explícitamente vía PLAN. Una relación solo con otra TASK o DEC no basta. No inventar FR para justificar detalle técnico. Eliminar o justificar tareas huérfanas.

# 8. Dependencias

Declarar `Depende de: TASK-[XXX]` o ninguna. No iniciar antes de que dependencias obligatorias estén listas ni admitir ciclos; un ciclo da `DEPENDENCY CYCLE DETECTED` y bloquea generación.

# 9. Paralelización

Se pueden proponer tareas paralelas sin dependencia, archivo conflictivo ni decisión compartida pendiente; no es obligación. Prima corrección y evidencia.

# 10. Alcance de archivos

Indicar `CREATE|MODIFY|REUSE|REMOVE` cuando sea posible. Un archivo extra menor exige necesidad, coherencia con PLAN y motivo documentado; cambio estructural requiere revisión de PLAN.

# 11. Conflictos potenciales

Marcar `FILE CONFLICT` si tareas paralelas modifican el mismo archivo; secuenciarlas o redefinir alcance.

# 12. Pruebas

Cubrir cada AC con TEST o evidencia prevista. Integrar casos dentro de una TASK o crear TASK de pruebas según cohesión. Para conducta automatizable, identificar TEST, FR/AC y DoD de RED válido antes del cambio productivo y GREEN después. Para trabajo fuera de TDD, registrar motivo y alternativa; entorno que bloquea test automatizable deja TASK `BLOCKED`.

# 13. Definition of Done

Cada TASK exige objetivo y requisitos satisfechos, implementación/pruebas relevantes completas y en PASS, standards/alcance respetados y evidencia. Código escrito solo no basta.

# 14. Aclaraciones durante generación de tareas

Ambigüedad funcional → `SPEC REVISION REQUIRED`; diseño → `PLAN REVISION REQUIRED`; solo descomposición → `Q-TASK-[XXX] [NEEDS CLARIFICATION]`. No resolver decisiones superiores en TASKS.

# 15. Coverage check

Mapear cada elemento implementable del PLAN y cada MUST/AC a tareas. `UNCOVERED PLAN ITEM` impide cerrar el documento.

# 16. Orphan check

Cada TASK debe llegar a SPEC o PLAN y a requisito/AC real; una dependencia con otra TASK no justifica por sí sola. Corregir o eliminar `ORPHAN TASK`.

# 17. Orden de ejecución

Dar orden legible que respete el grafo; el grafo TASK→TASK manda sobre fases orientativas.
Cada `## TASK-[XXX]` debe tener una línea independiente `**Estado:**
TODO|IN_PROGRESS|BLOCKED|DONE`. La tabla de orden lista cada TASK una sola
vez y repite ese estado; es una vista, no la fuente operativa. TASKS
`COMPLETED` exige todas las fichas `DONE`. Campos combinados, estados
ausentes o discrepancias impiden cerrar la feature.

# 18. Creación del artefacto

Crear `specs/<feature-id>/tasks.md` desde `.spec/templates/tasks.template.md`, sin modificar la template.

# 19. Self-check

Verificar SPEC/PLAN aprobados; objetivos, trazabilidad, cobertura MUST/AC/PLAN, dependencias sin ciclos, archivos y conflictos, pruebas/TDD, DoD, tamaño razonable, sin arquitectura nueva ni dudas bloqueantes.

# 20. Estado resultante

Defecto funcional → `TASK GENERATION STATUS: BLOCKED`, `SPEC REVISION REQUIRED`; técnico → `BLOCKED`, `PLAN REVISION REQUIRED`; duda bloqueante → TASKS `DRAFT`, `NEEDS CLARIFICATION`; completo → `IN_REVIEW`, `READY FOR REVIEW`. `BLOCKED` es resultado, no estado de TASKS. Solo aprobación humana lleva a `APPROVED`. Registrar alcance y huella en `decisions.json`, checker PASS antes de `/implement`. Estado/evidencia operativos no cambian trabajo autorizado; objetivos, dependencias, pruebas o alcance sí reabren gate. Durante `/tasks` solo editar TASKS, ledger y proyecciones de estado/enlaces.

# 21. Salida

Informar SPEC/PLAN/TASKS y ruta, cantidad por tipo, dependencias, paralelos/conflictos, cobertura FR/NFR/SEC/AC, huérfanas, dudas y siguiente gate.

# 22. Acciones prohibidas

No implementar, instalar, migrar, cambiar SPEC/PLAN en silencio, crear arquitectura o tareas sin fuente, ignorar dependencias/conflictos ni autoaprobar TASKS.
