import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()


def answer_question(question):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return "Gemini API key is not configured."

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = f"""
You are EduGenie, an AI learning assistant.

Answer the student's question clearly and simply.
Use easy language and give a useful explanation.

Student Question:
{question}
"""

    response = model.generate_content(prompt)

    return response.text