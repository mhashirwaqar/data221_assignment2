import requests
from bs4 import BeautifulSoup

# URL of the page
url = "https://en.wikipedia.org/wiki/Data_science"

# headers to avoid being blocked
headers = {
    "User-Agent": "Mozilla/5.0"
}

# send request
response = requests.get(url, headers=headers)

# parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# extract and print page title
page_title = soup.title.text.strip()
print("Page Title:", page_title)

# find main content div
content_div = soup.find("div", id="mw-content-text")

# find paragraphs inside the main content
paragraphs = content_div.find_all("p")

# extract first paragraph with at least 50 characters
for p in paragraphs:
    paragraph_text = p.get_text().strip()
    if len(paragraph_text) >= 50:
        print("\nFirst paragraph (≥ 50 characters):")
        print(paragraph_text)
        break
