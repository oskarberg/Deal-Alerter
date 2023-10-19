import requests
from bs4 import BeautifulSoup
from plyer import notification


# Function to scrape product names
def scrape_product_names(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    grid_items = soup.select('.product-items')
    
    product_names = []
    
    for item in grid_items:
        name = item.select_one('.product-card__name')
        if name:
            product_names.append(name.text.strip().lower())  # Convert to lowercase
    
    return product_names


# Function to send desktop notification
def send_desktop_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,  
        timeout=10, 
    )


# List of websites to scrape
websites = [
    "https://bjjfanatics.com/collections/daily-deals",
    "https://fanaticwrestling.com/collections/daily-deals",
    "https://dynamicstriking.com/collections/daily-deals"
]

# List of desired video instructional names you want to match (converted to lowercase for comparison)
video_names = [name.lower() for name in [
    "Single Legs For MMA By Beneil Dariush",
    # Add other video names here
]]

matched_names = []

# Scrape product names from all websites and check for matches
for website in websites:
    scraped_names = scrape_product_names(website)
    for name in scraped_names:
        if name in video_names:
            matched_names.append(name.title())


# If there are matched names, send a desktop notification
if matched_names:
    send_desktop_notification("Watchlisted item on sale!", "\n".join(matched_names))


