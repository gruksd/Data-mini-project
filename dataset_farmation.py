import nltk
from nltk.tokenize import sent_tokenize

with open("article.txt", "r", encoding='utf-8') as file:
    content = file.read()

dates_str, textes_str = content.split('\n')
dates = dates_str.split('#')
textes = textes_str.split('#')

dates_textes = list(zip(dates, textes))

dataset = []
for date, text in dates_textes:
    sentences = sent_tokenize(text)
    dataset.append((date, sentences))


    
print(dataset[0])

