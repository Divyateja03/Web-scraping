import requests
import csv
from bs4 import BeautifulSoup

url = input("Enter the url:")
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')
data = '\n'.join(line.strip() for line in soup.get_text().splitlines() if line.strip())

with open('web_content.csv', 'w', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([data])

print("Text content saved to web_content.csv")

