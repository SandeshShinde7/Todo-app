# news_scraper.py

import requests
from bs4 import BeautifulSoup

# URL of the news website (you can change to any news site you prefer)
URL = "https://www.bbc.com/news"

# Step 1: Fetch the HTML content
response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
if response.status_code != 200:
    print(f"Failed to fetch page, status code: {response.status_code}")
    exit()

# Step 2: Parse the HTML with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract headlines (look for <h2> or <h3> tags commonly used in news sites)
headlines = soup.find_all(["h2", "h3"])

# Step 4: Clean and store headlines in a list
cleaned_headlines = []
for h in headlines:
    text = h.get_text(strip=True)
    if text and len(text) > 15:  # filter short junk text
        cleaned_headlines.append(text)

# Step 5: Save the headlines into a text file
with open("headlines.txt", "w", encoding="utf-8") as f:
    for i, headline in enumerate(cleaned_headlines, 1):
        f.write(f"{i}. {headline}\n")

print(f"✅ {len(cleaned_headlines)} headlines saved to headlines.txt")
