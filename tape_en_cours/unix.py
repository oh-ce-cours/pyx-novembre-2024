f = open("./tape_en_cours/hello_world.py", encoding="utf8")
lines = f.readlines()
f.close()


def output(content):
    for line in content:
        print(line, end="")


def file_output(content, filename):
    with open(filename, "w", encoding="utf8") as f:
        f.writelines(content)


def head(content):
    return content[:10]


def tail(content: list[str]) -> list[str]:
    return content[-10:]


file_output(head(lines), filename="./output.txt")
