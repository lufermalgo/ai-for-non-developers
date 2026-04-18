import typer
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich import print as rprint
from aind import platform as plat, registry

console = Console()

app = typer.Typer(help="Manage skills from the registry.")


@app.command("list")
def list_cmd(
    layer: str = typer.Option(None, "--layer", "-l", help="verified | community"),
):
    """List available skills from the registry."""
    console.print("\n  [bold cyan]Fetching registry...[/bold cyan]")
    skills = registry.list_skills(layer)  # type: ignore[arg-type]
    if not skills:
        rprint("  [yellow]No skills found.[/yellow]\n")
        return

    table = Table(show_header=True, header_style="bold", box=None, padding=(0, 2))
    table.add_column("Name")
    table.add_column("Layer")
    table.add_column("Platforms")
    table.add_column("Description")

    for s in skills:
        platforms = ", ".join(s.get("platforms", []))
        layer_color = "green" if s["layer"] == "verified" else "yellow"
        table.add_row(
            f"[bold]{s['name']}[/bold]",
            f"[{layer_color}]{s['layer']}[/{layer_color}]",
            platforms,
            s.get("description", ""),
        )

    console.print(table)
    console.print()


@app.command("add")
def add_cmd(
    name: str = typer.Argument(..., help="Skill name to install"),
    platform_name: str = typer.Option(None, "--platform", "-p", help="Target platform"),
    global_: bool = typer.Option(False, "--global", "-g", help="Install globally"),
):
    """Install a skill from the registry."""
    if platform_name:
        try:
            platform = plat.Platform(platform_name)
        except ValueError:
            rprint(f"[red]Unknown platform: {platform_name}[/red]")
            raise typer.Exit(1)
    else:
        platform = plat.detect()

    if global_:
        dest_dir = plat.skills_dir(platform)
    else:
        dest_dir = Path(".claude") / "skills" if platform == plat.Platform.CLAUDE_CODE else Path(".ai") / "skills"

    console.print(f"\n  Installing [bold]{name}[/bold] → {dest_dir}")
    try:
        dest = registry.install_skill(name, dest_dir)
        console.print(f"  [green]✓[/green] {dest}\n")
    except ValueError as e:
        rprint(f"  [red]✗[/red] {e}\n")
        raise typer.Exit(1)
    except Exception as e:
        rprint(f"  [red]✗[/red] Failed to install: {e}\n")
        raise typer.Exit(1)


@app.command("remove")
def remove_cmd(
    name: str = typer.Argument(..., help="Skill name to remove"),
    platform_name: str = typer.Option(None, "--platform", "-p"),
    global_: bool = typer.Option(False, "--global", "-g"),
):
    """Remove an installed skill."""
    if platform_name:
        try:
            platform = plat.Platform(platform_name)
        except ValueError:
            rprint(f"[red]Unknown platform: {platform_name}[/red]")
            raise typer.Exit(1)
    else:
        platform = plat.detect()

    if global_:
        dest_dir = plat.skills_dir(platform)
    else:
        dest_dir = Path(".claude") / "skills" if platform == plat.Platform.CLAUDE_CODE else Path(".ai") / "skills"

    removed = registry.remove_skill(name, dest_dir)
    if removed:
        console.print(f"  [green]✓[/green] Removed [bold]{name}[/bold] from {dest_dir}\n")
    else:
        rprint(f"  [yellow]Skill '{name}' not found in {dest_dir}[/yellow]\n")
