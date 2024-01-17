
import requests
from bs4 import BeautifulSoup

url = 'https://smoothcomp.com/en/event/13661/participants'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
count = 0
results = soup.find(id = 'registrations')
name = results.find_all('div', class_='profile-card-name font-size-medium truncate')
for n in name:
    count += 1
print(count)

