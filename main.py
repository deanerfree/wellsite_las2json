from fastapi import FastAPI
from routers import las2json

app = FastAPI()
mock_file = "data/mockdata.las"

@app.get("/")
async def root():
    return {"message": "Welcome to my LAS to JSON converter"}


# mockdata = open_file(mock_file)
app.include_router(las2json.router)