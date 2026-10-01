import os
import json
import google.generativeai as genai


def generate_quiz(topic):

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return "Gemini API key is not configured."

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = f"""
You are EduGenie, an educational quiz generator.

Create exactly 3 multiple-choice questions about the given topic.

Each question must have exactly 4 options.
Provide the correct answer for each question.

Return ONLY valid JSON in this format:

[
  {{
    "question": "Question 1",
    "options": ["A", "B", "C", "D"],
    "answer": "A"
  }},
  {{
    "question": "Question 2",
    "options": ["A", "B", "C", "D"],
    "answer": "B"
  }},
  {{
    "question": "Question 3",
    "options": ["A", "B", "C", "D"],
    "answer": "C"
  }}
]

Topic:
{topic}
"""

    try:
        response = model.generate_content(prompt)

        text = response.text.strip()

        if text.startswith("```"):
            text = text.replace("```json", "").replace("```", "").strip()

        quiz = json.loads(text)

        return quiz

    except Exception as e:
        return f"Quiz generation error: {str(e)}"