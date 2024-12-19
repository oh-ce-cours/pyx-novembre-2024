with open("./tape_en_cours/hello_world.py", encoding="utf8") as f:
    lines = f.readlines()
print(f.closed)


def output(content):
    for line in content:
        print(line, end="")


def file_output(content, filename):
    with open(filename, "w", encoding="utf8") as f_handler:
        f_handler.writelines(content)


def head(content):
    return content[:10]


def tail(content: list[str]) -> list[str]:
    return content[-10:]


file_output(head(lines), filename="./output.txt")

try:
    f = open("./output.txt", "r")
    1 / 0
    f.read()
    f.close()
except ZeroDivisionError:
    print("une exception")

print(f.closed)
