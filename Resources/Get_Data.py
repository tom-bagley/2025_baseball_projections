import pandas as pd
from lxml import html
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
import requests
from bs4 import Comment
import time
import random

def is_year(value):
    try:
        # Try to convert to integer and check if it falls within a reasonable range for years
        year = int(value)
        return 1900 <= year <= 2100
    except ValueError:
        return False

def get_table(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")
  tables = soup.find_all("table")
  for table in tables:
    if table.get("id") == "batting_standard":
      data = []
      for tr in table.find_all('tr'):
          row = []
          for td in tr.find_all(['th', 'td']):
            row.append(td.text.strip())
          if row:
            data.append(row)
    elif table.get("id") == "pitching_standard":
      data = []
      for tr in table.find_all('tr'):
          row = []
          for td in tr.find_all(['th', 'td']):
            row.append(td.text.strip())
          if row:
            data.append(row)
  try:
    headers = data[0]
    df = pd.DataFrame(data, columns = headers)
    df = df.drop(df.index[0])
    name = soup.find("h1").text
    df.insert(0, "Name", name)
    df['Name'] = df['Name'].str.replace('\n', '')
    df = df[df['Year'].apply(is_year)]
    return df
  except:
    return None

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
complete_data = pd.DataFrame()
for letter in letters:
  url = f"https://www.baseball-reference.com/players/{letter}/"
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")
  print(letter)
  players = []
  links = soup.find_all("a")
  for link in links:
    href = link.get("href")
    if href and href.startswith("/players/") and href.endswith(".shtml"):
      full_url = "https://www.baseball-reference.com" + href
      players.append(full_url)
  data = pd.DataFrame()
  for player in players:
    df = get_table(player)
    time.sleep(random.uniform(1, 3))
    if df is not None:
      data = pd.concat([data, df], ignore_index=True)
  complete_data = pd.concat([complete_data, data], ignore_index=True)

print(len(data))
n = complete_data.nunique(axis=0)
print("No.of.unique values in each column :\n",
      n)

complete_data.to_excel("win probabilty added3.xlsx", index=False)