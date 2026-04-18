import typer
from pathlib import Path
from aind.commands import init, status
from aind.commands.skill import app as skill_app
from aind import platform as plat, __version__
from rich import print as rprint


def version_callback(value: bool):
    if value:
        rprint(f"aind {__version__}")
        raise typer.Exit()


app = typer.Typer(
    name="aind",
    help="AI for Non-Developers — project manager.",
    no_args_is_help=True,
    add_completion=False,
)


@app.callback()
def main(
    version: bool = typer.Option(None, "--version", "-v", callback=version_callback, is_eager=True, help="Show version."),
):
    pass

app.add_typer(skill_app, name="skill")


@app.command(name="init")
def init_cmd(
    directory: Path = typer.Argument(Path("."), help="Project directory (default: CWD)"),
    platform: str = typer.Option(None, "--platform", "-p", help="claude-code | gemini-cli | opencode | other"),
):
    """Initialize a project: deploy rule file + create .aind/ memory."""
    init.run(directory, platform)


@app.command(name="status")
def status_cmd(
    directory: Path = typer.Argument(Path("."), help="Project directory (default: CWD)"),
):
    """Show project state from .aind/."""
    status.run(directory)


@app.command(name="platform")
def platform_cmd():
    """Detect the active AI platform."""
    detected = plat.detect()
    label = plat.PLATFORM_LABEL[detected]
    rule = plat.rule_file(detected)
    skills = plat.skills_dir(detected)
    rprint(f"\n  Platform   : [bold]{label}[/bold]")
    rprint(f"  Rule file  : [white]{rule}[/white]")
    rprint(f"  Skills dir : [white]{skills}[/white]\n")

if __name__ == "__main__":
    app()
