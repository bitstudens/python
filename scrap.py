import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from collections import Counter
import string


# url = "https://anishansari.com.np/"
# response = requests.get(url)
# print(response)
# soup  = BeautifulSoup(response.text, "html.parser")
# page_title = soup.title.string
# page_h1 = soup.h1.string
# page_p = soup.p.string
# print(page_title)
# print(page_h1)
# print(page_p)
#robots.txt

# URL = "https://www.bbc.com/news"
# headers = {
#     "User-Agent": "Mozilla/5.0"
# }
# response = requests.get(URL, headers=headers)
# soup = BeautifulSoup(response.text, "html.parser")

# headlines = [h.get_text() for h in soup.find_all("h2")[:10]]
# print(headlines)

# # for idx, h in enumerate(headlines, 1):
# #     print(f"{idx}. {h.text.strip()}")
# text = " " . join(headlines).lower()
# for char in string.punctuation:
#     text = text.replace(char, "")
# words = text.split() 

# stopwords = ["the", "a", "an", "is", "are", "to", "of", "and", "in", "for"]
# words = [word for word in words if word not in stopwords]
# word_count = Counter(words)
# common = word_count.most_common(10)
# words, counts = zip(*common)
# plt.bar(words, counts)
# plt.title("Top 10 Words in BBC News Headlines")
# plt.ylabel("Words")
# plt.show()


# import matplotlib.pyplot as plt

# Sample days
days = [1, 2, 3, 4, 5, 6, 7]

# Corresponding stock prices
prices = [100, 105, 102, 110, 108, 115, 112]

# Create the line plot
plt.plot(days, prices)

# Add labels and a title
plt.xlabel("Day")
plt.ylabel("Stock Price ($)")
plt.title("Hypothetical Stock Price Over Time")

# Display the plot
plt.show()



