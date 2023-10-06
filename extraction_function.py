from bs4 import BeautifulSoup
from urllib import request
from urllib.request import Request, urlopen
import requests
import re


url = "https://yle.fi/uutiset/18-252783"
html = request.urlopen(url).read().decode('utf8')

links = re.findall(r'href=\"(\/a\/74-\w+)\" class=\"underlay-link\"', html)

articles = []

for link in links:
    articles.append("https://yle.fi" + link)


url = "https://yle.fi/uutiset/18-217902"
html = request.urlopen(url).read().decode('utf8')

links = re.findall(r'\"contentId\"\:\"(74-\w+)\"', html)

for link in links:
    articles.append("https://yle.fi/a/" + link)

textes=[]
i=1
for url in articles:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        article_text = soup.find_all(class_='yle__article__content')
        for element in article_text:
            textes.append(element.get_text() + '\n')
        print(i, "done")
        i+=1
    else: 
        print(i, "not done")
        i+=1
        continue

with open('article.txt', 'w', encoding='utf-8') as file:
    for element in article_text:
        file.write("\n".join(textes))
    
    
