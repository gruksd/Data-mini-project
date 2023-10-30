# Mini-project for Introduction to Data Science course
# Investigating the relationship between presidential candidate media coverage and electoral success
Group members: Sofia Gruk, Mitja Sainio and Mikhail Zolotilin

## Project idea and goal 

In 2023, the topic of Finnish politics has become particularly relevant and pressing for the entire population of the country. The Finnish people have noticeably shifted the direction of political development by voting for parties that were not part of the previous government. These significant changes have led to a special interest in this sphere.
As a result, the upcoming presidential elections have become a very popular subject for discussion and debate in the media. Despite the fact that these elections will only take place in 2024, there is already a large number of official and potential presidential candidates.

Our group has also become interested in the topic of the upcoming presidential elections, specifically how frequently and in what manner this topic is covered in the media. Consequently, we have decided to examine how objectively or subjectively the Finnish media treats the top ten most popular official and potential candidates. Furthermore, we aim to look not only at the frequency of mentions of these candidates but also at the context in which they are mentioned, i.e., whether the context is positive or negative. Ultimately, we want to compare how much the media influences or does not influence public opinion and whether the media's orientation is similar or dissimilar to the opinion of the Finnish people. In other words, our project is long-term, and we will only be able to observe the final results after the presidential elections and the announcement of their results.

Although the election has not yet taken place, we have obtained preliminary results by determining the correlation between a combined metric based on the properties of candidate mentions and the results of a recent presidential poll. We found that the combined metric correlated with the poll results more strongly than the mention frequency and the positivity of the mentions by themselves. The success of this evaluation suggests that our chosen metrics are promising indicators of electoral success.

As our main source of information, we have chosen the YLE https://yle.fi/  media portal for two reasons. Firstly, it is one of the largest Finnish media outlets with a massive audience, and secondly, all articles on YLE are freely accessible, so we had no problems extracting the data we needed.

## Procedures performed

Data Collection

The first thing we had to do for our project was to extract the necessary database. We noticed that on the YLE portal, there are two categories of articles that are suitable for our purposes. Thus, we created a function that reads and extracts the text of articles and their publication date from the internet resources https://yle.fi/uutiset/18-252783 and https://yle.fi/uutiset/18-217902. This function is located in the program called extraction_function.py. Next, in the same program, we transfer all the data we obtained to a text file named article.txt. We used libraries such as BeautifulSoup, Urllib, Re and NLTK for this program.

Data Formatting

After obtaining the necessary database, we needed to format and sort it. We decided that the best format for our data would be a dictionary, where the key would be the candidate's name, and the value would be a list of lists containing the publication date and the sentence in which the candidate is mentioned. This function is presented in the file dataset_farmation.py. For this function, we used libraries such as NLTK and Re.

The First Plot

Next, in the same Python file, you can find a function that creates the first plot. This plot represents the total number of mentions of the candidates we selected, distributed by month. The seaborn, matplotlib.pyplot and datetime libraries were used for this plot.

The Second Plot

The next part of our project was dedicated to creating the second plot. According to our initial idea, the second plot was supposed to be a graph showing the total number of candidate mentions, with the mentions categorized as positive or negative. For this task, we needed to select a relevant model that could perform sentiment analysis on Finnish text. Unfortunately, our attempts were not successful. We then decided to translate all the text into English and use a model that works with English text for sentiment analysis. Accordingly, creating the second plot was divided into three stages: translating our database into English, machine learning, and plotting the resulting data.

Translation

In the file translation_and_sentanalysis.ipynb, all three stages of creating the second plot are performed. First, we translated all the data into English using transformers (AutoTokenizer, AutoModelForSeq2SeqLM).

Machine Learning

Next, we used the cardiffnlp/twitter-roberta-base-sentiment-latest model, which performs sentiment analysis. This model analyzes the probability of positive, negative, and neutral classification for each text. We decided to consider only positive and negative classifications. Accordingly, our program examines all the probabilities calculated by the model and classifies the text based on these probabilities. That is, if the probability of positive content is higher than the negative, the text is classified as positive, and vice versa. We used the Numpy and SciPy libraries for this function. Also in translation_and_sentanalysis.ipynb file.

Plotting

After all these manipulations and obtaining new data, we were able to create the second plot, which includes information about the percentage ratio between positive and negative mentions of the most popular candidates we selected. For this part of our code, we used the matplotlib.pyplot, plotly.express and pandas libraries. This function can be found in the file second_plot.py.

Visualization 

Finally, we thought about visualizing our research and its results. For this purpose, we decided to create a website with a single blog page about our research. For this task, we used the services of our university, specifically the Blogs at HelsinkiUni project, which provides internet pages for course projects. Now, our research can be read at the following link: https://blogs.helsinki.fi/presidential-election-data/.

The Third Plot

We evaluated our results by determining Pearson’s correlation coefficient between the results of a recent Yle presidential poll (Yle News, 13.10.2023, https://yle.fi/a/74-20055215) and each of three metrics. The metrics studied were the frequency of media mentions, percentage of positive media mentions determined by sentiment analysis and finally a product of the two. The correlation coefficients and Plot 3 were produced with the correlation.py program. The program using the nltk, numpy, matplotlib, re and scipy Python libraries.

## Results
1. The first plot can be founs in the file plot1_photos.png.
We can see that the growth and peak of popularity for all candidates occurred in the summer of 2023. It was around that time that potential candidates such as Pekka Haavisto, Alexander Stubb, and Mika Aaltola officially announced their participation in the 2024 presidential elections. As it turns out, the candidate Mika Aaltola experienced the largest increase in mentions in August of that year, precisely when he declared his intentions to run. The smallest peaks in popularity occurred for candidates like Sari Essayah and Harry Harkimo. Interest in them also increased in August of that year but was very low. We observe an interesting statistic for Pekka Haavisto, as interest in him rose in June 2023 (the month he officially announced his candidacy for the Finnish presidency), then declined in July and rose again in August, which coincided with the peak in popularity for all candidates except Olli Rehn, Li Andersson, and Jussi Halla-aho. Rehn and Andersson experienced their popularity peaks in September of this year, while Halla-aho's peak was in July.

2. The second plot can be found in the file plot2_photos.png.
We can see that almost all candidates have approximately 80% positive context and around 20% negative context. Remarkable results were obtained for Sari Essayah, where negative context is mentioned in only 6% of cases. However, it's worth mentioning that this presidential candidate was mentioned less frequently in YLE articles compared to the others. YLE has a more critical attitude towards candidates Jussi Halla-aho and Jutta Urpilainen. They are mentioned in a negative context in almost 30% of cases. It's also noticeable that among the top three candidates mentioned most frequently, the percentage ratio of positive to negative context is almost the same, around 20%.

3. The third plot can be found in the plot3.png file.
The mention frequencies were found to have a fairly high correlation (r = 0.68) with candidate popularity as measured by the presidential poll. The percentages of positive media mentions, on the other hand, had a weak correlation (r = -0.07). A combination of the two metrics created by multiplying the mentions with the percentage of positive mentions, as determined by the sentiment analysis classifier, had the highest correlation of the three (r = 0.69). While the difference between the mention frequency metric and the combined metric is very slight, the latter did show a higher correlation with the results of the presidential poll. Plot 3 shows the correlation between the combined metric and the results of the poll.

## Future Work
Our project is long-term and aimed at analyzing the results of the 2024 presidential elections. In the future, when the public's opinion is known, specifically the election results, we will be able to determine whether it aligns with the opinion of the Finnish media. We can also conduct an analysis of whether the media influenced public opinion. This is the main goal of our project. It is worth mentioning that all the initial objectives of our project have been successfully achieved and realized.





