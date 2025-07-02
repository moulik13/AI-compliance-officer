import streamlit as st
import requests

# Title
st.title("AI Compliance Officer")

# Description
st.markdown("""
Welcome to the AI Compliance Officer.  
Upload a document or audio file to analyze for:
- Transcription (for audio)
- Summary
- Compliance issues
""")

# Toggle between Document and Audio
option = st.radio("Select input type:", ("Document", "Audio"))

# File uploader
if option == "Document":
    file = st.file_uploader("Upload PDF Document", type=["pdf"])
    endpoint = "http://127.0.0.1:8000/upload"
else:
    file = st.file_uploader("Upload Audio File", type=["wav", "mp3", "m4a"])
    endpoint = "http://127.0.0.1:8000/upload-audio/"

# Submit and fetch results
if file and st.button("Submit"):
    try:
        files = {"file": (file.name, file, file.type)}
        response = requests.post(endpoint, files=files)

        if response.status_code == 200:
            result = response.json()

            if "transcription" in result:
                st.subheader("Transcription")
                st.markdown(result["transcription"])

            st.subheader("Summary")
            st.markdown(result["summary"])

            st.subheader("Compliance Report")
            st.markdown(result["compliance_report"])

        else:
            st.error(f"Server error: {response.status_code} — {response.text}")
    except Exception as e:
        st.error(f"Request failed: {e}")
