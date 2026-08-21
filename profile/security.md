# Principios de Seguridad (Security)

Este documento establece los principios, prácticas y controles de seguridad que deben aplicarse en todos los proyectos del ecosistema. Está basado en patrones observados en las auditorías (gestión de `.env`, autenticación JWT, CORS, rate limiting) y en las mejores prácticas para entornos de producción.

---

## 1. Gestión de Secretos y Variables de Entorno

### 1.1 Principios
- **Nunca** versionar secretos (claves API, contraseñas, tokens, certificados).
- **Usar variables de entorno** para toda configuración sensible.
- **Proveer un archivo `.env.example`** con todas las variables necesarias (valores ficticios o vacíos).
- **Restringir permisos** de los archivos `.env` a `600` (lectura/escritura solo para el propietario).

### 1.2 Estructura Recomendada
```bash
# .env (en la raíz del backend o del proyecto)
DB_HOST=localhost
DB_USER=user
DB_PASSWORD=secure_password
DB_NAME=database

OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GEMINI_API_KEY=AIza...

JWT_SECRET_KEY=super_secret_key
DEBUG=False
1.3 Carga en Código
Python (Flask/FastAPI): Usar python-dotenv + pydantic-settings para cargar y validar.

Node.js: Usar dotenv o process.env directamente.

Ejemplo (Python):

python
from dotenv import load_dotenv
import os

load_dotenv()
DB_PASSWORD = os.getenv("DB_PASSWORD")
2. Autenticación y Autorización
2.1 Autenticación (JWT)
Uso general: JWT (JSON Web Tokens) para APIs sin estado.

Algoritmo: HS256 (para proyectos simples) o RS256 (para sistemas críticos como /opt/API).

TTL máximo: 15 minutos (900 segundos) para tokens de acceso.

Renovación: Implementar refresh tokens (si aplica) o solicitar nueva autenticación.

Validación:

Verificar firma y kid (key ID) en tokens RS256.

Validar aud (audiencia) y iss (emisor).

Rechazar tokens expirados o malformados.

2.2 Autorización (Roles y Permisos)
Implementar middlewares en Flask/FastAPI para verificar roles.

Roles comunes:

admin: Acceso total a gestión de usuarios/configuración.

client: Acceso solo a sus propios datos (en sistemas multi-tenant).

superadmin: Gestión de tenants (en plataformas SaaS).

2.3 Fail-Closed
Principio: Ante una falla en la autenticación (ej. falta de archivo de configuración), el sistema debe rechazar todas las peticiones (error 503) en lugar de permitir acceso no autenticado.

Ejemplo: /opt/API devuelve 503 si no encuentra el archivo firebase-service-account.json.

3. Seguridad de APIs
3.1 CORS (Cross-Origin Resource Sharing)
Restringir orígenes: Permitir solo dominios específicos (no * en producción).

Configuración en Flask:

python
CORS(app, resources={r"/api/*": {"origins": ["https://dominio.com"]}})
Configuración en FastAPI: Usar CORSMiddleware con allow_origins definido.

3.2 Rate Limiting
Implementar en todas las APIs expuestas: Proteger contra ataques de fuerza bruta y sobrecarga.

Herramientas:

flask-limiter para Flask.

slowapi para FastAPI.

Nginx limit_req para proxies.

Límites sugeridos:

/generate: 5 peticiones por minuto (por IP).

/auth/login: 3 peticiones por minuto (por IP).

/health: 10 peticiones por minuto (por IP).

3.3 Validación de Inputs
Siempre validar y sanitizar todos los datos de entrada (formularios, JSON, archivos).

Usar Pydantic para validación de schemas en Python.

Limitar el tamaño de archivos subidos (ej. 10MB para imágenes).

Rechazar archivos con extensiones peligrosas (.php, .exe, .sh).

4. Seguridad de la Infraestructura
4.1 Acceso SSH
Usar autenticación por clave pública (deshabilitar autenticación por contraseña).

Usuarios dedicados: Cada proyecto debe tener un usuario Unix independiente (wpblog, z-agent-stock, superz).

Permisos: Carpeta .ssh con permisos 700, authorized_keys con 600.

Cambiar puerto SSH: (opcional) para evitar ataques automatizados.

4.2 Firewall (UFW/iptables)
Permitir solo puertos necesarios: 80, 443, SSH (22 o puerto personalizado).

Bloquear puertos internos: Los servicios como Uvicorn (:8000) deben escuchar solo en localhost, no en 0.0.0.0.

4.3 Contenedores (Docker)
No ejecutar contenedores como root: Usar usuarios no privilegiados en Dockerfile.

Montar volúmenes de solo lectura cuando sea posible.

Escaneo de vulnerabilidades: Usar herramientas como trivy o snyk para imágenes base.

5. Auditoría y Registro
5.1 Logs de Seguridad
Registrar eventos críticos:

Intentos de autenticación (éxito/fallo).

Cambios en configuración (.env, config.py).

Acciones administrativas (creación de usuarios, borrado de datos).

Formato: Incluir timestamp, IP, usuario, acción, resultado.

Protección: No logear datos sensibles (contraseñas, tokens).

5.2 Auditoría de Ejecuciones
En proyectos críticos (ej. /opt/API), mantener un sistema de auditoría estructurada:

UUID por ejecución.

Almacenar inputs, outputs, metadatos y tiempos.

Política de retención (ej. 30 días).

6. Protección de Datos (GDPR / Privacidad)
6.1 Datos Personales
No almacenar información personal innecesaria.

Anonimizar datos de auditoría si contienen información identificable (ej. imágenes médicas).

Implementar política de retención: Eliminar datos antiguos automáticamente.

6.2 Encriptación
En tránsito: Usar TLS/HTTPS para todas las comunicaciones externas.

En reposo: Encriptar bases de datos si contienen datos sensibles (ej. pgcrypto en PostgreSQL).

7. Principios de "Fail-Safe" y "Fail-Closed"
7.1 Fail-Closed
Ante una falla de configuración o autenticación, el sistema debe rechazar las peticiones (no permitir acceso por defecto).

Ejemplo: Si no hay archivo .env, el sistema no debe arrancar o debe devolver error 503.

7.2 Fail-Safe
Funciones opcionales (ej. fase8_enhance) deben fallar sin afectar al flujo principal.

Ejemplo: Si fase8_enhance falla, el sistema debe devolver el resultado de la fase 1 sin error.

8. Recomendaciones Adicionales
Escaneo de vulnerabilidades: Realizar análisis periódicos con herramientas como OWASP ZAP, SonarQube o Snyk.

Actualización de dependencias: Mantener actualizadas las librerías críticas (Flask, FastAPI, OpenCV, etc.) para parchear CVEs conocidos.

Rotación de claves: Cambiar claves API y JWT secrets periódicamente (ej. cada 90 días).

Backups cifrados: Almacenar backups en ubicaciones seguras y con encriptación.

Este documento se actualiza conforme surgen nuevas amenazas o cambios en la arquitectura. Revisión periódica recomendada.