import subprocess


def execute_command(data):
    result = subprocess.run(
        data["message"], shell=True, capture_output=True, check=True
    )
    return result


if __name__ == "__main__":
    execute_command({"message": "ls -la"})
