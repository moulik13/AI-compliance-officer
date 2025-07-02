from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
import tempfile
import os

from services.transcribe import convert_to_wav, transcribe_audio
from agents.document_summarizer import run_summary_task
from agents.compliance_checker import check_compliance

router = APIRouter()

@router.post("/upload-audio/", summary="Upload audio and get transcription + compliance report")
async def upload_audio(file: UploadFile = File(...)):
    try:
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=file.filename) as temp_file:
            temp_file.write(await file.read())
            uploaded_path = temp_file.name

        # Convert and transcribe
        wav_path = convert_to_wav(uploaded_path)
        transcription = transcribe_audio(wav_path)

        # Run through agents
        summary = run_summary_task(str(transcription))
        compliance_issues = check_compliance(str(transcription))

        # Clean up
        os.remove(uploaded_path)
        os.remove(wav_path)

        # ✅ Use FastAPI auto-serialization
        return {
            "transcription": transcription,
            "summary": summary,
            "compliance_report": compliance_issues
        }

    except Exception as e:
        print("ERROR:", e)
        return JSONResponse(status_code=500, content={"error": str(e)})
