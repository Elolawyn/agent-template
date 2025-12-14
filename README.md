# Agent Template

Plantilla para crear agentes de inteligencia artificial con FastAPI.

## 🏆 Features

- ✅ **API FastAPI moderna** con Python 3.13
- ✅ **Configuración completa** de desarrollo (ruff, pyright, pytest)
- ✅ **Coverage automatizado** con reportes HTML
- ✅ **Testing integrado** con logging
- ✅ **Middleware configurado** (CORS, timing, seguridad)
- ✅ **Gestión de dependencias** con uv
- ✅ **VS Code integration** completa
- ✅ **Arquitectura modular** y escalable

## 🛠️ Tech Stack

- **Backend**: FastAPI, Uvicorn, Pydantic
- **Python**: 3.13.1
- **Dev Tools**: Ruff, Pyright, pytest-cov
- **Testing**: pytest con asyncio y coverage
- **Security**: pip-audit para vulnerabilidades
- **Package Manager**: uv

## 🚀 Para Empezar

```bash
# Clonar el repositorio
git clone https://github.com/Elolawyn/agent-template.git
cd agent-template

# Instalar dependencias
uv sync

# Ejecutar tests (con coverage y logging)
uv run pytest

# Iniciar el servidor
uv run python -m agent_template.main

# Verificar endpoint de health
curl http://localhost:8000/
```

## 📁 Estructura del Proyecto

```
agent-template/
├── src/agent_template/        # Paquete principal
│   ├── __init__.py            # Inicialización del paquete con metadatos dinámicos
│   ├── main.py                # Punto de entrada y ejecución del servidor
│   ├── app.py                 # Creación y configuración de FastAPI
│   ├── settings.py            # Gestión de configuración con Pydantic (centralizada)
│   ├── middleware.py          # Configuración de middlewares
│   ├── lifecycle.py           # Gestión de ciclo de vida de la app
│   ├── _metadata.py           # Módulo de metadatos centralizados
│   └── api/                   # Endpoints de la API
│       ├── __init__.py
│       └── v1/                # API versión 1
│           ├── __init__.py
│           ├── health.py      # Endpoint de health
│           └── root.py        # Endpoint raíz
├── tests/                     # Suite de tests
│   ├── conftest.py            # Configuración y fixtures de pytest
│   ├── test_settings.py       # Configuración de tests
│   └── test_api/              # Tests de la API
│       └── test_health.py     # Tests del endpoint de health
├── .vscode/                   # Configuración de VS Code
│   ├── settings.json          # Configuración del editor
│   └── tasks.json             # Tareas automatizadas
├── pyproject.toml             # Configuración del proyecto y dependencias
├── .python-version            # Versión de Python
├── .tool-versions             # Versiones de herramientas
└── README.md                  # Este archivo
```

## 🧪 Testing

```bash
# Ejecutar todos los tests (con coverage HTML + logging)
uv run pytest

# Ejecutar tests por tipo
uv run pytest -m unit       # Solo tests unitarios
uv run pytest -m "not slow" # Excluir tests lentos

# Coverage con reportes específicos
uv run pytest --cov=src --cov-report=html --cov-report=term  # HTML para desarrollo local
uv run pytest --cov=src --cov-report=xml --cov-report=json --cov-report=term  # XML/JSON para CI
```

## 🔒 Seguridad

```bash
# Escanear vulnerabilidades en dependencias
uv run pip-audit --dry-run

# Verificar actualizaciones de dependencias
uv run pip list --outdated
```

## 📋 Metadatos Centralizados

El proyecto utiliza metadatos dinámicos centralizados desde `pyproject.toml`. Esto significa que toda la información del paquete (nombre, versión, descripción) se lee automáticamente de un único lugar.

## 📚 Documentación

- [**AGENTS.md**](AGENTS.md) - Guía para desarrolladores
- [**TODO.md**](TODO.md) - Roadmap del proyecto
- [**CHANGELOG.md**](CHANGELOG.md) - Registro de cambios

## 🏗️ Próximos Pasos

Ver [TODO.md](TODO.md) para ver las tareas pendientes y el roadmap del proyecto.

## 📝 Licencia

Este proyecto está licenciado bajo la Licencia MIT.
