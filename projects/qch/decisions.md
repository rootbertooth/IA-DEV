# Decisiones Arquitectónicas: ¿Qué Cocino Hoy? (QCH)

## 1. Uso de Flask en lugar de FastAPI/Django
- **Contexto:** Prototipo inicial con requerimientos simples.
- **Decisión:** Flask por su simplicidad y curva de aprendizaje baja.
- **Alternativas:** FastAPI, Django.
- **Rationale:** Flask es más ligero y permite iterar rápido; se puede migrar a FastAPI en el futuro si se requiere asincronía.

## 2. Dual Provider (OpenAI + Anthropic)
- **Contexto:** Necesidad de robustez y calidad en las respuestas.
- **Decisión:** Usar OpenAI para embeddings y Anthropic Claude para razonamiento culinario.
- **Alternativas:** Solo OpenAI, solo Anthropic.
- **Rationale:** Claude tiene mejor razonamiento en tareas complejas (menús, modos); OpenAI es mejor para embeddings y tareas generales.

## 3. RAG Custom en MySQL (sin Vector DB externa)
- **Contexto:** Necesidad de caché semántico sin infraestructura adicional.
- **Decisión:** Almacenar embeddings en BLOB en MySQL y calcular similitud coseno en Python.
- **Alternativas:** Pinecone, Weaviate, pgvector.
- **Rationale:** Simplifica la arquitectura (no requiere servicios externos) y reduce costes.

## 4. Prompts Externalizados en Archivos .txt
- **Contexto:** Iteración rápida de prompts sin modificar código.
- **Decisión:** Cada prompt en un archivo .txt dentro de ackend/prompts/.
- **Alternativas:** Hardcodear prompts en Python, usar base de datos.
- **Rationale:** Permite editar prompts sin reiniciar el servidor y facilita A/B testing.

## 5. Uso de Few-shot y JSON Mode
- **Contexto:** Necesidad de salidas estructuradas y precisas.
- **Decisión:** Incorporar ejemplos (few-shot) y solicitar JSON en los prompts.
- **Alternativas:** Salida libre con procesamiento posterior.
- **Rationale:** JSON Mode garantiza estructura consistente para el frontend; few-shot mejora la precisión.

## 6. Autenticación JWT con Middleware
- **Contexto:** Protección de endpoints y control de créditos.
- **Decisión:** JWT con PyJWT y middlewares personalizados.
- **Alternativas:** OAuth2, sesiones de Flask.
- **Rationale:** JWT es sin estado y fácil de escalar.

## 7. Backups Manuales con Estructura de Carpetas
- **Contexto:** Seguimiento de cambios y recuperación ante fallos.
- **Decisión:** Backups manuales con timestamp (carpetas y archivos .sql).
- **Alternativas:** Backups automáticos con scripts, Git LFS.
- **Rationale:** Simple y efectivo para un proyecto en evolución.
