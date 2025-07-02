from fastapi import APIRouter, File, UploadFile
from utils.pdf_reader import extract_text_from_pdf
from agents.document_summarizer import run_summary_task
from agents.compliance_checker import check_compliance

router = APIRouter()

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    contents = await file.read()
    text = extract_text_from_pdf(contents)

    summary = run_summary_task(text)
    compliance_issues = check_compliance(text)

    return {
        "summary": summary,
        "compliance_report": compliance_issues
    }
