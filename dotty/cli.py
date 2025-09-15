from dotty.utils.config import load_profile
import click
from rich.console import Console
from dotty.modules.citation import validate_citation
from dotty.modules.ada import generate_disclaimer

console = Console()

@click.group()
def cli():
    pass

@cli.command()
@click.argument("text")
def validate(text):
    result = validate_citation(text)
    style = "green" if result["valid"] else "red"
    console.print(result["message"], style=style)

@cli.command()
@click.option("--jurisdiction", default="CO")
def disclaimer(jurisdiction):
    console.print(generate_disclaimer(jurisdiction))

if __name__ == "__main__":
    cli()

from dotty.utils.config import load_profile
import click
from rich.console import Console
from dotty.modules.citation import validate_citation
from dotty.modules.ada import generate_disclaimer

console = Console()

@click.group()
@click.option("--profile", default="default", help="Config profile name")
@click.pass_context
def cli(ctx, profile):
    ctx.ensure_object(dict)
    ctx.obj["config"] = load_profile(profile)

@cli.command()
@click.argument("text")
@click.pass_context
def validate(ctx, text):
    result = validate_citation(text)
    style = "green" if result["valid"] else "red"
    console.print(result["message"], style=style)

@cli.command()
@click.pass_context
def disclaimer(ctx):
    jurisdiction = ctx.obj["config"].get("jurisdiction", "CO")
    text = generate_disclaimer(jurisdiction)
    console.print(text)
