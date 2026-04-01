import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_email_reply(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        # 🔥 DEBUG (see response in terminal)
        print("API RESPONSE:", result)

        if "choices" in result:
            return result["choices"][0]["message"]["content"]

        elif "error" in result:
            return f"API Error: {result['error']['message']}"

        else:
            return f"Unexpected Response: {result}"

    except Exception as e:
        return f"Exception: {str(e)}"