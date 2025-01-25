from fastapi import FastAPI
from fastapi.testclient import TestClient
from starlette.testclient import TestClient
app = FastAPI()

@app.get("/")
async def read_main():
    return {"msg": "FIN TOYIN DEMO DEVOPS"}
client = TestClient(app)


