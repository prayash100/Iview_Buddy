# Iview Buddy

**Iview Buddy** is a web application designed to help job seekers prepare for interviews by providing personalized interview questions. The app takes a job description and a candidate's resume (in PDF or DOCX format) and generates a list of interview questions based on how well the resume matches the job description.

This application uses **Google Gemini API** to analyze and generate relevant interview questions and ATS scores based on the content in the resume and job description.

## Features
- Upload a job description and a resume (PDF or DOCX format)
- Get personalized interview questions tailored to the job description and resume
- ATS score (0-100) based on how well the resume matches the job description
- Easy-to-use interface with real-time results

## Demo

Check out the live demo of the project here: [Iview Buddy](https://iview-buddy.onrender.com)

## Tech Stack
- **Backend**: Flask
- **AI**: Google Gemini API
- **Frontend**: HTML, CSS
- **Libraries**:
  - `PyPDF2` for PDF handling
  - `python-docx` for DOCX file handling
  - `Flask` for web framework
  - `python-dotenv` for managing environment variables

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/prayash100/Iview_Buddy.git
2. Navigate to the project directory:
   cd Iview_Buddy
3. Install the required dependencies:
   pip install -r requirements.txt
4. Create a .env file in the root directory of the project and add the following content:
   GOOGLE_API_KEY=your_google_gemini_api_key_here
   Replace your_google_gemini_api_key_here with your actual Google Gemini API key.
   **Name of the env varriable should be GOOGLE_API_KEY**

## Usage
1. Run the Flask app:
   python app.py
2. Open your browser and go to http://127.0.0.1:5000 to interact with the app.
3. Input the job description and upload a resume (PDF or DOCX format). The app will generate personalized interview questions based on the job description and resume.

## How to Use the App
Step 1: Enter the Job Description in the provided text area.
Step 2: Upload the Resume (PDF or DOCX format) of the candidate.
Step 3: Click on Generate Interview Questions to receive ATS score and personalized interview questions.

**Important: Make sure to create a .env file in the root directory and define the GOOGLE_API_KEY variable as described above.**
**This API key is necessary to make the app function.**
