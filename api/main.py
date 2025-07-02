from fastapi import FastAPI
from api.routes.upload import router as upload_router
from api.routes.upload_audio import router as upload_audio_router

app = FastAPI()
app.include_router(upload_router)
app.include_router(upload_audio_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Compliance Officer API. Visit /docs for Swagger UI."}
