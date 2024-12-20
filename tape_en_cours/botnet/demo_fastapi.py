import utils
from fastapi import FastAPI

app = FastAPI()


@app.get("/actions/")
async def read_item(command: dict):
    args, return_code, result = utils.execute_command(command)
    return {"executed_command": args, "return_code": return_code, "result": result}
