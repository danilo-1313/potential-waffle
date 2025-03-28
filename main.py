# This file should contain Python code. If you want to run a FastAPI app, ensure the app is defined here.

from fastapi import FastAPI # type: ignore

app = FastAPI()

@app.get("/saudacao/{name}")
def saudacao(name: str):
	return {"message": f"Olá, {name}!"}
