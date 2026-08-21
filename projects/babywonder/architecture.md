# Arquitectura Técnica: BabyWonder Motor

## Stack Tecnológico
| Componente | Tecnología | Versión |
|------------|------------|---------|
| **Framework API** | FastAPI | 0.115.0 |
| **Servidor ASGI** | Uvicorn | 0.30.6 |
| **Validación** | Pydantic | 2.9.0 |
| **Configuración** | pydantic-settings | 2.5.0 |
| **Procesamiento Imagen** | OpenCV (headless) | 4.11.0.86 |
| | Pillow | 10.4.0 |
| | NumPy | 1.26.4 |
| | SciPy | 1.14.1 |
| **IA/ML** | Google Gemini | 3.5 Flash |
| | MediaPipe | 0.10.21 |
| | Replicate API (GPT Image 2.0) | - |
| **Autenticación** | python-jose (JWT RS256) | 3.3.0 |
| | cryptography | - |
| | firebase-admin | - |

## Pipeline V4 (8 Fases)

```
Input (Ecografía 3D/4D)
        │
        ▼
┌─────────────────┐
│ FASE 0          │ 5.4s avg
│ Detection       │ ← Gemini 3.5 Flash (primario)
│ Dual AI         │ ← MediaPipe (fallback si conf < 0.60)
└────────┬────────┘
         │ viable?
    NO   │   YES
    ▼    │    ▼
 REJECT  │  ┌─────────────────┐
         │  │ FASE 1          │ 91ms
         │  │ Crop            │ ← Adaptive padding (face/skull)
         │  └────────┬────────┘
         │           ▼
         │  ┌─────────────────┐
         │  │ FASE 2          │ 259ms
         │  │ CLAHE           │ ← Contrast Limited AHE
         │  └────────┬────────┘
         │           ▼
         │  ┌─────────────────┐
         │  │ FASE 3          │ ~0ms
         │  │ Re-detection    │ ← Solo si Gemini falló inicialmente
         │  └────────┬────────┘
         │           ▼
         │  ┌─────────────────┐
         │  │ FASE 4          │
         │  │ Pose Estimation │ ← Yaw, tilt, facing_direction
         │  └────────┬────────┘
         │           ▼
         │  ┌─────────────────┐
         │  │ FASE 5          │
         │  │ Skull Mask      │ ← Gaussian feathering
         │  └────────┬────────┘
         │           ▼
         │  ┌─────────────────┐
         │  │ FASE 6          │
         │  │ Composite       │ ← Ultrasound + mask on black
         │  └────────┬────────┘
         │           ▼
         │  ┌─────────────────┐
         │  │ PHASE 1         │ ~120-180s
         │  │ RENDER          │ ← GPT Image 2.0 (Replicate)
         │  └────────┬────────┘
         │           ▼ (opcional)
         │  ┌─────────────────┐
         │  │ FASE 8          │
         │  │ Enhance         │ ← Segunda pasada (reparación anatómica)
         │  └────────┬────────┘
         │           ▼
         │  ┌─────────────────┐
         │  │ POSTPROCESS     │
         │  │ Photo Finish    │ ← Film grain, chrom.aberr., vignette
         │  └────────┬────────┘
         ▼           ▼
    Final Portrait (PNG, base64)

```
## Autenticación JWT RS256
- **Firma:** RS256 con clave privada local.
- **Verificación:** Firebase Service Account (fail-closed).
- **TTL:** 900s (15 min).
- **Audiencia:** abywonder-motor-v4.
- **Fail-closed:** Sin .json → 503 para todos.

## Seguridad
- ✅ Uvicorn solo en localhost.
- ✅ CORS restringido.
- ✅ .env y irebase-service-account.json en .gitignore.

## Auditoría
- Cada ejecución genera un directorio en /opt/API/audit/.
- Estructura: {timestamp}_{uuid}/ con imágenes intermedias y metadata.json.

## Endpoints
| Endpoint | Método | Autenticación | Propósito |
|----------|--------|---------------|-----------|
| /generate | POST | JWT RS256 | Renderizado de ecografía |
| /generate-test | POST | ❌ (temporal) | Endpoint de desarrollo |
| /result/{id} | GET | ❌ | Descarga de imagen renderizada |
| /transition | POST | JWT RS256 | Generación de video de transición |
| /health | GET | ❌ | Health check |
