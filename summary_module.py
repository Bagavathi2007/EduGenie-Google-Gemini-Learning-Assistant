import os
import google.generativeai as genai


def summarize_text(text):

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return "Gemini API key is not configured."

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = f"""
You are EduGenie, an educational learning assistant.

Summarize the following educational text in a short,
clear and easy-to-understand way.

Educational Text:
{text}
"""

    try:
        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"Summary generation error: {str(e)}"