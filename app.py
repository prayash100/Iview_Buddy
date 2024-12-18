from flask import Flask, render_template, request
import google.generativeai as genai
import PyPDF2
import os
from docx import Document  # Import for DOCX file handling
import re

# Initialize Flask app
app = Flask(__name__)





from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Configure the Bard API
genai.configure()  # Replace with your actual API key






model = genai.GenerativeModel("gemini-1.5-flash")

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

# Function to extract text from DOCX
def extract_text_from_docx(docx_file):
    doc = Document(docx_file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text



def generate_ats_score_and_questions(job_description, resume):
    prompt = f"""
    You are an AI system evaluating how well a candidate's resume matches a job description. Based on the following job description and the candidate's resume, calculate an ATS score (0-100) to represent how well the resume fits the job description. Provide an explanation of the key areas where the resume matches or falls short.

    Job Description:
    {job_description}

    Candidate Resume:
    {resume}

    After calculating the ATS score, also generate 5 thoughtful, personalized interview questions that can help assess the candidate's qualifications based on the job description and resume.
    """
    response = model.generate_content(prompt)
    return response.text


# Home route
@app.route("/", methods=["GET", "POST"])
def home():
    ats_score = None
    matched_keywords = None
    questions = None

    if request.method == "POST":
        job_description = request.form["job_description"]
        resume_file = request.files.get("resume")

        if resume_file:
            resume_filename = resume_file.filename
            resume_path = os.path.join("uploads", resume_filename)
            resume_file.save(resume_path)

            # Extract text based on file type (PDF or DOCX)
            if resume_filename.lower().endswith('.pdf'):
                resume_text = extract_text_from_pdf(resume_path)
            elif resume_filename.lower().endswith('.docx'):
                resume_text = extract_text_from_docx(resume_path)
            else:
                resume_text = "Unsupported file format."
        else:
            resume_text = "No resume uploaded."

        # Generate interview questions based on the job description and resume
        questions = generate_ats_score_and_questions(job_description, resume_text)

    return render_template(
        "index.html",
        ats_score=ats_score,
        matched_keywords=matched_keywords,
        questions=questions
    )

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
