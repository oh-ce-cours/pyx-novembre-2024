import os

print(os.system("ls"))

#############

import subprocess

output = subprocess.run(["ls", "-l"])
print(output)
