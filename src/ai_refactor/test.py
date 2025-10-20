from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()
hf_token = os.getenv("HUGGINGFACE_API_KEY")

client = InferenceClient(token=hf_token)

# Chat messages
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "how can I be a software engineer roadmap?"}
]

# Correct way to call chat_completion
response = client.chat_completion(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    messages=messages,
    max_tokens=100
)

# Print the assistant reply
print(response.choices[0].message["content"])



