from fastapi import FastAPI
import requests

app = FastAPI()

SCRAPER_URL = "http://127.0.0.1:8001/scrape"

@app.get("/aggregate")
def aggregate_data():
    try:
        response = requests.get(SCRAPER_URL)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        return {"error": f"Failed to fetch data: {e}"}
    return {"error": "Unknown error occurred"}
