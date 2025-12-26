from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

from src.services.ai_service import get_ai_response

my_app = FastAPI(
    title="My Professional Prtfolio",
    description="A great portfolio built with FastAPI and Jinja2",
    version="1.0.0"
)
my_app.mount("/static", StaticFiles(directory="src/static"), name="static")
my_templates = Jinja2Templates(directory="src/templates")

@my_app.get("/")
async def home(request: Request):
    return my_templates.TemplateResponse("index.html", {"request": request})

"""
@my_app.post("/chat")
async def chat(message: str):
    response= await get_ai_response(message)
    return {"reply": response}
"""

@my_app.get("/chat")
async def chat_page(request: Request):
    return my_templates.TemplateResponse("chat.html", {"request": request})

@my_app.post("/chat")
async def chat_logic(message: str):
    return {"reply": f"You said: {message}. (Ollama integration coming next!)"}
