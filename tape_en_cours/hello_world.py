import pandas

print("hello world")
print(1 == 2)


def fizzbuzz() -> int:
    for nombre in range(1, 101):
        resultat = ""
        if nombre % 3 == 0:
            resultat = resultat + "fizz"
        if nombre % 5 == 0:
            resultat += "buzz"
        if resultat == "":
            resultat = nombre
        return resultat

