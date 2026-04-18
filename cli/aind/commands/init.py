import typer
import httpx
from pathlib import Path
from rich.console import Console
from rich import print as rprint
from aind import platform as plat

console = Console()

TEMPLATE_URL = (
    "https://raw.githubusercontent.com/lufermalgo/ai-for-non-developers/main"
    "/templates/AGENT.md"
)

AIND_FILES = {
    "context.md": "# Project Context\n\n## Overview\nPending discovery...\n",
    "roadmap.md": "# Roadmap\n\n## Milestones\n- [ ] Initial Setup\n\n## Archive\n",
    "tasks.md": "# Tasks\n\n## Current Focus\n- [ ] Initial discovery\n\n## Done\n",
    "lessons.md": "# Lessons\n",
}


_PLATFORM_CHOICES = [
    (plat.Platform.CLAUDE_CODE, "Claude Code / CoWork"),
    (plat.Platform.GEMINI_CLI, "Gemini CLI / Antigravity"),
    (plat.Platform.OPENCODE, "OpenCode"),
]


def _prompt_platform() -> plat.Platform:
    console.print("\n  [bold]Which AI platform are you using?[/bold]")
    for i, (_, label) in enumerate(_PLATFORM_CHOICES, 1):
        console.print(f"  [cyan]{i}[/cyan]. {label}")
    while True:
        raw = typer.prompt("\n  Enter number", default="1")
        try:
            idx = int(raw) - 1
            if 0 <= idx < len(_PLATFORM_CHOICES):
                return _PLATFORM_CHOICES[idx][0]
        except ValueError:
            pass
        console.print("  [red]Invalid choice. Enter 1, 2, or 3.[/red]")


def run(directory: Path, platform_name: str | None):
    project_dir = directory.resolve()
    project_dir.mkdir(parents=True, exist_ok=True)

    # Detect or use explicit platform
    if platform_name:
        try:
            platform = plat.Platform(platform_name)
        except ValueError:
            rprint(f"[red]Unknown platform: {platform_name}[/red]")
            raise typer.Exit(1)
    else:
        detected = plat.detect(project_dir)
        if detected == plat.Platform.OTHER or not plat.was_detected_from_file(project_dir):
            platform = _prompt_platform()
        else:
            platform = detected

    label = plat.PLATFORM_LABEL[platform]
    rule_file = plat.rule_file(platform)

    console.print(f"\n  [bold cyan]aind[/bold cyan] — initializing project")
    console.print(f"  Directory : [white]{project_dir}[/white]")
    console.print(f"  Platform  : [white]{label}[/white]")
    console.print(f"  Rule file : [white]{rule_file}[/white]\n")

    # Remove stale rule files from other platforms
    for other_rule in {"CLAUDE.md", "GEMINI.md", "AGENTS.md"} - {rule_file}:
        stale = project_dir / other_rule
        if stale.exists():
            stale.unlink()
            console.print(f"  [yellow]✕[/yellow] Removed stale: {other_rule}")

    # Deploy rule file
    dest = project_dir / rule_file
    template_src = Path(__file__).parents[3] / "templates" / "AGENT.md"
    if template_src.exists():
        dest.write_text(template_src.read_text())
    else:
        try:
            r = httpx.get(TEMPLATE_URL, timeout=10, follow_redirects=True)
            r.raise_for_status()
            dest.write_text(r.text)
        except Exception as e:
            rprint(f"[red]Failed to download template: {e}[/red]")
            raise typer.Exit(1)
    console.print(f"  [green]✓[/green] {rule_file}")

    # Initialize .aind/ memory
    aind_dir = project_dir / ".aind"
    (aind_dir / "specs" / "archive").mkdir(parents=True, exist_ok=True)
    for fname, default_content in AIND_FILES.items():
        fpath = aind_dir / fname
        if not fpath.exists() or fpath.stat().st_size == 0:
            fpath.write_text(default_content)
            console.print(f"  [green]✓[/green] .aind/{fname}")

    console.print(f"\n  [bold green]Ready.[/bold green] Open your AI tool and say:")
    console.print(f'  [dim]"I want to build [your idea]. Let\'s start."[/dim]\n')
