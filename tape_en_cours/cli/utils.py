def addition(num1, num2):
    return num1 + num2


def soustraction(num1, num2):
    return num1 - num2


def main():
    print(addition(1, 2) == 3)
    print(soustraction(1, 2) == -1)


data = [0 for _ in range(1000000000)]

if __name__ == "__main__":
    main()
