from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from fastapi.responses import JSONResponse
from backend.app.services.document_parser import handle_upload

router = APIRouter()


@router.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    result = handle_upload(file)
    return result


@router.post("/generate-curriculum")
async def generate_curriculum():
    return {"curriculum": []}


@router.post("/ask-question")
async def ask_question(question: str):
    return {"answer": "This is a sample answer to your question."}


@router.post("/track-progress")
async def track_progress(score: int = Form(...)):
    return {"status": "Progress tracked."}


@router.post("/generate-quiz")
async def generate_quiz(ques: int = Form(...)):
    return {"quiz": "This is a sample quiz with {ques} questions."}


@router.get("/progress-summary")
async def progress_summary():
    return {"summary": "This is a sample progress summary."}
