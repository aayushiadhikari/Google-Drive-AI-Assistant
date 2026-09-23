# Google Drive AI Assistant

An AI-powered Google Drive assistant that allows users to search and find files using natural-language queries.

The application uses a Streamlit frontend, FastAPI backend, Groq LLM, and Google Drive API. The user's natural-language request is converted into a valid Google Drive search query using an LLM, and the matching files are retrieved and displayed through the frontend.

---

## Features

- Natural-language search for Google Drive files
- AI-powered Google Drive query generation using Groq LLM
- Google Drive API integration
- FastAPI REST API backend
- Streamlit interactive frontend
- Displays matching file names and Google Drive links
- Secure handling of API credentials
- Simple frontend-backend architecture

---

## Architecture

```text
                User
                  |
                  v
        +-------------------+
        | Streamlit Frontend|
        |    frontend.py    |
        +-------------------+
                  |
                  | POST /chat
                  v
        +-------------------+
        |   FastAPI Backend |
        |    backend.py     |
        +-------------------+
                  |
                  v
        +-------------------+
        |    Groq LLM       |
        |  Query Generation |
        +-------------------+
                  |
                  | Google Drive Query
                  v
        +-------------------+
        |  Google Drive API |
        | drive_service.py  |
        +-------------------+
                  |
                  v
        +-------------------+
        |  Search Results    |
        +-------------------+
                  |
                  v
        Streamlit Frontend

How It Works
The user enters a natural-language request in the Streamlit interface.
The Streamlit frontend sends the user's message to the FastAPI /chat endpoint.
The FastAPI backend sends the request to the Groq LLM.
The Groq LLM converts the natural-language request into a Google Drive API search query.
The generated query is passed to the Google Drive API.
The application retrieves matching files, including their:
File name
File type
Google Drive link
Modified time
The results are returned by the FastAPI backend and displayed in the Streamlit frontend.

Example Queries

The assistant can understand requests such as:
Find PDF files
Find report files
Show files containing invoice
Find Google Docs
Find spreadsheets

The natural-language request is converted into a Google Drive API query before searching the Drive.

## Tech Stack

Frontend
  Streamlit
Backend
  FastAPI
  Uvicorn
AI / LLM
  Groq
  Llama 3.1 8B Instant
  LangChain Groq
APIs & Services
  Google Drive API
  Google Authentication
Programming Language
  Python
Other Libraries
  Requests
  python-dotenv

## Project Structure

TailorTalk_Assignment/
│
├── backend.py
├── frontend.py
├── drive_service.py
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md

File Description

| File               | Description                                    |
| ------------------ | ---------------------------------------------- |
| `frontend.py`      | Streamlit-based user interface                 |
| `backend.py`       | FastAPI backend and LLM-based query generation |
| `drive_service.py` | Google Drive API integration and file search   |
| `requirements.txt` | Python dependencies                            |
| `.gitignore`       | Prevents sensitive files from being committed  |
| `.env.example`     | Example environment variable configuration     |
| `README.md`        | Project documentation                          |

Backend API

The application provides a FastAPI endpoint:

POST /chat

The endpoint accepts a natural-language message.

Example Request
{
  "message": "Find PDF files"
}

Response

The backend returns:

Original user message
Generated Google Drive query
Matching Google Drive files

Example response structure:
{
  "user_message": "Find PDF files",
  "drive_query": "mimeType='application/pdf'",
  "files": []
}

Installation
1. Clone the Repository
git clone https://github.com/aayushiadhikari/TailorTalk_Assignment.git

Navigate to the project directory:
cd TailorTalk_Assignment

2. Install Dependencies

Install the required Python packages:
pip install -r requirements.txt

Configuration

The application requires:

Groq API key
Google service account credentials with Google Drive access

Groq API Key

Create a .env file in the project root:
GROQ_API_KEY=your_groq_api_key_here

Google Service Account

Place the Google service account credentials file in the project root:
service_account.json

The service account must have access to the Google Drive files that need to be searched.

Running the Application

The application consists of two components:

FastAPI backend
Streamlit frontend

Start the Backend
Open a terminal in the project directory and run:
uvicorn backend:app --reload

The backend will start at:
http://127.0.0.1:8000

You can also check the backend using:
http://127.0.0.1:8000/

Start the Frontend
Open a second terminal in the same project directory and run:
streamlit run frontend.py

The Streamlit application will open in your browser.

Environment & Security
Sensitive credentials are intentionally excluded from the GitHub repository.

The following files should not be committed:
.env
service_account.json

These files are included in .gitignore.

Never upload:
Groq API keys
Google service account credentials
Private authentication information

The .env.example file is provided only as a template for configuring the required environment variable.

## API Flow

Natural Language Request
          |
          v
      Streamlit
          |
          v
      FastAPI /chat
          |
          v
       Groq LLM
          |
          v
Google Drive Search Query
          |
          v
    Google Drive API
          |
          v
     Matching Files
          |
          v
      Streamlit UI

## Key Components

Streamlit Frontend
The frontend provides a simple chat-based interface where users can enter requests about their Google Drive files.

FastAPI Backend
The backend exposes the /chat API endpoint and handles the application logic between the frontend, LLM, and Google Drive service.

Groq LLM
The Groq-powered LLM converts natural-language requests into Google Drive API query syntax.

Google Drive API
The Google Drive API performs the actual file search using the generated query and returns matching file information.

Future Improvements

Possible future enhancements include:
  Conversation history
  More advanced natural-language query handling
  File-type and date filters
  Improved error handling
  Authentication for multiple users
  File preview support
  Deployment of the frontend and backend
  Support for additional Google Workspace services

License
This project is intended for educational and demonstration purposes.
