from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from app.utils import analyze_rooftop_image

app = FastAPI(title="Solar Industry AI Assistant")

@app.post("/analyze/")
async def analyze_image(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        result = analyze_rooftop_image(contents)
        return JSONResponse(content=result)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
