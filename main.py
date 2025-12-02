# from fastapi import FastAPI, File, UploadFile, Form, HTTPException
# from pydantic import BaseModel, Json
# import shutil
# import os
import core.mock_api
import uvicorn
# import json
# from typing import List 
from fastapi import FastAPI, Body

app = FastAPI()

@app.post("/flureg")
async def get_raw_json(payload: dict = Body(...)):
    
    
    result = core.mock_api.generate_mock(payload)

    
    return result

if __name__ == "__main__":
    # uvicorn.run(app, host="0.0.0.0", port=5000)
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        # workers=100,  # จำนวน worker processes
        # reload=False
    )