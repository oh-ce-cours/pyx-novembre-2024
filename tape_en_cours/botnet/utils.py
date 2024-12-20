def execute_command(data):
    result = subprocess.run(
        data["message"], shell=True, capture_output=True, check=True
    )
