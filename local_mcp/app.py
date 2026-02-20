from fastapi import FastAPI

app = FastAPI(title="Math API")


@app.get("/")
def health():
    return {"status": "Math API running"}


@app.get("/add")
def add(a: float, b: float):
    return {"result": a + b}


@app.get("/subtract")
def subtract(a: float, b: float):
    return {"result": a - b}


@app.get("/multiply")
def multiply(a: float, b: float):
    return {"result": a * b}


@app.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        return {"error": "Division by zero"}
    return {"result": a / b}