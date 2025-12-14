"""Script para abrir documentación de endpoints FastAPI en el navegador."""

import argparse
import os
import sys

import requests
from common import open_with_browser


def validate_server_available(url: str, timeout: int = 5) -> bool:
    """Check if the FastAPI server is running and accessible."""
    try:
        # For docs URLs, check the docs endpoint directly
        if url.endswith("/docs"):
            response = requests.get(url, timeout=timeout)
        else:
            response = requests.get(f"{url}/openapi.json", timeout=timeout)
        return response.status_code == 200
    except requests.RequestException:
        return False


def open_docs_file(file_path: str) -> int:
    """Open a local HTML documentation file."""
    if not os.path.exists(file_path):
        print(f"❌ Error: Archivo no encontrado: {file_path}")
        return 1

    if not open_with_browser(file_path):
        print(
            "❌ Error: No se pudo abrir el archivo de documentación en ningún navegador disponible"
        )
        return 1

    print("✅ Documentación abierta en navegador por defecto")
    return 0


def open_docs_url(url: str) -> int:
    """Open FastAPI documentation URL in browser."""
    if not validate_server_available(url):
        print(f"❌ Error: Servidor no disponible en {url}")
        print("💡 Asegúrate de que el servidor FastAPI esté corriendo")
        print("💡 Sugerencia: uv run python -m agent_template.main")
        return 1

    if not open_with_browser(url):
        print(
            "❌ Error: No se pudo abrir la documentación en ningún navegador disponible"
        )
        return 1

    print(f"✅ Documentación abierta en navegador por defecto en {url}")
    return 0


def main() -> int:
    """Main function with argument parsing."""
    parser = argparse.ArgumentParser(
        description="Abrir documentación de endpoints FastAPI en el navegador",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    group = parser.add_mutually_exclusive_group()

    # URL option
    group.add_argument(
        "--url",
        "-u",
        type=str,
        help="URL específica de la documentación (ej: http://localhost:8080/docs)",
    )

    # Port option
    group.add_argument(
        "--port",
        "-p",
        type=int,
        default=8000,
        help="Puerto del servidor FastAPI (default: 8000)",
    )

    # File option
    group.add_argument(
        "--file", "-f", type=str, help="Archivo HTML local con la documentación"
    )

    args = parser.parse_args()

    # Determine what to open
    if args.url:
        return open_docs_url(args.url)
    elif args.file:
        return open_docs_file(args.file)
    else:
        # Default: localhost:8000/docs
        default_url = f"http://localhost:{args.port}/docs"
        return open_docs_url(default_url)


if __name__ == "__main__":
    sys.exit(main())
