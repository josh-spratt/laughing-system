import click


@click.group()
def cli():
    pass


@cli.command()
@click.option("-n", "--name", type=str, help="Name to greet", default="world")
def helloworld(name):
    click.echo(f"hello {name}!")
