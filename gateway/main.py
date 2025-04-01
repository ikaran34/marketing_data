from fastapi import FastAPI
import requests

app = FastAPI()

AGGREGATOR_URL = "http://aggregator:8000/aggregate"

@app.get("/products")
def get_products():
    try:
        response = requests.get(AGGREGATOR_URL)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        return {"error": "Failed to fetch products", "details": str(e)}

    return {"error": "Unknown error occurred"}
