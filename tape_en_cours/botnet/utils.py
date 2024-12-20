import subprocess


def execute_command(data):
    result = subprocess.run(
        data["message"], shell=True, capture_output=True, check=True
    )
    return result.args, result.returncode, result.stdout.decode()


if __name__ == "__main__":
    result = execute_command({"message": "ls -la"})
    print(result)
