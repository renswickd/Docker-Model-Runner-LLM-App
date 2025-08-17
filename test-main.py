import requests

url = "http://localhost:12434/engines/llama.cpp/v1/chat/completions"
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

try:
    response = requests.post(url=url, json=data)
    response.raise_for_status()

    # Extract results
    print(response.json()["choices"][0]["message"]["content"])

except:
    print("An error occurred while making the request.")
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    raise

