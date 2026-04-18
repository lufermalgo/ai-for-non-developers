from pathlib import Path
from enum import Enum


class Platform(str, Enum):
    CLAUDE_CODE = "claude-code"
    GEMINI_CLI = "gemini-cli"
    OPENCODE = "opencode"
    OTHER = "other"


PLATFORM_RULE_FILE = {
    Platform.CLAUDE_CODE: "CLAUDE.md",
    Platform.GEMINI_CLI: "GEMINI.md",
    Platform.OPENCODE: "AGENTS.md",
    Platform.OTHER: "AGENTS.md",
}

PLATFORM_SKILLS_SUBDIR = {
    Platform.CLAUDE_CODE: ".claude/skills",
    Platform.GEMINI_CLI: ".gemini/skills",
    Platform.OPENCODE: ".opencode/skills",
    Platform.OTHER: ".ai/skills",
}

PLATFORM_LABEL = {
    Platform.CLAUDE_CODE: "Claude Code",
    Platform.GEMINI_CLI: "Gemini CLI",
    Platform.OPENCODE: "OpenCode",
    Platform.OTHER: "Other",
}


def was_detected_from_file(project_dir: Path = Path(".")) -> bool:
    """True if a platform rule file already exists in the project directory."""
    return any((project_dir / f).exists() for f in ("CLAUDE.md", "GEMINI.md", "AGENTS.md"))


def detect(project_dir: Path = Path(".")) -> Platform:
    """Detect active AI platform from existing rule files or installed binaries."""
    if (project_dir / "CLAUDE.md").exists():
        return Platform.CLAUDE_CODE
    if (project_dir / "GEMINI.md").exists():
        return Platform.GEMINI_CLI
    if (project_dir / "AGENTS.md").exists():
        return Platform.OPENCODE

    import shutil
    if shutil.which("claude"):
        return Platform.CLAUDE_CODE
    if shutil.which("gemini"):
        return Platform.GEMINI_CLI
    if shutil.which("opencode"):
        return Platform.OPENCODE

    return Platform.OTHER


def project_skills_dir(project_dir: Path = Path(".")) -> Path:
    """Return the skills directory for the current project, or raise if not in a project."""
    platform = detect(project_dir)
    if not was_detected_from_file(project_dir):
        raise RuntimeError("Not in an aind project. Run `aind init` first.")
    return project_dir / PLATFORM_SKILLS_SUBDIR[platform]


def rule_file(platform: Platform) -> str:
    return PLATFORM_RULE_FILE[platform]
