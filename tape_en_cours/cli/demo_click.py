import click

from utils import addition

# ou
# import utils

# # ou
# from utils import *


@click.command()
@click.argument("num1", type=float)
@click.argument("num2", type=float)
def add(num1, num2):
    """Additionne deux nombres."""
    result = utils.addition(num1, num2)
    print(f"La somme de {num1} et {num2} est {result}")


if __name__ == "__main__":
    add()
