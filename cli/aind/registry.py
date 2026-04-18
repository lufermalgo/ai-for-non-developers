import httpx
from pathlib import Path
from typing import Literal

REGISTRY_BASE = (
    "https://raw.githubusercontent.com/lufermalgo/ai-for-non-developers/main"
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


def fetch_skill_content(skill: dict) -> str:
    url = skill.get("url") or f"{REGISTRY_BASE}/{skill['layer']}/{skill['name']}.md"
    r = httpx.get(url, timeout=10, follow_redirects=True)
    r.raise_for_status()
    return r.text


def find_skill(name: str) -> dict | None:
    for s in list_skills():
        if s["name"] == name:
            return s
    return None


def install_skill(name: str, dest_dir: Path) -> Path:
    skill = find_skill(name)
    if not skill:
        raise ValueError(f"Skill '{name}' not found in registry.")
    dest_dir.mkdir(parents=True, exist_ok=True)
    content = fetch_skill_content(skill)
    dest = dest_dir / f"{name}.md"
    dest.write_text(content)
    return dest


def remove_skill(name: str, dest_dir: Path) -> bool:
    target = dest_dir / f"{name}.md"
    if target.exists():
        target.unlink()
        return True
    return False
