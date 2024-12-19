f = open("./tape_en_cours/hello_world.py", encoding="utf8")
lines = f.readlines()
f.close()


def output(content):
    for line in content:
        print(line, end="")


def head(content: list[str]) -> list[str]:
    return content[:10]


def tail(content: list[str]) -> list[str]:
    return content[-10:]


output(head(lines))
