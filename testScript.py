import requests
from bs4 import BeautifulSoup

def scrape_product_names(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Using the class selector to capture all items in the grid
    grid_items = soup.select('.product-items')
    
    product_names = []
    
    for item in grid_items:
        # Extracting product name
        name = item.select_one('.product-card__name')
        if name:
            product_names.append(name.text.strip())
    
    return product_names

website = "https://fanaticwrestling.com/collections/daily-deals"
product_names = scrape_product_names(website)

print("Products on sale today:")
for name in product_names:
    print(name)
