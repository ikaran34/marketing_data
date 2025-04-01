from fastapi import FastAPI
import requests
from bs4 import (BeautifulSoup)
app = FastAPI()

    @app.get("/scrape")
    def scrape_website():
        url = "https://www2.hm.com/en_us/men/products/hoodies-sweatshirts.html"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        products = []
        for item in soup.select(".product-item"):  # Adjust selector based on website
            name = item.select_one(".product-name").text.strip()
            price = item.select_one(".product-price").text.strip()
            link = item.select_one("a")["href"]
            products.append({"name": name, "price": price, "link": link})

        return {"products": products}