from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]

SERVICE_ACCOUNT_FILE = "service_account.json"

creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)

service = build("drive", "v3", credentials=creds)


def search_drive_files(query):
    try:
        results = service.files().list(
            q=query,
            fields="files(id, name, mimeType, webViewLink, modifiedTime)",
            pageSize=10
        ).execute()

        files = results.get("files", [])

        return files

    except Exception as e:
        return [{"error": str(e)}]