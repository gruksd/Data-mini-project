from bs4 import BeautifulSoup
from urllib import request
from urllib.request import Request, urlopen
import requests
import re
import nltk
from nltk.tokenize import sent_tokenize

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


urls_weird =["https://yle.fi/a/74-20050630", "https://yle.fi/a/74-20045482", 
             "https://yle.fi/a/74-20045412", "https://yle.fi/a/74-20045052", 
             "https://yle.fi/a/74-20043730", "https://yle.fi/a/74-20037825",
             "https://yle.fi/a/74-20035746", "https://yle.fi/a/74-20054059"]

textes=[]
dates = []
print(len(articles))
for url in articles:
    response = requests.get(url)
    if response.status_code == 200:
        if url not in urls_weird:
            #Extracting text from articles
            soup = BeautifulSoup(response.text, 'html.parser')
            article_text = soup.find_all(class_='yle__article__content')
            for element in article_text:
                textes.append(element.get_text() + '\n')
            #Extracting dates of the articles
            html = request.urlopen(url).read().decode('utf8')
            date = re.findall(r'\"datePublished\": \"(\d{4}-\d{2}-\d{2})', html)
            dates.append(date)

        else:
            #Extracting text from articles
            soup = BeautifulSoup(response.text, 'html.parser')
            article_elements = soup.find_all(class_='post-content')
            for element in article_text:
                textes.append(element.get_text() + '\n')
            #Extracting dates of the articles
            html = request.urlopen(url).read().decode('utf8')
            date = re.findall(r'\"datePublished\": \"(\d{4}-\d{2}-\d{2})', html)
            dates.append(date)
        

    else: 
        continue


print(len(dates), len(textes))

dates = [item for sublist in dates for item in sublist]


for i in range(len(textes)):
    paragraphs = textes[i].split('\n')  
    combined_text = ' '.join(paragraphs) 
    textes[i] = combined_text

with open('article.txt', 'w', encoding='utf-8') as file:
    file.write("#".join(dates))

    file.write('\n')

    file.write("#".join(textes))

    
    
