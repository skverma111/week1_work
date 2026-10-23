import os
import sys
from dotenv import load_dotenv
from openai import OpenAI, AuthenticationError, APIConnectionError

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Error: OPENAI_API_KEY is not found.")
    print("Copy .env.example to .env and add your key")
    sys.exit(1)

client = OpenAI(api_key= api_key)

model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

# --- THE CALL ---
print("Sending prompt: 'What is generative AI in one sentence?'")
print("-" * 50)

try:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Be concise."},
            {"role": "user", "content": "What is generative AI in one sentence?"},
        ],
        temperature=0.7,
        max_tokens=100,
    )

    # --- THE RESPONSE ---
    print()
    print("Response:")
    print(response)
    print(f"  {response.choices[0].message.content}")
    print()
    print("-" * 50)
    print("Response metadata:")
    print(f"  Model used:        {response.model}")
    print(f"  Prompt tokens:     {response.usage.prompt_tokens}")
    print(f"  Completion tokens: {response.usage.completion_tokens}")
    print(f"  Total tokens:      {response.usage.total_tokens}")
    print()
    print("✓ Success! You just talked to an AI from Python.")
    print("=" * 50)
except AuthenticationError:
    print("Error: Authentication failed. Check your OPENAI_API_KEY.")
    sys.exit(1)
except APIConnectionError:
    print("Error: Failed to connect to the OpenAI API. Check your internet connection.")

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
    