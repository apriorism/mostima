from os import getenv
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from scripts.config import MostimaConfig
import scripts.state as state

app = FastAPI()
templates = Jinja2Templates(directory='templates')
config = MostimaConfig(getenv('CONFIG_PATH') or 'config.toml')


app.mount('/public', StaticFiles(directory='public'), name='public')


@app.get('/', response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(request=request, name='index.html')