# main.py
from fastapi import FastAPI, Depends, HTTPException, Header
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import ollama

load_dotenv()

API_KEY = os.getenv("API_KEY", "dev_key")  # pour dev si .env absent
INITIAL_CREDITS = int(os.getenv("INITIAL_CREDITS", "5"))

# Map clé -> crédits (in-memory). Pour production, utiliser DB.
API_KEY_CREDITS = {API_KEY: INITIAL_CREDITS}

app = FastAPI(title="LLM API Lab")

class GenerateRequest(BaseModel):
    prompt: str

def verify_api_key(x_api_key: str = Header(None)):
    if x_api_key is None or x_api_key not in API_KEY_CREDITS:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    credits = API_KEY_CREDITS.get(x_api_key, 0)
    if credits <= 0:
        raise HTTPException(status_code=402, detail="No credits remaining")
    return x_api_key

@app.post("/generate")
def generate(payload: GenerateRequest, api_key: str = Depends(verify_api_key)):
    # Deduct a credit
    API_KEY_CREDITS[api_key] -= 1
    # Call Ollama (chat API)
    # Note: ollama.chat returns a dict-like structure
    resp = ollama.chat(model="mistral", messages=[{"role": "user", "content": payload.prompt}])
    # defensive extraction
    content = None
    try:
        content = resp["message"]["content"]
    except Exception:
        # fallback to string representation
        content = str(resp)
    return {"response": content, "credits_left": API_KEY_CREDITS[api_key]}
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "🚀 FastAPI fonctionne parfaitement !"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Salut {name}, bienvenue sur ton API FastAPI 😎"}
