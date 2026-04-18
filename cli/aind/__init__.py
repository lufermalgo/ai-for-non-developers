from pathlib import Path

_version_file = Path(__file__).parent / "VERSION"
__version__ = _version_file.read_text().strip() if _version_file.exists() else "0.0.0"
