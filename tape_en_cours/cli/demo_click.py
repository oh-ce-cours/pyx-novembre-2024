import click
from utils import addition, soustraction


@click.command()
@click.argument("num1", type=float)
@click.argument("num2", type=float)
def add(num1, num2):
    """Additionne deux nombres."""
    result = addition(num1, num2)
    print(f"La somme de {num1} et {num2} est {result}")


if __name__ == "__main__":
    add()
