# Consumer Sentiment Analysis
**Problem Statement**

Product360 is an end-to-end solution that helps users understand consumer sentiment on a product or service. For example, input a product name, such as Nokia 6.1, and decode 360-degree customer and market behavior. It is a simple solution that can solve multiple business problems and help with making business strategies.

Sentiment analysis involves finding the sentiments score for a given sentence. It categorizes a sentence as positive, negative, or neutral. It captures the public sentiment in reaction to a product or brand, which influences future business decision-making. However, this approach can only classify the texts into a positive, negative, or neutral class. This is not enough method when there are so many possible emotions attached to it. The desired solution to the problem is emotion detection along with sentiment.

Emotion detection involves identifying emotions (sad, angry, happy, etc.) from sentences. Data is extracted from social media like Twitter and Facebook, and e-commerce websites, and processed and analyzed using different NLP and machine learning techniques that provide the 360-degree view of that product, enabling better decision-making.

**Approach Formulation**

There are multiple sentiment prediction libraries, but we do not have the same for emotion detection, which is more robust. We built an emotion classifier. And using the classifier we built and sentiment prediction libraries, we predict the emotion and sentiment of a product using Twitter data. The detailed report is sent to the business team through an automated e-mail.

Data is collected from Twitter by using Twitter search API by specifying the search key. So, tweets related to any product can be used as the testing data. It is also possible to collect date and geolocation data.

Below is a flowchart that explains how the product works at a high level.

![1234](https://github.com/sohansai/Consumer-Sentiment-Analysis/assets/76840110/676b2588-0338-4dff-b8d2-3655199e966f)


**Steps to Solve This Problem**

1. Build an emotion classifier model

2. Twitter data extraction

3. Data preprocessing

4. Emotion prediction

5. Sentiment prediction

6. Visualization and insights

7. Send report via mail


**Building an Emotion Classifier Model**

This model helps us understand the emotions around given sentences and reviews.

**Data for Emotion Classifiers**

To train the emotion classifier, let's use the ISEAR data set. Download the data from [here](https://www.kaggle.com/datasets/psohansai/isear-dataset)




The data set has 7666 phrases classified into seven basic emotions.

The data set classifies joy, anger, fear, disgust, sadness, guilt, and shame.


| Emotion | Sentence |
| ------------- | ------------- |
| Anger  | 1094  |
| Disgust | 1094  |
| Shame | 1094|
| Sadness | 1094|
| Fear | 1093 |
| Joy | 1092 |
| Guilt | 1091 |
|Total| 7652 |

**Real-time Data Extraction**

We want to make a product as real time as possible. To understand the sentiment and emotion of any product, we need public data that is freely available. If we have a retail website,we can fetch data from there. But that's very rare. And we always sell products on someone else's platform. The following are possible ways to collect data.

• Twitter

• Other social media like Facebook and LinkedIn

• E-commerce websites like Amazon

• Company websites

• News articles on companies or products

Getting data from all these data sources is the biggest task. We start with Twitter for now.

