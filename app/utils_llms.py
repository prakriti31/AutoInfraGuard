import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def suggest_fix_for_error(error_message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert DevOps engineer. Help debug errors."},
                {"role": "user", "content": f"Explain and suggest a fix for this error:\n{error_message}"}
            ],
            temperature=0.3,
            max_tokens=200
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ Suggestion failed: {e}"
