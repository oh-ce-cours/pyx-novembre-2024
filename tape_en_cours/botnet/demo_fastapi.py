import utils
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.get("/actions/")
async def read_item(command: dict):
    args, return_code, result = utils.execute_command(command)
    return {"executed_command": args, "return_code": return_code, "result": result}
