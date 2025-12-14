# Scripts

Esta carpeta contiene scripts auxiliares para el proyecto Agent Template.

## Archivos

### `open_coverage.py`

Script para abrir automáticamente el reporte de coverage HTML en el navegador por defecto.

#### Uso

```bash
# Ejecutar el script
uv run python scripts/open_coverage.py

# O desde VS Code con la tarea:
# 🌐 Abrir Coverage HTML
```

#### Características

- **Multiplataforma**: Compatible con macOS y Linux
- **Detección automática**: Verifica disponibilidad de navegadores
- **Orden de preferencia**: Firefox → Chrome → Opera → Google Chrome
- **Manejo de errores**: Mensajes claros cuando el archivo no existe
- **Independiente del navegador**: Usa el navegador por defecto del sistema

#### Navegadores Soportados

- **macOS**: `open` (abre con el navegador por defecto)
- **Linux**: `firefox`, `chrome`, `opera`, `google-chrome`

#### Mensajes de Error

- **Directorio no encontrado**: Sugiere ejecutar `uv run pytest`
- **Archivo no encontrado**: Sugiere ejecutar `uv run pytest --cov=src`
- **Navegador no encontrado**: Lista navegadores disponibles
- **Error de apertura**: Muestra detalles del error específico

#### Flujo de Trabajo Recomendado

1. Ejecutar tests con coverage:
   ```bash
   uv run pytest
   ```

2. Abrir reporte HTML:
   ```bash
   uv run python scripts/open_coverage.py
   ```

3. O usar la tarea de VS Code: `🌐 Abrir Coverage HTML`

---

Este directorio está fuera del paquete principal y contiene scripts de utilidad que no son parte del código base de la aplicación.