import argparse
from utils import addition


def main():
    parser = argparse.ArgumentParser(description="Additionne deux nombres.")
    parser.add_argument("num1", type=float, help="Le premier nombre")
    parser.add_argument("num2", type=float, help="Le deuxième nombre")

    args = parser.parse_args()

    result = addition(args.num1, args.num2)
    print(f"La somme de {args.num1} et {args.num2} est {result}")


if __name__ == "__main__":
    main()
