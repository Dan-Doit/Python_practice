import requests
from bs4 import BeautifulSoup

url = "http://google.com"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print(soup.find("li", attrs={"원하는 내용"})) # 원하는 내용 찾기

