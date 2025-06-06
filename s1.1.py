from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

url = 'https://www.crunchbase.com/organization/facebook'
driver.get(url)
time.sleep(5)  # așteptăm să se încarce complet JS-ul

soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup.prettify())
# Exemplu: cautăm unele secțiuni cunoscute (clasele pot varia!)
location = soup.find('span', string='Headquarters Location')
employee = soup.find('span', string='Number of Employees')
website = soup.find('span', string='Website')
funding = soup.find('span', string='Total Funding Amount')

print("Locație:", location.find_next('span').text.strip() if location else "N/A")
print("Angajați:", employee.find_next('span').text.strip() if employee else "N/A")
print("Website:", website.find_next('a').text.strip() if website else "N/A")
print("Fonduri totale:", funding.find_next('span').text.strip() if funding else "N/A")

driver.quit()
