from bs4 import BeautifulSoup
import requests
url = 'https://ru.wikipedia.org/wiki/%D0%98%D0%B3%D0%B3%D0%B4%D1%80%D0%B0%D1%81%D0%B8%D0%BB%D1%8C'
filtered_text = []
only_text = []
page = requests.get(url)
if page.status_code == 200:
    soup = BeautifulSoup(page.text, 'html.parser')
filtered_text = soup.findAll()
#print(filtered_text)
for data in filtered_text:
    if data.find() is not None:
        only_text.append((data.text))
#print(only_text)
for i in only_text:
    print(i)