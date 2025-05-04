from fastapi import FastAPI
from pydantic import BaseModel
import requests
import uvicorn

# NVIDIA API details
NVIDIA_API_URL = "https://integrate.api.nvidia.com/v1"
NVIDIA_API_KEY = "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"
MODEL = "nvidia/llama-3.1-nemotron-70b-instruct"

application = FastAPI()

# Request model
class Question(BaseModel):
    question: str

@application.post("/ask")
async def ask_question(payload: Question):
    try:
        # Prepare request payload
        headers = {
            "Authorization": f"Bearer {NVIDIA_API_KEY}",
            "Content-Type": "application/json",
        }

        data = {
            "model": MODEL,
            "messages": [{"role": "user", "content": payload.question}],
            "temperature": 0.5,
            "top_p": 1,
            "max_tokens": 1024,
            "stream": False
        }

        # Make the POST request to NVIDIA API
        response = requests.post(NVIDIA_API_URL + "/chat/completions", json=data, headers=headers)

        if response.status_code == 200:
            answer = response.json()['choices'][0]['message']['content'].strip()
            return {"answer": answer}
        else:
            return {"error": f"Error: {response.status_code}, {response.text}"}

    except Exception as e:
        return {"error": str(e)}

# Run the app
if __name__ == "__main__":
    uvicorn.run("application:application", host="0.0.0.0", port=8000)

