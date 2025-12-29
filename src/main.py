# Modules
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.services.ai_service import get_ai_response

# Initialize the Instance
app = FastAPI(
    title="My Professional Prtfolio",
    description="A great portfolio built with FastAPI and Jinja2",
    version="1.0.0"
)

# We Initialize Statics and Jija2Templates
app.mount("/static", StaticFiles(directory="src/static"), name="static")
templates = Jinja2Templates(directory="src/templates")

# GET Requests
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/projects")
async def projects_page(request: Request):
    return templates.TemplateResponse("projects.html", {"request": request})

@app.get("/chat")
async def chat_page(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

# POST Requests
@app.post("/chat")
async def chat(message: str):
    response= await get_ai_response(message)
    return {"reply": response}

