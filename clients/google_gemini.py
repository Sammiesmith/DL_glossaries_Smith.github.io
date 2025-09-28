# lm_personalization/clients/azure_openai.py
import os
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env from project root (works in scripts & notebooks)
ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")

def _require(name: str) -> str:
    val = os.getenv(name)
    if not val:
        raise RuntimeError(f"Missing required env var: {name}")
    return val

# configure Google Generative AI
genai.configure(api_key=_require("GOOGLE_API_KEY"))

# default model = Gemini 1.5 Flash (free, fast)
DEFAULT_MODEL = os.getenv("GOOGLE_GEMINI_MODEL", "gemini-2.5-flash")


# get llm respnse
def get_llm_response(system_prompt: str, user_prompt: str, temperature=0.7) -> str:
    # Calls the google gemini api with a system and user prompt and returns text
    full_prompt = f"[System]\n{system_prompt}\n[User]\n{user_prompt}"
    model = genai.GenerativeModel(DEFAULT_MODEL)
    response = model.generate_content(
        full_prompt,
        generation_config= genai.GenerationConfig(temperature=temperature)
    )
    print("Prompting Gemini...")
    return response.text.strip() if response.text else ""


# Example usage
"""
from CS182-autotext.clients.google_gemini import get_llm_response

system_prompt = "You are a helpful assistant"
user_prompt = "Teach me how to make chocolate chip cookies."

reply = get_llm_response(system_prompt, user_prompt, temperature=0.2)
print(reply)
"""
