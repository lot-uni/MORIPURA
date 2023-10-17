from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request


app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request
    })

@app.get("/image/{pas}")
def image(pas: str):
    with open("./image/"+pas+".png", "rb") as f:
        return Response(content=f.read(), media_type="image/png")