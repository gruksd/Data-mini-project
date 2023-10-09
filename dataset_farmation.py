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
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

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

# Color palette
color_palette = {
    'Pekka Haavisto': 'greenyellow',
    'Alexander Stubb': 'darkblue',
    'Olli Rehn': 'seagreen',
    'Mika Aaltola': 'lightslategray',
    'Jussi Halla-aho': 'skyblue',
    'Li Andersson': 'indianred',
    'Jutta Urpilainen': 'lightcoral',
    'Sari Essayah': 'blueviolet',
    'Harry Harkimo': 'hotpink',
}

# Create a Seaborn figure
plt.figure(figsize=(12, 6))
sns.set_style("whitegrid")

for name, mentions in plotting_data.items():
    x = [datetime(year, month, 1) for year, month in mentions.keys()]  
    y = list(mentions.values())  
    color = color_palette.get(name, 'gray')
    sns.lineplot(x=x, y=y, label=name, color=color)


plt.title('Media Mentions Over Time')
plt.xticks(rotation=45)

# Customize legend placement
plt.legend(loc='upper right')

# Format x-axis dates
date_format = plt.matplotlib.dates.DateFormatter('%b, %Y')
plt.gca().xaxis.set_major_formatter(date_format)

plt.tight_layout()
plt.show()

import plotly.express as px
import pandas as pd

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

# Create a DataFrame from the plotting data
df = pd.DataFrame({
    'Name': [name for name in plotting_data.keys() for _ in plotting_data[name]],
    'Date': [datetime(year, month, 1) for name in plotting_data.keys() for year, month in plotting_data[name].keys()],
    'Mentions': [count for name in plotting_data.keys() for count in plotting_data[name].values()],
})

# Map names to colors using the color_palette dictionary
df['Color'] = df['Name'].map(color_palette)

# Create the Plotly figure
fig = px.line(
    df,
    x='Date',
    y='Mentions',
    color='Name',
    color_discrete_map=color_palette,  # Use the defined color palette
    labels={'Date': '', 'Mentions': ''},  # Empty labels for x and y axes
    title='Media Mentions Over Time',
)

# Customize the x-axis date format
fig.update_xaxes(
    tickformat='%b, %Y',
    tickangle=45,
)

# Remove legend
fig.update_layout(legend_title_text='')

# Show the interactive plot
fig.show()

