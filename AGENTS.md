# Agent Template - Compatibilidad con Agentes de Código

Este archivo contiene información para que los agentes de código puedan entender y trabajar con este proyecto eficazmente.

## Visión del Proyecto

**Agent Template** es una plantilla de aplicación FastAPI en Python para crear agentes de IA. Proporciona una base estructurada para construir sistemas de agentes con gestión de configuración apropiada, endpoints de API y herramientas de desarrollo.

## Estructura del Proyecto
```
agent-template/
├── src/agent_template/        # Paquete principal
│   ├── __init__.py            # Inicialización del paquete con metadatos dinámicos
│   ├── main.py                # Punto de entrada (CLI y arranque del servidor)
│   ├── app.py                 # Creación y configuración de FastAPI
│   ├── settings.py            # Gestión de configuración con Pydantic (centralizada)
│   ├── _metadata.py           # Módulo de metadatos desde pyproject.toml
│   ├── middleware.py          # Configuración de middlewares
│   ├── lifecycle.py           # Gestión de ciclo de vida de la aplicación
│   └── api/                   # Endpoints de la API
│       ├── __init__.py
│       └── v1/                # API versión 1
│           ├── __init__.py
│           ├── health.py      # Endpoint de health
│           └── root.py        # Endpoint raíz
├── tests/                     # Suite de tests
│   ├── conftest.py            # Configuración y fixtures de pytest
│   ├── test_settings.py       # Configuración de tests (TestSettings)
│   └── test_api/              # Tests de la API
│       └── test_health.py     # Tests del endpoint de health
├── .vscode/                   # Configuración de VS Code
│   ├── settings.json          # Configuración del editor
│   └── tasks.json             # Tareas automatizadas
├── pyproject.toml             # Configuración del proyecto y dependencias (fuente de metadatos)
├── .python-version            # Versión de Python (3.13.1)
├── .tool-versions             # Versiones de herramientas
├── CHANGELOG.md               # Changelog del proyecto
└── README.md                  # Documentación principal
```

## Stack Tecnológico

- **Python**: 3.13.1
- **Framework**: FastAPI para REST API
- **Package Manager**: uv
- **Configuration**: Pydantic Settings
- **Testing**: pytest con soporte asyncio
- **Linting**: ruff
- **Type Checking**: pyright
- **Server**: uvicorn

## Dependencias Clave

### Producción
- `fastapi~=0.124.4` - Web framework
- `uvicorn[standard]~=0.38.0` - Servidor ASGI
- `pydantic~=2.12.5` - Validación de datos
- `pydantic-settings~=2.12.0` - Gestión de configuración
- `starlette~=0.50.0` - ASGI toolkit

## Metadatos Centralizados

### Fuente de Verdad
Todos los metadatos del proyecto (nombre, versión, descripción) se leen dinámicamente desde `pyproject.toml` a través del módulo `_metadata.py`.

### Tests
Los tests de configuración se ubican en `tests/test_settings.py` y usan `TestSettings` que hereda de `Settings` para sobreescribir los valores por defecto del entorno de testing.

### Development
- `ruff~=0.14.9` - Linting y formatting
- `pyright~=1.1.390` - Type checking
- `pytest~=9.0.2` - Testing framework
- `pytest-asyncio~=1.3.0` - Async testing support
- `pytest-cov>=7.0.0` - Coverage reporting
- `httpx~=0.28.0` - HTTP client para testing
- `pip-audit>=2.7.0` - Security vulnerability scanning

## Comandos de Desarrollo

### Setup
```bash
# Instalar dependencias
uv sync

# Instalar solo dependencias de producción
uv sync --no-dev
```

### Ejecución de la Aplicación
```bash
# Ejecutar el servidor
uv run python -m agent_template.main

# O usar el CLI entry point
uv run agent-template
```

### Herramientas de Desarrollo
```bash
# Linting (incluye tanto src como tests)
uv run ruff check src tests
uv run ruff format src tests

# Type checking (incluye tanto src como tests)
uv run pyright

# Testing
uv run pytest                              # Configurado con coverage HTML + logging por defecto

# Testing with Coverage Reports
uv run pytest --cov=src --cov-report=html --cov-report=term  # HTML para desarrollo local

# CI Coverage Reports
uv run pytest --cov=src --cov-report=xml --cov-report=json --cov-report=term  # XML/JSON para CI

# Testing with Specific Markers
uv run pytest -m unit                         # Solo tests unitarios
uv run pytest -m "not slow"                   # Excluir tests lentos

# Dependency Management
uv run pip-audit --dry-run                              # Verificar vulnerabilidades
uv run pip-audit --dry-run --verbose                    # Análisis detallada de vulnerabilidades
uv run pip list --outdated --format=columns            # Verificar actualizaciones
uv run pip list --format=columns                       # Lista de dependencias actuales

# Full check (lint + type + test)
# Usar tarea de VS Code "🔍 Estilo y tipado" o ejecutar comandos secuencialmente
```

## API Endpoints

### Health Check Endpoints
- `GET /` - Health check endpoint en nivel raíz
- `GET /api/v1/health/` - Health check endpoint con versioning

Ambos endpoints retornan:
- `name`: Nombre de la API (desde settings)
- `description`: Descripción de la API (desde settings)
- `version`: Versión de la API (desde settings)
- `status`: Estado del servicio

## Configuración

La configuración se gestiona a través de `src/agent_template/settings.py` usando Pydantic Settings:

- **Servidor**: host, port, debug mode, reload
- **API**: title, description, version
- **Logging**: log level

Las variables de entorno pueden usarse para anular las configuraciones por defecto (case-insensitive).

## Testing

- Los archivos de tests están ubicados en `tests/`
- Usa `pytest` para ejecutar tests
- `conftest.py` provee fixtures para FastAPI test client
- Los tests asíncronos son soportados con `pytest-asyncio`
- Configuration mejorada con logging y coverage

## Code Style

- **Longitud de línea**: 88 caracteres
- **Formatting**: Gestionado por ruff
- **Import sorting**: Gestionado por ruff (isort)
- **Type checking**: Modo estricto con pyright
- **Python version**: Features de 3.13+ disponibles

## VS Code Integration

El proyecto incluye configuración de VS Code:
- **Settings**: Intérprete de Python, formatting, linting, testing
- **Tasks**: Install, run, test, lint, format, type check
- **Extensions**: Recomendado instalar extensión de ruff

## Desarrollo Futuro

La estructura actual soporta:
- Añadir nuevos endpoints de API en `src/agent_template/api/v1/`
- Implementar agentes cuando se integren frameworks
- Extender configuración de middlewares
- Integrar con frameworks de agentes (LangGraph, CrewAI, etc.)

## Tareas Comunes para Agentes de Código

1. **Añadir nuevos endpoints**: Crear nuevos archivos en `src/agent_template/api/v1/`
2. **Cambios de configuración**: Modificar `src/agent_template/settings.py`
3. **Añadir tests**: Crear archivos de tests en `tests/test_api/` siguiendo patrones existentes
4. **Cambios de middlewares**: Modificar `src/agent_template/middleware.py`
5. **Dependencias**: Actualizar `pyproject.toml` y ejecutar `uv sync`

## Manejo de Errores

- Validación automática de modelos de request/response con FastAPI
- Excepciones HTTP para errores de API
- Validación de configuración con Pydantic
- Respuestas de error comprehensivas en endpoints de API

## Logging

- Nivel de log configurable a través de settings
- Uvicorn maneja el logging del servidor
- Listo para implementación de logging específica de la aplicación
- Logging integrado con pytest para tests

## Recursos Adicionales

- [Documentation Official](README.md) - Documentación principal
- [TODO.md](TODO.md) - Tareas pendientes y roadmap
