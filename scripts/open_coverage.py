"""Script para abrir el reporte de coverage HTML en el navegador."""

import os
import subprocess
import sys

from common import get_browsers


def open_coverage_html() -> int:
    """Abrir el reporte de coverage HTML en el navegador por defecto."""
    coverage_file = "htmlcov/index.html"

    # Verificar que existe el directorio y el archivo
    if not os.path.exists("htmlcov/"):
        print("❌ Error: Directorio htmlcov/ no encontrado. Ejecuta los tests primero.")
        print("💡 Sugerencia: uv run pytest")
        return 1

    if not os.path.exists(coverage_file):
        print(f"❌ Error: Archivo de coverage no encontrado en {coverage_file}")
        print("💡 Sugerencia: uv run pytest --cov=src")
        return 1

    # Obtener lista de navegadores en orden de preferencia
    browsers = get_browsers()

    # Intentar abrir con cada navegador hasta que uno funcione
    for browser in browsers:
        try:
            # En macOS y Linux, usamos which para verificar disponibilidad
            subprocess.run(
                ["which", browser], check=True, capture_output=True, text=True
            )

            # Intentar el archivo
            subprocess.run([browser, coverage_file])

            print(f"✅ Coverage HTML abierto en {browser}")
            return 0

        except (subprocess.CalledProcessError, FileNotFoundError, OSError):
            # Navegador no encontrado, intentar con el siguiente
            print(f"⚠️ {browser} no encontrado, intentando con siguiente...")
            continue
        except Exception as e:
            print(f"❌ Error al abrir con {browser}: {e}")
            continue

    print(
        "❌ Error: No se pudo abrir el archivo de coverage HTML en ningún navegador disponible"
    )
    print("💡 Asegúrate de que los navegadores estén instalados:")
    for browser in browsers:
        print(f"   - {browser}")

    return 1


def main() -> int:
    """Función principal del script."""
    return open_coverage_html()


if __name__ == "__main__":
    sys.exit(main())
