# 🧠 AI Methodology Ecosystem

> **Fuente de la verdad para agentes de IA** — Documentación estructurada de todo el ecosistema de desarrollo, perfiles de equipo, y 31 proyectos activos/inactivos distribuidos en 3 VPS.

---

## 📖 ¿Qué es esto?

Este repositorio contiene la **documentación metodológica** y el **contexto completo** de todos los proyectos del ecosistema. Está diseñado para que cualquier agente de IA (o nuevo miembro del equipo) pueda **entender en minutos**:

- Quién eres (`profile/`) → stack, workflow, convenciones, seguridad, preferencias.
- Qué proyectos existen (`project/index.md`) → 31 proyectos con ubicación, estado y descripción.
- Detalles técnicos de cada grupo (`projects/`) → arquitectura, estado actual, decisiones clave.

Es la **memoria persistente** del ecosistema.

---

## 📂 Estructura del repositorio

```
.
├── .gitignore
├── README.md
├── profile/                     # Perfil del equipo y metodología
│   ├── agents.md               # Cómo interactuar con agentes
│   ├── conventions.md          # Reglas de estilo y estructura
│   ├── preferences.md          # Preferencias de comunicación
│   ├── security.md             # Principios de seguridad
│   ├── stack.md                # Stack tecnológico completo
│   └── workflow.md             # Flujo de trabajo Plan → Build → Documentación
├── project/
│   └── index.md                # Índice maestro de 31 proyectos (VPS1, VPS2, VPS3)
└── projects/                   # Documentación detallada por grupo
    ├── babywonder/             # Motor de renderizado médico (producción)
    ├── nexus/                  # Plataforma multi-tenant contenerizada
    ├── bots/                   # Bots de Telegram y WhatsApp (8 proyectos)
    ├── qch/                    # Asistente culinario con IA (cocina-con-ia)
    ├── web-apps/               # Flask + React (4 proyectos)
    ├── node-apps/              # Node.js + React + Supabase (6 proyectos)
    ├── wordpress-blogs/        # Blogs corporativos (2 proyectos)
    └── static-sites/           # Sitios HTML/CSS/JS estáticos (7 proyectos)
```

## 🚀 ¿Cómo se usa?

🤖 Para agentes de IA

* Clona el repositorio o accede a los archivos.
* Lee profile/ para entender el stack, convenciones y flujo de trabajo.
* Consulta project/index.md para localizar un proyecto específico.
* Entra en projects/[grupo]/ para ver contexto, arquitectura, estado y decisiones.

👨🏻 Para humanos

*Úsalo como documentación viva para onboarding de nuevos miembros.
*Mantén los archivos actualizados a medida que evolucionan los proyectos.
*Es el punto de partida para cualquier reunión técnica o planificación.

## 📊 Proyectos incluidos (31 en total)

VPS	Activos	Inactivos	Total	Propósito
VPS1 (89.167.100.214)	11	6	17	Laboratorio / Entorno Legacy
VPS2 (204.168.228.41)	8	0	8	Productos de Negocio
VPS3 (37.27.201.215)	8	0	8	Producción / Industrialización

##📌 Todos los detalles en project/index.md

##🛠️ Tecnologías principales

Área	Tecnologías
Backend	Python (Flask, FastAPI), Node.js, PHP (WordPress)
Frontend	React, Vite, TypeScript, Tailwind
IA/ML	OpenAI, Anthropic Claude, Google Gemini, Ollama, MediaPipe, Replicate
Bases de datos	PostgreSQL, MySQL, Redis, Supabase
Infraestructura	Docker, Docker Compose, Traefik, Nginx, Gunicorn, Uvicorn, PM2, systemd

## 📬 Cómo contribuir

Actualiza los archivos cuando cambie un proyecto (estado, arquitectura, decisiones).
Usa worklog.md dentro de cada grupo para registrar cambios relevantes.
Sigue las convenciones definidas en profile/conventions.md.
Haz commits claros con mensajes descriptivos.

## 📝 Nota
Este repositorio es la base de conocimiento para el ecosistema. Sin él, los agentes trabajarían a ciegas. Mantenerlo actualizado es una prioridad.

👤 Mantenido por — Roberto Rios - Respuestas Inteligentes
📅 Última actualización — Agosto 2026
