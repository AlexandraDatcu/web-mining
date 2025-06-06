### **Exercise 2: Web Scraping a Product Listings Page**
import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

r = requests.get(URL)
html = r.text
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())
prices = soup.find_all("span", attrs={"itemprop": "price"})
products = soup.find_all("a", attrs={"class": "title"})

values = []
for i in range(len(prices)):
    values.append((products[i].get("title"), prices[i].contents[0]))

df = pd.DataFrame(values, columns=["Product", "Price"])
print(df)
df.drop_duplicates(subset="Product", inplace=True)
print(df)
df.to_csv("scraped_products.csv", index=False)
