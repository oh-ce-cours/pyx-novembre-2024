import click


@click.group()
def cli():
    pass


@click.command()
@click.argument("filename")
@click.option("--lines", default=10, help="Number of lines to display")
def head(filename, lines):
    with open(filename, encoding="utf8") as f:
        content = f.readlines()
    output(content[:lines])


@click.command()
@click.argument("filename")
@click.option("--lines", default=10, help="Number of lines to display")
def tail(filename, lines):
    with open(filename, encoding="utf8") as f:
        content = f.readlines()
    output(content[-lines:])


def output(content):
    for line in content:
        print(line, end="")


cli.add_command(head)
cli.add_command(tail)

if __name__ == "__main__":
    cli()
