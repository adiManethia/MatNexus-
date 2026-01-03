import os 
import time 
from google import genai
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

def get_gemini_client():
    """Initializes and returns the Gemini 3 Client."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return None
    return genai.Client(api_key=api_key)

def process_uploaded_pdfs(client, pdf_files):
    """
    Handles the temporary saving, uploading, and processing 
    of multiple PDFs for the Gemini Files API.
    """
    gemini_files = []
    
    for pdf in pdf_files:
        # 1. Save temp file locally to upload
        temp_path = f"temp_{pdf.name}"
        with open(temp_path, "wb") as f:
            f.write(pdf.getbuffer())
        
        # 2. Upload using the correct 'file' argument
        myfile = client.files.upload(file=temp_path)
        
        # 3. Wait for the 'ACTIVE' state
        while myfile.state == "PROCESSING":
            time.sleep(2)
            myfile = client.files.get(name=myfile.name)
            
        if myfile.state == "FAILED":
            continue
            
        gemini_files.append(myfile)
        os.remove(temp_path) # Cleanup
        
    return gemini_files