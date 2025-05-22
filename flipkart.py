import requests
from bs4 import BeautifulSoup
import random
import time
import matplotlib.pyplot as plt
from fake_useragent import UserAgent

# Setup
ua = UserAgent()

def get_headers():
    return {
        "User-Agent": ua.random,
        "Accept-Language": "en-US,en;q=0.9",
    }

def scrape_amazon_products(search_term, pages=5):
    products = []
    
    for page in range(1, pages + 1):
        print(f"Scraping '{search_term}' - Page {page}")
        url = f"https://www.flipkart.com/search?q={search_term.replace(' ', '+')}&page={page}"
        try:
            response = requests.get(url, headers=get_headers(), timeout=10)
            if "captcha" in response.url or "Enter the characters" in response.text:
                print("⚠️ CAPTCHA triggered! Stopping.")
                break

            soup = BeautifulSoup(response.content, "html.parser")
            items = soup.select("div ._75nlfW")
            print(items)
            for item in items:
                title_tag = item.select_one("a")
                rating_tag = item.select_one("div .XQDdHH")

                if title_tag and rating_tag:
                    try:
                        title = title_tag.text.strip()
                        rating = float(rating_tag.text.strip().split()[0])
                        products.append((title, rating))
                    except:
                        continue

            time.sleep(random.uniform(1, 3))  # Polite delay

        except Exception as e:
            print(f"Error: {e}")
            continue

    return products

# Main
search_terms = ["laptops", "smartphones", "headphones", "monitors", "watches"]
all_products = []

for term in search_terms:
    scraped = scrape_amazon_products(term, pages=10)  # 10 pages × ~20 = ~200 per term
    all_products.extend(scraped)

# Deduplicate by title
unique_products = list({title: rating for title, rating in all_products}.items())

print(f"\n✅ Total unique products scraped: {len(unique_products)}")

# Sort and get top 20
top_products = sorted(unique_products, key=lambda x: -x[1])[:20]
titles, ratings = zip(*top_products)

# Plotting
plt.figure(figsize=(10, 8))
plt.barh(titles[::-1], ratings[::-1])
plt.xlabel("Rating")
plt.title("Top 20 Rated Amazon.in Products (Scraped)")
plt.tight_layout()
plt.show()