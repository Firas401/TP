import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

title = soup.title.text
content = soup.find("p").text
links = [a["href"] for a in soup.find_all("a")]

print("Titre:", title)
print("Premier paragraphe:", content)
print("Liens:", links)
