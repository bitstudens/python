import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def get_products(search_query, max_products=10):
    url = f"https://www.amazon.in/s?k={search_query.replace(' ', '+')}" 
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    
    titles = []
    ratings = []

    for product in soup.select(".s-result-item")[:max_products]:
        title_tag = product.select_one("h2 span")
        rating_tag = product.select_one(".a-icon-alt")
        
        if title_tag and rating_tag:
            try:
                title = title_tag.get_text()
                rating = float(rating_tag.get_text().split()[0])
                titles.append(title[:60])  
                ratings.append(rating)
            except:
                continue

    return titles, ratings

titles, ratings = get_products("toys", max_products=10)

# Plotting
plt.figure(figsize=(10, 5))
plt.barh(titles, ratings)
plt.xlabel("Ratings")
plt.title("Top Rated Products on Amazon.in")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()