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

import numpy
import matplotlib
import matplotlib.pyplot as plt
from scipy import stats

mention_scores = {name: sum(plotting_data[name].values()) for name in plotting_data}
sentiment_scores = {"Pekka Haavisto": 0.8293, "Alexander Stubb": 0.7619, "Olli Rehn": 0.8217,
                    "Mika Aaltola": 0.8, "Jussi Halla-aho": 0.7263, "Li Andersson": 0.8125,
                    "Jutta Urpilainen": 0.7143, "Sari Essayah": 0.9375, "Harry Harkimo": 0.8148}
combined_scores = [mention_scores[name]*sentiment_scores[name] for name in name_list]
# Source for poll scores: https://yle.fi/a/74-20055215
poll_scores = {"Pekka Haavisto": 0.29, "Alexander Stubb": 0.22, "Olli Rehn": 0.14,
               "Mika Aaltola": 0.1, "Jussi Halla-aho": 0.08, "Li Andersson": 0.07,
               "Jutta Urpilainen": 0.03, "Sari Essayah": 0.02, "Harry Harkimo": 0.02}

mention_values = [x for x in mention_scores.values()]
sentiment_values = [x*100 for x in sentiment_scores.values()]
poll_values = [x*100 for x in poll_scores.values()]

r1 = numpy.corrcoef(mention_values, poll_values)
r2 = numpy.corrcoef(sentiment_values, poll_values)
r3 = numpy.corrcoef(combined_scores, poll_values)

print()
print("mention frequencies\t", r1[0][1])
print("sentiment analysis\t", r2[0][1])
print("combined\t\t", r3[0][1])

slope, intercept, r, p, std_err = stats.linregress(combined_scores, poll_values)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, combined_scores))

plt.scatter(combined_scores, poll_values)
plt.plot(combined_scores, mymodel)
plt.xlabel("Candidate score")
plt.ylabel("Popularity in poll %")
plt.show()
