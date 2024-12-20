from fabric import SerialGroup

# result = Connection(", "ubuntu").run("uname -s", hide=True)
result = SerialGroup("51.210.243.135", "146.59.156.185").run("hostname")
msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
print(msg.format(result))
