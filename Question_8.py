import requests
from bs4 import BeautifulSoup

# Wikipedia page URL
url = "https://en.wikipedia.org/wiki/Data_science"

# send request with User-Agent
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

# parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# main content area
main_content = soup.find("div", id="mw-content-text")

# list to store headings
heading_list = []

# headings to exclude
excluded_headings = ["References", "External links", "See also", "Notes"]

# extract section headings
if main_content is not None:
    section_tags = main_content.find_all(["h2", "h3"])

    for tag in section_tags:
        heading_text = tag.get_text().replace("[edit]", "").strip()

        if heading_text == "":
            continue

        if any(word in heading_text for word in excluded_headings):
            continue

        heading_list.append(heading_text)

# save headings to file (same folder as this Python file)
file_path = "headings.txt"
with open(file_path, "w", encoding="utf-8") as file:
    for heading in heading_list:
        file.write(heading + "\n")

# confirmation output
print("Number of headings saved:", len(heading_list))
