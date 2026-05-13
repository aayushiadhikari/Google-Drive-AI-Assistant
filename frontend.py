import streamlit as st
import requests

st.title("Google Drive AI Assistant")

user_input = st.chat_input("Ask about files")

if user_input:
    st.write("You:", user_input)

    response = requests.post(
        "http://127.0.0.1:8000/chat",
        json={"message": user_input}
    )

    data = response.json()

    st.write("Generated Drive Query:")
    st.code(data["drive_query"])

    st.write("Files Found:")

    for file in data["files"]:
        if "error" in file:
            st.error(file["error"])
        else:
            st.write(f"📄 {file['name']}")
            st.write(file["webViewLink"])