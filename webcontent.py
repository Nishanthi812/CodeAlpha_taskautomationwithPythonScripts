import requests
from bs4 import BeautifulSoup
url = "https://www.python.org"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string.strip()
    with open("webpage_title.txt", "w", encoding="utf-8") as f:
        f.write(f"Page Title: {title}\n")
    print("✅ Title scraped and saved successfully!")
else:
    print("❌ Failed to fetch the webpage.")