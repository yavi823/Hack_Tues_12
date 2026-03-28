import base64
import os
import requests
import json
import subprocess

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Nqma OPENAI_API_KEY")
    exit()

subprocess.run(["rpicam-jpeg", "-o", "plant.jpg"], check=True)

with open("plant.jpg", "rb") as f:
    image_b64 = base64.b64encode(f.read()).decode("utf-8")

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

payload = {
    "model": "gpt-4.1-mini",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Analizirai snimkata na rastenieto i mi vurni samo kratuk status na bulgarski."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{image_b64}",
                        "detail": "high"
                    }
                }
            ]
        }
    ],
    "max_tokens": 200
}

response = requests.post(url, headers=headers, json=payload)
data = response.json()

print(data["choices"][0]["message"]["content"])