# Decisiones Arquitectónicas: BabyWonder Motor

## 1. Uso de FastAPI en lugar de Flask
- **Contexto:** Necesidad de manejar operaciones asíncronas y alto rendimiento.
- **Decisión:** Elegir FastAPI por su soporte nativo de async/await y generación automática de OpenAPI.
- **Alternativas:** Flask con gevent, Django.
- **Rationale:** FastAPI ofrece mejor rendimiento para I/O-bound operations (llamadas a Gemini, Replicate) y mejor integración con Pydantic.

## 2. Detección Dual: Gemini + MediaPipe
- **Contexto:** La detección de rostros en ecografías es crítica; un solo modelo puede fallar.
- **Decisión:** Usar Gemini 3.5 Flash como modelo primario y MediaPipe como fallback offline.
- **Alternativas:** Solo Gemini, solo MediaPipe, YOLO.
- **Rationale:** Gemini ofrece alta precisión semántica; MediaPipe da garantía de funcionamiento offline y es rápido.

## 3. JWT RS256 con Firebase Service Account
- **Contexto:** Necesidad de autenticación robusta y fail-closed.
- **Decisión:** Implementar JWT RS256 con verificación local de clave pública derivada de Firebase Service Account.
- **Alternativas:** OAuth2 tradicional, API keys.
- **Rationale:** Fail-closed (503 sin config), verificación offline (sin dependencia de Google en cada request), TTL limitado (900s).

## 4. Renderizado con Replicate (GPT Image 2.0)
- **Contexto:** Generación de imágenes fotorrealistas a partir de ecografías.
- **Decisión:** Usar Replicate API con modelo openai/gpt-image-2.
- **Alternativas:** Stable Diffusion local, Midjourney API, DALL-E.
- **Rationale:** GPT Image 2.0 está optimizado para fotorrealismo y tiene buena integración con Replicate (timeout configurable).

## 5. Semaphore(1) para Serializar Renders
- **Contexto:** El renderizado consume muchos recursos y tiene coste por API call.
- **Decisión:** Implementar semáforo de 1 para serializar renders (uno concurrente).
- **Alternativas:** Cola de mensajería (Redis/RabbitMQ).
- **Rationale:** Implementación simple y efectiva para evitar sobrecarga; se planifica migrar a colas en el futuro.

## 6. Auditoría Estructurada con UUID
- **Contexto:** Necesidad de trazabilidad en un sistema médico.
- **Decisión:** Cada ejecución genera un directorio UUID con timestamp, imágenes intermedias y metadatos JSON.
- **Alternativas:** Logs tradicionales, base de datos.
- **Rationale:** Permite reconstruir cualquier ejecución, auditarla y depurar fallos.

## 7. Nginx como Frontend
- **Contexto:** Exposición de la API al exterior.
- **Decisión:** Usar Nginx como proxy inverso con TLS termination en 443.
- **Alternativas:** Traefik, Apache.
- **Rationale:** Nginx ya está en uso en otros proyectos, y es ligero y fiable para TLS.
