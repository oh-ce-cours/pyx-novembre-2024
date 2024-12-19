try:
    with open("./tape_en_cours/hello_world.py", encoding="utf8") as f:
        lines = f.readlines()
except:
    pass
print("is closed", f.closed)


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
except ZeroDivisionError:
    print("une exception")
finally:
    print("dans finally")
    f.close()

print(f.closed)
