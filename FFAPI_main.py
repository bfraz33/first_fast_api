from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():

    return{"Connected to your first api✅! Welcome to FastApi!!"}
