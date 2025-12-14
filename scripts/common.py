"""Funciones comunes reutilizadas entre scripts de la carpeta scripts."""

import platform
import subprocess


def get_browsers() -> list[str]:
    """Get list of browsers in order of preference."""
    if platform.system() == "Darwin":  # macOS
        return ["open"]
    else:  # Linux y otros sistemas tipo Unix
        # Prioritarios: firefox, chrome, opera
        return ["firefox", "chrome", "opera", "google-chrome"]


def open_with_browser(file_path_or_url: str) -> bool:
    """Open file or URL in default browser."""
    browsers = get_browsers()

    for browser in browsers:
        try:
            # Verificar disponibilidad del navegador
            subprocess.run(
                ["which", browser], check=True, capture_output=True, text=True
            )

            # Intentar el archivo o URL
            subprocess.run([browser, file_path_or_url])
            return True

        except (subprocess.CalledProcessError, FileNotFoundError, OSError):
            # Navegador no encontrado, intentar con el siguiente
            continue
        except Exception:
            continue

    return False
