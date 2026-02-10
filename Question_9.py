import requests
from bs4 import BeautifulSoup
import csv

url = "https://en.wikipedia.org/wiki/Machine_learning"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

content = soup.find("div", id="mw-content-text")

# find first table with at least 3 rows
for table in content.find_all("table"):
    rows = table.find_all("tr")
    if len(rows) >= 4:   # 1 header + 3 data rows
        break

# get all rows
rows = table.find_all("tr")

# headers
headers_cells = rows[0].find_all("th")
if headers_cells:
    headers_row = [h.get_text(strip=True) for h in headers_cells]
else:
    cols = len(rows[1].find_all(["td", "th"]))
    headers_row = [f"col{i+1}" for i in range(cols)]

# table data
data = []
for row in rows[1:]:
    cells = row.find_all(["td", "th"])
    if not cells:
        continue

    row_data = [c.get_text(strip=True) for c in cells]
    while len(row_data) < len(headers_row):
        row_data.append("")
    data.append(row_data)

# save CSV (same folder as this Python file)
file_path = "wiki_table.csv"
with open(file_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers_row)
    writer.writerows(data)

print(f"Table saved with {len(data)} rows")
