import csv
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.farmaciasanpablo.com.mx"

# Example URL of a category or search results page
PRODUCTS_URL = f"{BASE_URL}/online/products/search?keyword=paracetamol"

def fetch_page(url):
    """Fetch a URL and return its content."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text

def parse_products(html):
    """Parse product information from the given HTML."""
    soup = BeautifulSoup(html, "html.parser")
    products = []
    for card in soup.select("div.product-card"):
        name = card.select_one("h2.product-name")
        price = card.select_one("span.product-price")
        if name and price:
            products.append({
                "name": name.get_text(strip=True),
                "price": price.get_text(strip=True),
            })
    return products

def save_csv(products, filename="products.csv"):
    """Save product data to a CSV file."""
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["name", "price"])
        writer.writeheader()
        writer.writerows(products)

def main():
    html = fetch_page(PRODUCTS_URL)
    products = parse_products(html)
    save_csv(products)

if __name__ == "__main__":
    main()
