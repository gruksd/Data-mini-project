import matplotlib.pyplot as plt

data = {
    'Haavisto': {'positive': 136, 'negative': 28},
    'Stubb': {'positive': 80, 'negative': 25},
    'Rehn': {'positive': 106, 'negative': 23},
    'Aaltola': {'positive': 148, 'negative': 37},
    'Halla-aho': {'positive': 69, 'negative': 26},
    'Andersson': {'positive': 26, 'negative': 6},
    'Urpilainen': {'positive': 40, 'negative': 16},
    'Essayah': {'positive': 15, 'negative': 1},
    'Harkimo': {'positive': 22, 'negative': 5}
}
color_palette = {
    'Haavisto': 'greenyellow',
    'Stubb': 'darkblue',
    'Rehn': 'seagreen',
    'Aaltola': 'lightslategray',
    'Halla-aho': 'skyblue',
    'Andersson': 'indianred',
    'Urpilainen': 'lightcoral',
    'Essayah': 'blueviolet',
    'Harkimo': 'hotpink',
}

names = list(data.keys())
positive_mentions = [entry['positive'] for entry in data.values()]
negative_mentions = [entry['negative'] for entry in data.values()]
total_mentions = [positive + negative for positive, negative in zip(positive_mentions, negative_mentions)]

fig, ax = plt.subplots(figsize=(9, 6))
bar_width = 0.35
index = range(len(names))

bar1 = plt.bar(index, positive_mentions, bar_width, label='Positive', color='green')
bar2 = plt.bar(index, negative_mentions, bar_width, label='Negative', color='red', bottom=positive_mentions)


plt.title('Sentiment Analysis')
label_colors = [color_palette.get(name, 'gray') for name in names]
plt.xticks(index, names, rotation=45, ha="right", fontsize=8)
for label, color in zip(plt.gca().get_xticklabels(), label_colors):
    label.set_color(color)



plt.legend()

# Adding percentage labels with increased distance from bars
label_distance = 1.5  # Adjust this value to increase or decrease the distance
for i in index:
    total = total_mentions[i]
    positive = positive_mentions[i]
    negative = negative_mentions[i]
    percentage_positive = (positive / total) * 100
    percentage_negative = (negative / total) * 100
    plt.text(i, total + label_distance, f'{percentage_negative:.2f}%', ha='center', va='bottom', fontsize=6)
    plt.text(i, -label_distance, f'{percentage_positive:.2f}%', ha='center', va='top', fontsize=6)

plt.tight_layout()
plt.show()

import plotly.express as px
import pandas as pd

data = {
    'Name': ['Haavisto', 'Stubb', 'Rehn', 'Aaltola', 'Halla-aho', 'Andersson', 'Urpilainen', 'Essayah', 'Harkimo'],
    'Positive': [136, 80, 106, 148, 69, 26, 40, 15, 22],
    'Negative': [28, 25, 23, 37, 26, 6, 16, 1, 5],
}

df = pd.DataFrame(data)

fig = px.bar(df, x='Name', y=['Positive', 'Negative'], color_discrete_map={'Positive': 'green', 'Negative': 'red'})
fig.update_layout(
    title='Sentiment Analysis',
    xaxis_title='',
    yaxis_title='',
    xaxis=dict(tickangle=-45, tickfont=dict(size=8)),
    barmode='relative',
)

# Adding percentage labels
for index, row in df.iterrows():
    total = row['Positive'] + row['Negative']
    percentage_positive = (row['Positive'] / total) * 100
    percentage_negative = (row['Negative'] / total) * 100
    fig.add_annotation(
        text=f'{percentage_negative:.2f}%',
        x=row['Name'],
        y=total + 5,  # Adjust this value to control label distance
        showarrow=False,
        font=dict(size=10),
        yshift=10,
    )
    fig.add_annotation(
        text=f'{percentage_positive:.2f}%',
        x=row['Name'],
        y=0 - 5,  # Adjust this value to control label distance
        showarrow=False,
        font=dict(size=10),
        yshift=-10,
    )

fig.show()
