import httpx

async def get_ai_response(user_message: str):
    # Ollama runs a local API on port 11434
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3.2:1b",
        "prompt": user_message,
        "stream": False
    }

    async with httpx.AsyncClient as client:
        response = await client.post(url, json=payload, timeout=30.0)
        return response.json().get("response")