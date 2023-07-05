
# #singer, name = map(str, input().split())

singer = 'eisbrecher'
name = 'angst'

import requests
from bs4 import BeautifulSoup


response = requests.get(f'https://www.amalgama-lab.com/songs/{singer[0]}/{singer}/{name}.html')

soup = BeautifulSoup(response.text, 'lxml')


original = soup.find_all('div', class_='original')
translate = soup.find_all('div', class_='translate')

for i in range(len(original)):
    print(original[i].text)
    print(translate[i].text)
print(0)
