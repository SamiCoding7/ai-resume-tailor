from flask import Flask, request, render_template
import google.generativeai as genai
import PyPDF2
import os
from dotenv import load_dotenv

# Setup
load_dotenv("/Users/samiksha/ai-resume-tailor/.env")
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

app = Flask(__name__)

def readFile(filepath):
    with open(filepath, "r") as file:
        return file.read()

def readPdf(filepath):
    with open(filepath, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        strTotal = ""
        for page in reader.pages:
            strTotal += page.extract_text()
    return strTotal

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    job_description = request.form.get("job_description")
    resume_file = request.files.get("resume")
    filename = resume_file.filename

    # Read the resume
    if filename.endswith(".txt"):
        resumeText = resume_file.read().decode("utf-8")
    elif filename.endswith(".pdf"):
        import tempfile
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            resume_file.save(tmp.name)
            resumeText = readPdf(tmp.name)
    else:
        return "Please upload a .txt or .pdf file"

    # Send to Gemini
    chat = model.start_chat()
    response = chat.send_message(f"Give feedback on this resume: {resumeText} where this is the job description: {job_description}. Give it in four sections: 1. A match score as a %, 2. Rewritten bullet points tailored to the job, 3. Skill gaps - what the job wants that the resume is missing, 4. Keywords to add - terms from the job description not in the resume")
    
    feedback = response.text
    return render_template("results.html", feedback=feedback)

if __name__ == "__main__":
    app.run(debug=True)
