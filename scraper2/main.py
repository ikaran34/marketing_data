from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

AGGREGATOR_URL = "http://127.0.0.1:8002/aggregate"

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    try:
        response = requests.get(AGGREGATOR_URL)
        products = response.json().get("products", [])
    except Exception as e:
        products = []
        print(f"Error fetching data: {e}")

    return templates.TemplateResponse("index.html", {"request": request, "products": products})
