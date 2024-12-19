f = open("./tape_en_cours/hello_world.py", encoding="utf8")
lines = f.readlines()
f.close()
for line in lines[:10]:
    print(line, end="")
