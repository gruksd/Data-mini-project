import nltk
from nltk.tokenize import sent_tokenize
import re

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


name_data = {
    "Pekka Haavisto": [],
    "Alexander Stubb": [],
    "Olli Rehn": [],
    "Mika Aaltola": [],
    "Jussi Halla-aho": [],
    "Li Andersson": [],
    "Jutta Urpilainen": [],
    "Sari Essayah": [],
    "Harry Harkimo": [],
}

for d, s in dataset:
    for sentence in s:
        for name, dates_sentences in name_data.items():
            pattern = re.compile(r'\b' + re.escape(name) + r'\b|\b' + re.escape(name.split()[0]) + r'\b|\b' + re.escape(name.split()[1]) + r'\b', re.IGNORECASE)
            if pattern.search(sentence):
                data_list = []
                sentence_list = []
                dates_sentences_draft2 =[]
                dates_sentences_draft3 =[]
                data_list.append(d)
                sentence_list.append(sentence)
                dates_sentences_draft = [list(data_list), list(sentence_list)]
                dates_sentences.append(dates_sentences_draft)



print(name_data["Pekka Haavisto"])

