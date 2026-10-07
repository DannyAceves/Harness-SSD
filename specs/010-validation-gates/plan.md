# Plan Técnico: Gates de validación y estados de tarea coherentes

**ID:** PLAN-010  
**SPEC relacionada:** SPEC-010 v0.1.0  
**Estado:** APPROVED  
**Versión:** 0.1.0  
**Fecha:** 2026-10-07

# 1. Precondiciones

- [x] SPEC-010 `APPROVED`, DECISION-001 vigente y sin aclaraciones bloqueantes.
- [x] `python3 src/check_harness_state.py`: PASS antes de planificar.

# 2. Resumen técnico

Extender el checker Python existente con lectura explícita de estados y
evidencia estructural, mantener una sola fuente operativa por TASK y probar
todo el ciclo en una adopción temporal. Reutilizar sus funciones de ledger,
huella y proyección, y la suite `unittest`; sin dependencias nuevas.

# 3. Requisitos cubiertos

| Requisito | Estrategia |
|-----------|------------|
| FR-001, BR-001 | Verificar gates finales antes de proyectar VALIDATED y emitir issues concretos. |
| FR-002 | Cotejar AC de SPEC, TASK de TASKS, resultados TEST y rutas de evidencia del reporte. |
| FR-003 | Leer estado por encabezado TASK; exigir correspondencia con cada fila de orden y estado global. |
| FR-004 | Corregir TASKS-009 tras su decisión humana de cambio y repetir su validación. |
| FR-005 | Fixture de adopción con transiciones y escenarios negativos. |
| NFR-001 | Preservar exención de aprobación legado, interpretar formatos históricos y comprobar el repo fuente. |
| NFR-002 | Orden estable de issues y diagnóstico con feature/ruta/ID. |
| SEC-001 | Fixtures sintéticas en directorios temporales, sin secretos reales. |

# 4. Contexto técnico existente

Python 3 estándar, `unittest`, Markdown y JSON; sin BD, API ni servicios.
`src/check_harness_state.py` ya verifica ledger, hashes y proyecciones, pero
`projected_state()` confía en dos marcas del reporte y `audit_repository()`
no comprueba cierre. `src/adopt_harness.py` copia checker, tests, templates y
commands a un destino limpio. `tests/test_check_harness_state.py` cubre
aprobaciones; `tests/test_adopt_harness.py` llega solo al gate de SPEC.
Reportes antiguos varían en tablas y metadatos, aunque todos contienen AC,
TASK y resultados recuperables. TASKS-009 tiene `TODO` en ficha y `DONE` en
tabla; su texto combinado no es metadata normalizada por `canonical_bytes()`.

# 5. Decisiones técnicas

## DEC-001 — Cierre y proyección desde una evaluación común

**Decisión:** una evaluación por feature determinará estados de SPEC/PLAN/
TASKS, tareas, validación y errores; `audit_repository()` emitirá issues y
`projected_state()` usará el mismo resultado para proyectar VALIDATED solo
cuando el cierre sea coherente. El ledger vigente seguirá verificándose en
`audit_repository()` antes de aceptar PASS global.

**Justificación:** evita que el handoff marque validada una feature que el
checker rechaza. **Traza:** FR-001, BR-001, AC-001/002.

**Alternativas:** comprobar solo al final de `audit_repository()` mantendría
proyecciones falsas; nueva herramienta duplicaría el contrato actual.

**Consecuencias:** el handoff deberá reflejar el estado derivado si una
validación histórica se reabre. **ADR:** NO; evolución local del checker.

## DEC-002 — Estado por ficha de TASK

**Decisión:** `**Estado:**` bajo cada `## TASK-[XXX]` será el estado operativo.
La tabla de orden es una vista que debe listar cada TASK exactamente una vez
y repetir su estado. TASKS `COMPLETED` exige todas `DONE`. El lector rechazará
estado ausente, duplicado, desconocido o conflicto ficha/tabla, incluidos
campos combinados como los de TASKS-009; no inferirá `DONE` del reporte.

**Justificación:** ofrece una fuente clara y hace visible la discrepancia.
**Traza:** FR-003/004, AC-003. **Alternativas:** hacer la tabla autoridad
perpetuaría dos significados para `**Estado:**`. **Consecuencias:** ajustar
instrucciones/template y resolver TASKS-009; el formato combinado deja de
ser válido. **ADR:** NO.

## DEC-003 — Evidencia estructural comprobable

**Decisión:** extraer IDs AC de encabezados de SPEC, IDs TASK de encabezados
de TASKS y resultados del reporte. El cierre exigirá para cada AC una fila
individual PASS con TEST/verificación y evidencia localizable; para cada TASK,
estado DONE y referencia localizable en la validación; y resultado PASS de
los TEST requeridos, además de un resultado final PASS y ausencia de
bloqueos/finding abiertos declarados. Las rutas referidas deben resolver
dentro del repositorio y existir. El parser aceptará los formatos de tabla
históricos reconocibles y la plantilla nueva fijará el formato inequívoco;
un formato no interpretable fallará con diagnóstico, sin declarar PASS.

**Justificación:** comprueba presencia y consistencia, mientras `/validate`
revisa calidad y contenido de la evidencia. **Traza:** FR-001/002,
NFR-001/002, AC-002/004/005. **Alternativas:** contar palabras PASS permite
falsos cierres; un manifiesto nuevo duplicaría reportes y requeriría migrar
todo el historial. **Consecuencias:** adaptar reportes históricos solo cuando
falte un dato estructural real y con trazabilidad; no inventar evidencias.
**ADR:** NO.

## DEC-004 — Migración gobernada de TASKS-009

**Decisión:** tras aprobar TASKS-010, preparar el cambio mínimo de las once
fichas de TASKS-009 para que digan `DONE` en líneas independientes. Como
`canonical_bytes()` no normaliza el texto combinado, obtener aprobación
humana explícita de la nueva versión y registrar un evento `APPROVAL` que
reemplace DECISION-003 mediante `supersedes`; después cotejar PLAN/SPEC y
revalidar SPEC-009 con evidencia existente más la corrección. No ejecutar
esta mutación sin esa decisión, aunque TASKS-010 esté aprobada.

**Justificación:** respeta artículo VIII y huella de contenido autorizado.
**Traza:** FR-004, BR-001, AC-003. **Alternativas:** cambiar el hash o añadir
una excepción específica ocultaría la contradicción. **Consecuencias:**
hay un gate humano adicional para reparar la feature anterior. **ADR:** NO.

# 6. Arquitectura y flujo

| Componente | Responsabilidad | Cambio |
|------------|-----------------|--------|
| `src/check_harness_state.py` | Evaluar cierre, estados y proyección | MODIFY |
| `tests/test_check_harness_state.py` | Casos unitarios y adversos de gates | MODIFY |
| `tests/test_adopt_harness.py` | Recorrido en destino limpio | MODIFY |
| Template/command de TASKS y validación | Formato y precondiciones | MODIFY |
| `docs/state-reconstruction.md` | Contrato durable y migración | MODIFY |
| TASKS/validación/ledger de SPEC-009 | Corregir y revalidar historial afectado | MODIFY con gate propio |

Flujo: leer artefactos → validar ledger y estados → leer TASK/tabla → analizar
reporte/AC/TEST/evidencia → generar issues → proyectar active/validated →
comparar handoff e índice. Usar funciones pequeñas dentro del checker; sin
ciclos ni nuevo paquete.

# 7. Datos, contratos y compatibilidad

No hay persistencia externa ni migración de esquema. Los contratos son los
Markdown y `decisions.json` existentes. `Issue(code, path, detail)` se
mantiene; se añaden códigos específicos para estados y evidencia. El parser
solo acepta rutas de evidencia relativas y contenidas en el repo; rechaza
`..`, rutas absolutas y destinos inexistentes. `canonical_bytes()` conserva
su formato salvo una regla prospectiva justificada por pruebas; no se
reescriben hashes previos. `DESTRUCTIVE CHANGE: NO`.

La tabla de TASKS se mantiene por legibilidad, sincronizada con cada ficha.
Los reportes antiguos con estructura diferente deben pasar por adaptadores
acotados al formato observado, no por una exención amplia. Las aprobaciones
de SPEC-001 a SPEC-006 siguen siendo legado no verificable, sin inventar
eventos ni dispensar contradicciones de TASKS.

# 8. Seguridad y manejo de errores

Sin autenticación ni permisos nuevos. Tratar archivos Markdown/JSON como
entradas no confiables: parser acotado, errores controlados y rutas contenidas
en el repositorio. No imprimir contenido completo, secretos ni trazas en
diagnósticos. Fixtures con textos sintéticos. Estado desconocido o evidencia
rota producen FAIL, nunca éxito por defecto. SEC-001 → AC-005.

# 9. Estrategia de pruebas y TDD

Para código nuevo o defectos reproducibles, RED antes de cambiar checker y
GREEN después, según testing §21. Documentación usa cotejo de formato y
checker como verificación alternativa. Sin tests vacíos ni cambios de
expectativa para forzar PASS.

| AC | Verificación prevista | RED inicial |
|----|-----------------------|-------------|
| AC-001 | Fixture `VALIDATED` con TASKS APPROVED y con TASK TODO; salida FAIL y proyección activa | Sí |
| AC-002 | AC/TEST/evidencia completos PASS; ausencia, FAIL o ruta rota rechazada | Sí |
| AC-003 | Ficha/tabla contradictoria y duplicada; TASKS-009 corregida con gate | Sí para checker; documental para migración |
| AC-004 | Test de adopción SPEC→PLAN→TASKS→VALIDATED, con estados intermedios y negativos | Sí |
| AC-005 | Diagnósticos estables y fixtures sin secretos | Sí para diagnóstico; revisión para secretos |

Ejecutar tests dirigidos, luego `python3 -m unittest discover -s tests -v`,
`python3 src/check_harness_state.py` y `git diff --check`; registrar comandos,
causa de RED y resultados GREEN por tarea en `evidence/`.

# 10. Impacto en repositorio

**CREATE:** evidencia y validación de SPEC-010 durante fases posteriores.

**MODIFY tras gates:** checker, dos archivos de tests, commands/templates de
TASKS y validación si el formato lo exige, `docs/state-reconstruction.md`,
TASKS/ledger/validación de SPEC-009 con su aprobación específica, y
handoff/índice como proyecciones.

**REUSE:** adopción, ledger, canonicalización, parser de proyección y suite
existente. **REMOVE:** ninguno. **Dependencias nuevas:** ninguna.
**Configuración:** ninguna. **Build/CI:** workflow existente ejecuta suite y
checker; no se cambia salvo descubrimiento justificado y gate correspondiente.

# 11. Riesgos técnicos

## RISK-001 — Variantes históricas

**Impacto:** HIGH. **Probabilidad:** MEDIUM. Reportes antiguos no siguen una
tabla única. **Mitigación:** inventario de nueve formatos, fixtures de
regresión y adaptadores limitados; bloquear si una evidencia no puede
reconstruirse sin inventarla.

## RISK-002 — Hash de TASKS-009

**Impacto:** HIGH. **Probabilidad:** HIGH. La corrección de fichas cambia
contenido aprobado. **Mitigación:** DEC-004 y nueva aprobación explícita
antes de editar; revalidación y checker PASS después.

# 12. Aclaraciones técnicas y ADR

No hay `Q-TECH` bloqueante. No se requiere ADR: el cambio permanece en el
comprobador, los formatos del Harness y pruebas existentes.

# 13. Orden para TASKS

Primero inventariar variantes y preparar casos RED. Luego implementar lectura
de TASK y cierre/evidencia, sincronizar proyección, actualizar formato
documental y probar adopción completa. Preparar la reparación de TASKS-009;
aplicar solo tras su aprobación humana, revalidar y ejecutar regresión final.

# 14. Criterios para avanzar a TASKS

- [x] SPEC aprobada, MUST/AC cubiertos, impacto y compatibilidad identificados.
- [x] Seguridad, TDD, riesgos, dependencias y ADR revisados.
- [x] PLAN aprobado por humano y decisión registrada.

# 15. Estado del plan

**Estado actual:** APPROVED  
**Aprobado por:** Usuario responsable del proyecto  
**Fecha de aprobación:** 2026-10-07  
**Decisión explícita y alcance:** «Revisado y aprobado» en respuesta a PLAN-010 v0.1.0; autoriza preparar TASKS-010.  
**Registro durable:** `specs/010-validation-gates/decisions.json`.
