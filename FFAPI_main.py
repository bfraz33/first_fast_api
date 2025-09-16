from fastapi import FastAPI # Importing FastApi Library

app = FastAPI() # Establishing webserver object

@app.get("/") # Decorator getting root
def read_root():# Defining Root

    return{"Connected to your first api✅! Welcome to FastApi!!"} # Output
