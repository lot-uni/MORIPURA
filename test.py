from fastapi import FastAPI, Request, Response, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# @app.get('/')
# async def index():
#     return templates.TemplateResponse("upload.html", {
#     })

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("upload.html", {
        "request": request
    })

@app.get("/image/{pas}")
def image(pas: str):
    with open("./image/"+pas+".png", "rb") as f:
        return Response(content=f.read(), media_type="image/png")
@app.get("/dele/{pas}")
async def image(pas: str):
    os.remove(f'image/{pas}.png')
    return "ななちー＝"
@app.post("/upload/")
async def upload_file(file: UploadFile):
    # ファイルを保存する場合
    path="./image/"+file.filename
    with open(path, "wb") as f:
        f.write(file.file.read())
    return {"filename": file.filename}

