# Contexto del Proyecto: BabyWonder Motor

## Propósito y Visión
BabyWonder Motor es un motor de renderizado fotorrealista especializado en ecografías obstétricas 3D/4D. Transforma imágenes médicas en retratos hiperrealistas del feto.

## Dominio y Alcance
- **Área:** Salud / Diagnóstico por Imagen (Obstetricia)
- **Input:** Ecografías 3D/4D (PNG/JPG)
- **Procesos:** Detección facial con IA (Gemini + MediaPipe), mejora de imagen (CLAHE), renderizado (GPT Image 2.0), post-procesado fotográfico, auditoría completa.

## Actores
- **Médico/Especialista:** Envía imágenes y recibe resultados.
- **Paciente:** Recibe la imagen renderizada.
- **Sistema:** Ejecuta el pipeline automáticamente.
- **Administrador:** Mantiene y monitorea el sistema.

## Entorno
- **Servidor:** VPS3 (37.27.201.215)
- **Estado:** ✅ Activo en producción (PID 15050, babywonder-api.service)
- **Acceso:** API REST vía Nginx (HTTPS:443) → FastAPI (127.0.0.1:8000)
- **Seguridad:** JWT RS256 con Firebase Service Account (fail-closed)

## Relaciones con Otros Proyectos
- **/opt/ai (ai-infra):** Independiente. BabyWonder usa modelos en nube (Gemini, Replicate), no Ollama.
- **/opt/BOTS:** Independiente. No hay comunicación ni compartición.

## Estado Actual
- **Desarrollo:** Pipeline V4 completo y en producción.
- **Rendimiento:** 2-3 minutos por render (dominado por GPT Image 2.0).
- **Próximos pasos:** Activar ENHANCE_ENABLED=True, implementar colas de renderizado, añadir monitoreo con Prometheus/Grafana.
