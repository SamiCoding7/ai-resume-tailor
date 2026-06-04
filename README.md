# ai-resume-tailor

A Python tool that analyzes your resume against a job description and gives you feedback to help you tailor your application.

## What it does
- Gives a match score showing how well your resume fits the role
- Rewrites your bullet points to better align with the job description
- Identifies skill gaps — what the job wants that your resume is missing
- Pulls out keywords from the job description to add to your resume

## Built with
- Python
- Google Gemini API
- PyPDF2

## How to use
1. Clone the repo
2. Create a `.env` file and add your Gemini API key: `GEMINI_API_KEY=your_key_here`
3. Open the Jupyter notebook and run it
4. Enter your resume path (.txt or .pdf) and paste in a job description
5. Feedback is printed and saved to a .txt file of your choice

## Install dependencies
pip install google-generativeai PyPDF2 python-dotenv
