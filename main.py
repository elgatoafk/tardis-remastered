import os

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"Hello": "World"}

# app.include_router()


if __name__ == "__main__":
    debug_mode = os.getenv('DEBUG_MODE', 'False').lower() == 'true'
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=debug_mode)
