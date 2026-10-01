import os
import google.generativeai as genai


def generate_learning_path(topic):

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return "Gemini API key is not configured."

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = f"""
You are EduGenie, an educational learning assistant.

Create a structured learning path for the following topic.

The learning path should contain:
1. Beginner level
2. Intermediate level
3. Advanced level
4. Useful learning resources

Keep the explanation simple and useful for a student.

Topic:
{topic}
"""

    try:
        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"Learning path generation error: {str(e)}"