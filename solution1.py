### **Exercise 1: Extracting and Cleaning Data from an API**
from numbers import Number

import requests
import pandas as pd
import re


columns = ['City', 'Temperature', 'Weather Condition']
df = pd.DataFrame(columns=columns)
cities = ["New York", "London", "Tokyo", "Paris", "Berlin"]
i = 0
for city in cities:
    url = f"https://wttr.in/{city}?format=%C+%t"
    r = requests.get(url)
    html = r.text
    html_p = html.split()
    df.loc[i,"City"] = city
    df.loc[i,"Temperature"] =  html_p[len(html_p) - 1]
    df.loc[i,"Weather Condition"] = " ".join(html_p[:-1])
    i +=1
print(df)

#==================SAU=========================


def parse_weather_data(raw_text):
    parts = raw_text.strip().split()
    if not parts or len(parts) < 2:
        return None, None

    temp_raw = parts[-1]
    condition_raw = " ".join(parts[:-1])

    match = re.search(r"[+-]?\d+", temp_raw)
    temp = match.group().replace(" ", "") if match else None

    condition = condition_raw.strip()
    return temp, condition


cities = ["New York", "London", "Tokyo", "Paris", "Berlin"]
data = []

for city in cities:
    url = f"https://wttr.in/{city}?format=%C+%t"
    try:
        r = requests.get(url, timeout=5)
        if r.status_code != 200:
            print(f"Eroare la {city}: {r.status_code}")
            continue

        raw_text = r.text
        temperature, condition = parse_weather_data(raw_text)

        if temperature is None or condition == "":
            print(f" Date lipsă pentru {city}")
            continue

        data.append({
            "City": city,
            "Temperature": temperature,
            "Weather Condition": condition
        })
    except requests.RequestException as e:
        print(f"Eroare rețea pentru {city}: {e}")
        continue

df = pd.DataFrame(data, columns=["City", "Temperature", "Weather Condition"])
print(df)
