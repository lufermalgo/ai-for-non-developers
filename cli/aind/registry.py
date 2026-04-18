import shutil
import httpx
from pathlib import Path
from typing import Literal

REGISTRY_BASE = (
    "https://raw.githubusercontent.com/lufermalgo/ai-for-non-developers/main"
    "/skills/skill-registry"
)
GITHUB_API_BASE = (
    "https://api.github.com/repos/lufermalgo/ai-for-non-developers/contents"
    "/skills/skill-registry"
)

Layer = Literal["verified", "community"]


def _fetch_index(layer: Layer) -> list[dict]:
    url = f"{REGISTRY_BASE}/{layer}/index.json"
    try:
        r = httpx.get(url, timeout=10, follow_redirects=True)
        r.raise_for_status()
        return r.json().get("skills", [])
    except Exception:
        return []


def list_skills(layer: Layer | None = None) -> list[dict]:
    layers: list[Layer] = ["verified", "community"] if layer is None else [layer]
    skills = []
    for l in layers:
        for s in _fetch_index(l):
            skills.append({**s, "layer": l})
    return skills


def find_skill(name: str) -> dict | None:
    for s in list_skills():
        if s["name"] == name:
            return s
    return None


def _download_folder(api_url: str, dest_dir: Path) -> None:
    """Recursively download a GitHub folder via the Contents API."""
    r = httpx.get(api_url, timeout=15, follow_redirects=True,
                  headers={"Accept": "application/vnd.github+json"})
    r.raise_for_status()
    entries = r.json()
    for entry in entries:
        if entry["type"] == "file":
            file_dest = dest_dir / entry["name"]
            file_dest.parent.mkdir(parents=True, exist_ok=True)
            content_r = httpx.get(entry["download_url"], timeout=15, follow_redirects=True)
            content_r.raise_for_status()
            file_dest.write_bytes(content_r.content)
        elif entry["type"] == "dir":
            _download_folder(entry["url"], dest_dir / entry["name"])


def install_skill(name: str, dest_dir: Path) -> Path:
    skill = find_skill(name)
    if not skill:
        raise ValueError(f"Skill '{name}' not found in registry.")

    layer = skill["layer"]
    skill_dest = dest_dir / name
    if skill_dest.exists():
        shutil.rmtree(skill_dest)
    skill_dest.mkdir(parents=True, exist_ok=True)

    api_url = f"{GITHUB_API_BASE}/{layer}/{name}"
    _download_folder(api_url, skill_dest)
    return skill_dest


def remove_skill(name: str, dest_dir: Path) -> bool:
    target = dest_dir / name
    if target.exists() and target.is_dir():
        shutil.rmtree(target)
        return True
    return False
