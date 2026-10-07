from app.config import (
    GEMINI_API_KEY,
    GROK_API_KEY,
    OPENAI_API_KEY,
    OPENROUTER_API_KEY,
)

print("Configuration loaded successfully!")

print("Gemini:", bool(GEMINI_API_KEY))
print("Grok:", bool(GROK_API_KEY))
print("OpenAI:", bool(OPENAI_API_KEY))
print("OpenRouter:", bool(OPENROUTER_API_KEY))