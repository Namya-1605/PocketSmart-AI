from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/ask")
async def ask_ai(request: Request, question: str = Form(...)):
    answer = f"You asked: {question}"

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "question": question,
            "answer": answer
        }
    )