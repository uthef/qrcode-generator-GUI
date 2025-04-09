from pathlib import Path

QR_CODES_DIR = "QR-Codes"
TEMP_DIR = "temp"


@staticmethod
def make_sure_directory_exists(dir):
    path = Path(dir)

    if not path.exists():
        path.mkdir()
