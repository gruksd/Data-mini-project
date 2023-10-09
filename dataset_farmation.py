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


def extract_month_and_sentence_count(data):
    result = {}
    for item in data:
        date = item[0][0]
        year, month, _ = date.split('-')
        year = int(year)
        month = int(month)
        sentences = item[1][0]
        sentence_count = len(re.split(r'[.!?]', sentences))
        
        if (year, month) in result:
            result[(year, month)] += sentence_count
        else:
            result[(year, month)] = sentence_count
    sorted_result = {k: v for k, v in sorted(result.items(), key=lambda item: item[0])}
    
    return sorted_result


#input_data = name_data["Alexander Stubb"]

#output = extract_month_and_sentence_count(input_data)


#print(output)

#print(name_data["Pekka Haavisto"])
name_list = [
    "Pekka Haavisto",
    "Alexander Stubb",
    "Olli Rehn",
    "Mika Aaltola",
    "Jussi Halla-aho",
    "Li Andersson",
    "Jutta Urpilainen",
    "Sari Essayah",
    "Harry Harkimo",
]
plotting_data = {}
for name in name_list:
    input_data = name_data[name]

    output = extract_month_and_sentence_count(input_data)
    plotting_data[name] = output

#print(plotting_data)

import matplotlib.pyplot as plt
from datetime import datetime

color_palette = {
    'Pekka Haavisto': 'greenyellow',
    'Alexander Stubb': 'darkblue',
    'Olli Rehn': 'seagreen',
    'Mika Aaltola': 'lightslategray',
    'Jussi Halla-aho': 'skyblue',
    'Li Andersson': 'indianred',
    'Jutta Urpilainen': 'lightcoral',
    'Sari Essayah': 'blueviolet',
    'Harry Harkimo': 'hotpink'
}

fig, ax = plt.subplots()

for name, mentions in plotting_data.items():
    x = [datetime(year, month, 1) for year, month in mentions.keys()]  
    y = list(mentions.values())  
    color = color_palette.get(name, 'gray') 
    ax.plot(x, y, label=name, color=color)


ax.set_xlabel('Time')
ax.set_ylabel('Number of Mentions')
ax.set_title('Media Mentions Over Time')
ax.legend(loc='upper right')


date_format = plt.matplotlib.dates.DateFormatter('%b, %Y')
ax.xaxis.set_major_formatter(date_format)


plt.xticks(rotation=45)


plt.grid(True)
plt.tight_layout()
plt.show()


import seaborn as sns

# Your data and color palette definitions remain the same

fig, ax = plt.subplots(figsize=(10, 6))  # Set the figure size

for name, mentions in plotting_data.items():
    x = [datetime(year, month, 1) for year, month in mentions.keys()]  
    y = list(mentions.values())  
    color = color_palette.get(name, 'gray') 
    sns.lineplot(x=x, y=y, label=name, color=color)  # Use Seaborn's lineplot function

ax.set_xlabel('Time')
ax.set_ylabel('Number of Mentions')
ax.set_title('Media Mentions Over Time')
ax.legend(loc='upper right')

date_format = plt.matplotlib.dates.DateFormatter('%b, %Y')
ax.xaxis.set_major_formatter(date_format)
plt.xticks(rotation=45)

plt.grid(True)
plt.tight_layout()
plt.show()
