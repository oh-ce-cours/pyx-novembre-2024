import subprocess


def execute_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, check=True)
    return result.args, result.returncode, result.stdout.decode()


if __name__ == "__main__":
    result = execute_command("ls -la")
    print(result)
