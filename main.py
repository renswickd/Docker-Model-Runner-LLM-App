import requests

url = "http://localhost:12434/engines/11ama.cpp/v1/chat/completions"
data = {
    "model": "ai/smollm2",
    "messages" : [
        {
        "role": "system",
        "content": "You are a helpful assistant."
        },
        {
        "role": "user",
        "content": "What is containerization?"
        }
    ]
}

response = requests.post(url=url, json=data)
response.raise_for_status()