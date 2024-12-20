print("hello world")
print(1 == 2)


def fizzbuzz():
    for nombre in range(1, 101):
        if nombre % 3 == 0:
            print("fizz")
        elif nombre % 5 == 0:
            print("buzz")
        elif nombre % 3 == 0 and nombre % 5 == 0:
            print("fizzbuzz")
        else:
            print(nombre)

        # resultat = ""
        # if nombre % 3 == 0:
        #     resultat = resultat + "fizz"
        # if nombre % 5 == 0:
        #     resultat += "buzz"
        # if resultat == "":
        #     resultat = nombre
        # return resultat


fizzbuzz()
