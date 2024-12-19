f = open("./tape_en_cours/hello_world.py", encoding="utf8")
lines = f.readlines()
f.close()


def output(lines):
    for line in lines:
        print(line, end="")


def head(c: list[str]) -> list[str]:
    return lines[:10]


def tail(lines: list[str]) -> list[str]:
    return lines[-10:]
