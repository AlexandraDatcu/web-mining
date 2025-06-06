#
# De pe 10 pagini de metacritic ale unor filme, extrageti regizorul, scorul mediu acordat de critici,
# scorul mediu acordat de utilizatori și durata filmului.
import requests
from bs4 import BeautifulSoup
import pandas as pd
headers = {
    "User-Agent": "Mozilla"
}
data = {
    "Titlul": [],
    "Regizor": [],
    "Metascore": [],
    "UserScore": [],
    "Durata": []
}

urls = ['https://www.metacritic.com/movie/the-leopard-re-release/',
        'https://www.metacritic.com/movie/rear-window/',
        'https://www.metacritic.com/movie/pitch-perfect',
        'https://www.metacritic.com/movie/the-mustang',
        'https://www.metacritic.com/movie/the-pianist',
        'https://www.metacritic.com/movie/the-last-samurai',
        'https://www.metacritic.com/movie/flower',
        'https://www.metacritic.com/movie/summer-1993',
        'https://www.metacritic.com/movie/the-dark-knight',
        'https://www.metacritic.com/movie/a-man-called-otto']
for url in urls:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    data["Titlul"].append(soup.find('h1').text.strip())

    regizor = soup.find('a', attrs={'class': 'c-crewList_link u-text-underline'})
    data["Regizor"].append(regizor.contents[0].strip())

    span = soup.find_all("span", attrs={"data-v-e408cafe": ""})
    data["Metascore"].append(span[0].text.strip())
    data["UserScore"].append(span[1].text.strip())

    durata = soup.find_all("li", attrs={"class": "c-heroMetadata_item u-inline"})
    data["Durata"].append(durata[3].text.strip())
print(data)
df = pd.DataFrame(data)
df.to_csv('data.csv')
print(df)
