
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.repository import VideoRepository

app = FastAPI()

templates = Jinja2Templates(directory="templates")

video_repository = VideoRepository("data")

@app.get("/health")
def health():
    return {"status": "UP"}


@app.get("/vocabulary/{video_id}/{language}")
def vocabulary(request: Request,video_id,language):

    context = {
        "request" : request,   
        "title" : "Hello World!", 
        "vocabulary" : video_repository.get_vocabulary(video_id,language)
    }

    return templates.TemplateResponse("vocabulary.html", context)


@app.get("/play/{video_id}/{language}")
def play(request: Request,video_id,language):

    context = {
        "request" : request,   
        "title" : "Hello World!", 
        "cards" : video_repository.get_vocabulary(video_id,language)
    }

    return templates.TemplateResponse("play.html", context)


@app.get("/")
def home(request: Request):

    context = {
        "request" : request,   
        "title" : "Hello World!", 
        "videos" : video_repository.get_metadata_list()
    }


    return templates.TemplateResponse("index.html", context)


app.mount("/", StaticFiles(directory="htdocs",html = True))

