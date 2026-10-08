# Exercises: Day 22

# 1 Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').

import requests
from bs4 import BeautifulSoup

import json

# url = 'https://www.bu.edu/president/boston-university-facts-stats/'

# response = requests.get(url)
# print(response.status_code)

# # beautiful soup will give a chance to parse
# soup = BeautifulSoup(response.content, 'html.parser') 

# data = []

# for item in soup.find_all("li"):
#     text = item.get_text(" ", strip=True)
#     data.append(text)

# with open("website_data.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)

# 2 Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file

# 3 Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.
url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

headers = {"User-Agent": "Opera Omnia"}

response = requests.get(url)
print(response.status_code)

# beautiful soup will give a chance to parse
soup = BeautifulSoup(response.content, 'html.parser') 

# data = []

# for item in soup.find_all("li"):
#     text = item.get_text(" ", strip=True)
#     data.append(text)

# with open("website_data.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)