# Estado Actual: ¿Qué Cocino Hoy? (QCH)

## Información General
| Métrica | Valor |
|---------|-------|
| **Estado** | ✅ Activo |
| **PID** | 855, 1058 |
| **Servidor** | Gunicorn (workers: 1) |
| **Puerto** | 5000 |
| **Última modificación** | 15 Aug 2026 |
| **Tamaño total** | 226M |

## Modos de Prompt Implementados
| Modo | Archivo | Propósito |
|------|---------|-----------|
| Apetece | modo_apetece.txt | Interpretar antojos y sugerir recetas |
| Clásica | modo_clasica.txt | Recetas tradicionales auténticas |
| Cocción | modo_coccion.txt | Ayuda en tiempo real durante la cocción |
| Ingredientes | modo_ingredientes.txt | Recetas por ingredientes disponibles |
| Menú | modo_menu.txt | Generación de menús semanales |
| Mundo | modo_mundo.txt | Gastronomía internacional |
| Rápido | modo_rapido.txt | Recetas en menos de 30 minutos |
| Tiempo | modo_tiempo.txt | Recetas según el clima |
| Visión | modo_vision.txt | Análisis de fotos de platos |

## Métricas de Rendimiento
| Fase | Duración |
|------|----------|
| Embedding | ~0.5s |
| Búsqueda en caché | ~0.2s |
| Llamada a IA (Claude/OpenAI) | 2-5s |
| Total | 2.5-5.5s |

## Backups Realizados
| Fecha | Archivo | Tamaño |
|-------|---------|--------|
| 2026-08-01 | ackups/phase1_p0_20260801_080756/ | - |
| 2026-08-01 | ackups/20260801_091401_p1_p2_full/ | - |
| 2026-07-30 | ackups/frontend_20260730_183950/ | - |
| 2026-04-20 | ackup_20260420_192501.sql | 8.9M |

## Problemas Conocidos
- Dependencia de APIs externas (latencia, coste).
- Caché semántico con umbral fijo (puede fallar en consultas nuevas).
- Sin contenerización.

## Próximos Pasos
1. Ajustar umbral de similitud coseno para mejorar aciertos.
2. Añadir más ejemplos en prompts (few-shot).
3. Considerar migrar a FastAPI para mejor rendimiento.
4. Implementar monitoreo de costes de API.
