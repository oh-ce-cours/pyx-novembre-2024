print("hello world")
print(1 == 2)

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(format="%(asctime)s %(message)s")
logger.debug("This message should go to the log file")
logger.info("So should this")
logger.warning("And this, too")
logger.error("And non-ASCII stuff, too, like Øresund and Malmö")
logging.warning("%s before you %s", "Look", "leap!")


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
