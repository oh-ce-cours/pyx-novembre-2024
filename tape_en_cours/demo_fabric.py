from fabric import ParallelGroup

# result = Connection(", "ubuntu").run("uname -s", hide=True)
result = ParallelGroup("51.210.243.135", "146.59.156.185", user="ubuntu").run(
    "hostname", hide=True
)
for item in result.items():
    print(item)
# msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
# print(msg.format(result))
