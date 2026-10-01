import os
import google.generativeai as genai


def explain_topic(topic):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return "Gemini API key is not configured."

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = f"""
You are EduGenie, an educational learning assistant.

Explain the following topic in simple and easy language.
Make the explanation clear for a student.

Topic:
{topic}
"""

    response = model.generate_content(prompt)

    return response.text