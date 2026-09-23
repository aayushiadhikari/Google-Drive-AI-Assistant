from fastapi import FastAPI
from pydantic import BaseModel
from drive_service import search_drive_files
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="qwen/qwen3.8-27b"
)


class ChatRequest(BaseModel):
    message: str


def convert_to_drive_query(user_message):
    prompt = f"""
Convert this user request into a valid Google Drive API q query.

Return only the query string.

Examples:
Find PDF files -> mimeType='application/pdf'
Find report file -> name contains 'report'
Show files containing invoice -> fullText contains 'invoice'
Find docs files -> mimeType='application/vnd.google-apps.document'
Find sheets -> mimeType='application/vnd.google-apps.spreadsheet'

User request:
{user_message}
"""

    response = llm.invoke(prompt)
    return response.content.strip()


@app.get("/")
def home():
    return {"message": "Backend is running"}


@app.post("/chat")
def chat(request: ChatRequest):
    user_message = request.message

    drive_query = convert_to_drive_query(user_message)

    files = search_drive_files(drive_query)

    return {
        "user_message": user_message,
        "drive_query": drive_query,
        "files": files
    }