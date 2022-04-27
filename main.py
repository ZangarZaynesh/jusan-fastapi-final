from posixpath import split
from re import I
from typing import Optional
from fastapi import FastAPI, Header
from pydantic import BaseModel

class Item(BaseModel):
    element: Optional[str] = None

app = FastAPI()

@app.get("/sum1n/{item_n}")
def read_root(item_n: int):
    result = 0
    for x in range(1, item_n + 1):
        result += x
    return {"result": result}

@app.get("/fibo")
async def fibo(n: int=0):
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if n <= 0:
        return {"result": n1}
        # if there is only one term, return n1
    elif n == 1:
        return {"result": n1}
        # generate fibonacci sequence
    else:
        while count < n-2:
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1
        return {"result": nth}


@app.post("/reverse")
async def reverse(string: Optional[str] = Header(None)):
    return {"result": string[::-1]}

array = []
@app.put("/list")
async def update(element: Item):
    array.append(element.element)

@app.get("/list")
async def showArray():
    return {"result": array}

class ItemCalc(BaseModel):
    expr: str

@app.post("/calculator")
async def calculator(expr: ItemCalc):
    arr = expr.expr.split(",")
    syntax = "".join(arr)
    return {"result": eval(syntax)}
