1.	AIM/OBJECTIVE OF THE PROJECT:
The aim of this project is to develop a Fake News Detection system using Natural Language Processing (NLP) and machine learning techniques,
 which can process textual news data, extract features, train a classifier, and accurately predict whether a news item is “real” or “fake”.

2.	INTRODUCTION:
Fake news has become a major problem in today’s digital world. With the rapid growth of social media platforms and online news sharing,
false information spreads very quickly and can influence people’s opinions, decisions, and beliefs. Traditional methods of identifying
fake news—such as manual verification and fact-checking—are slow and time-consuming. Therefore, there is a need for an automated system
to detect fake news efficiently and accurately. In this project, we use Natural Language Processing (NLP) and Machine Learning techniques
to analyze the content of news articles and classify them as “real” or “fake.” By training a model using published datasets,
the system learns patterns and features from text, allowing it to predict the authenticity of new unseen news data.
This approach can help reduce misinformation and improve trust in online information sources.

3.	DATASET USED:
•  The dataset is in CSV format.
•  It contains news articles with their title, full text content, and whether the article is fake or real.
•  The dataset has 3 main columns and contains multiple rows of different news samples.
> Dataset Columns:
  ColumnName	     Description
  title	         Headline of the news article
  text	         Full article / body text describing the news
  label	         Target class – indicates if the news is fake or real
  >Target Variable:
    Label	Meaning
      1	Fake News
      0	Real News
