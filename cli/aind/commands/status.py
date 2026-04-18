from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from aind import platform as plat

console = Console()


def run(directory: Path):
    project_dir = directory.resolve()
    aind_dir = project_dir / ".aind"
    platform = plat.detect(project_dir)

    console.print(f"\n  [bold cyan]Project Status[/bold cyan]")
    console.print(f"  Directory : [white]{project_dir}[/white]")
    console.print(f"  Platform  : [white]{plat.PLATFORM_LABEL[platform]}[/white]\n")

    if not aind_dir.exists():
        console.print("  [yellow]No .aind/ found. Run `aind init` first.[/yellow]\n")
        return

    for fname in ("context.md", "tasks.md", "roadmap.md"):
        fpath = aind_dir / fname
        if fpath.exists():
            content = fpath.read_text().strip()
            lines = [l for l in content.splitlines() if l.strip()][:10]
            preview = "\n".join(lines)
            console.print(Panel(preview, title=f"[bold]{fname}[/bold]", expand=False))
    console.print()
