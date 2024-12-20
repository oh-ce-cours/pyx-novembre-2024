from fabric import Connection

result = Connection("51.210.243.135", "ubuntu").run("uname -s", hide=True)
msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
print(msg.format(result))
