import utils
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Command(BaseModel):
    command: str


class CommandResult(BaseModel):
    executed_command: str
    return_code: int
    result: str | None


@app.get("/actions/")
async def read_item(command: Command) -> CommandResult:
    args, return_code, result = utils.execute_command(command)
    return {"executed_command": args, "return_code": return_code, "result": result}
