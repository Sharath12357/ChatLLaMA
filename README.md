# 🧠 Chat API using FastAPI and NVIDIA NIM (LLaMA 3.1)

This project provides a RESTful API that accepts a JSON body with a `question` key, sends it to a large language model (LLaMA 3.1 70B Instruct) via NVIDIA NIM, and returns the model's response.

---

## ⚠️ Why NVIDIA NIM instead of OpenAI ChatGPT?

> **ChatGPT API requires a paid subscription**, so this project uses **NVIDIA's free-to-use NIM API** as a drop-in alternative with similar capabilities.

---

## 🔗 Hosted API Endpoint (replace with your actual EC2 URL)

```bash
curl -X POST https://<your-ec2-ip-or-domain>/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is the capital of France?"}'


# 1. Clone this repo
git clone https://github.com/your-username/your-repo.git
cd your-repo

# 2. Set up a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install fastapi uvicorn requests

# 4. Run the server
uvicorn app:app --host 0.0.0.0 --port 8000




curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is the capital of France?"}'
