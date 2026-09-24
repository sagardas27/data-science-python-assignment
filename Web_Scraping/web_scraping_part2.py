import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website used for scraping practice
url = "https://quotes.toscrape.com/"

records = []
page = 1

while len(records) < 50:
    page_url = url + f"page/{page}/"

    response = requests.get(page_url)

    if response.status_code != 200:
        print("Failed to access page:", page)
        break

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    if not quotes:
        break

    for quote in quotes:
        text = quote.find("span", class_="text").get_text(strip=True)
        author = quote.find("small", class_="author").get_text(strip=True)

        records.append({
            "Quote": text,
            "Author": author
        })

        if len(records) >= 50:
            break

    page += 1

# Convert to DataFrame
df = pd.DataFrame(records)

# Save only the first 50 records
df = df.head(50)

output_file = "scraped_quotes.csv"
df.to_csv(output_file, index=False)

print("Scraping completed successfully!")
print("Number of records:", len(df))
print("CSV file created:", output_file)
print(df.head())