import os
from PyPDF2 import PdfReader
from docx import Document
from backend.settings import get_settings

settings = get_settings()
UPLOAD_DIR = settings.UPLOAD_FOLDER
os.makedirs(UPLOAD_DIR, exist_ok=True)


def save_upload_file(upload_file, destination):
    with open(destination, "wb") as buffer:
        buffer.write(upload_file.file.read())


def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def extract_text_from_docx(file_path):
    doc = Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text


def handle_upload(upload_file):
    filename = upload_file.filename
    file_path = os.path.join(UPLOAD_DIR, filename)
    save_upload_file(upload_file, file_path)
    if filename.lower().endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    elif filename.lower().endswith(".docx"):
        text = extract_text_from_docx(file_path)
    else:
        text = ""
    return {"filename": filename, "text": text}
