import pandas as pd
import requests
from bs4 import BeautifulSoup

URL= 'https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html'
req =requests.get(URL)
soup = BeautifulSoup (req.text, 'lxml')

table = soup.find('table', attrs={"id": "weather_records"})
rows = table.find_all('tr')

headers = [header.text.strip() for header in rows[0].find_all('th')]

data = []
for row in rows[1:]:
    cells = row.find_all('td')
    data.append([cell.text.strip() for cell in cells])

weather_records = pd.DataFrame(data, columns=headers)

print(weather_records)