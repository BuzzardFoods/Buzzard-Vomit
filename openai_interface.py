import requests
import json

def get_response(prompt):
    url = "http://localhost:1234/v1/completions"

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "model": "openhermes-2.5-mistral-7b",  # Make sure this matches what LM Studio shows
        "prompt": prompt,
        "temperature": 0.7,
        "max_tokens": 500,
        "stop": ["User:", "Aura:", "###"]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        result = response.json()
        return result["choices"][0]["text"]
    except Exception as e:
        return f"[Error getting response: {e}]"
