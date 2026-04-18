import httpx
from aind import __version__

VERSION_URL = (
    "https://raw.githubusercontent.com/lufermalgo/ai-for-non-developers/main/cli/aind/VERSION"
)


def _parse(v: str) -> tuple[int, ...]:
    try:
        return tuple(int(x) for x in v.strip().split("."))
    except ValueError:
        return (0, 0, 0)


def check() -> str | None:
    """Return a warning string if a newer version exists, else None."""
    try:
        r = httpx.get(VERSION_URL, timeout=2, follow_redirects=True)
        r.raise_for_status()
        latest = r.text.strip()
        if _parse(latest) > _parse(__version__):
            return (
                f"[yellow]  ⚠  New version available: {latest} "
                f"(you have {__version__}). Run [bold]aind update[/bold].[/yellow]"
            )
    except Exception:
        pass
    return None
