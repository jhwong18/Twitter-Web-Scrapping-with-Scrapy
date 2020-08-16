# Twitter Web Scraping via Scrapy

# Requirements
* scrapy
* dateutils


# Objective 

Twitter is one of the most popular social media platforms for political news and opinions. In many cases, the political news are first released in Twitter than in traditional news outlets. Our objective is to analyse the polarity of tweets from politicians and political supporters based on their realtime tweets.
To achieve this, we will first need to scrape realtime tweets from Twitter of the profiles of politicans and a small group of randomly sampled followers of the politicians. In this repository, we have automated the process of scraping realtime tweets from any twitter profile and parse these tweets (tweet_url, tweet_text, comments, retweets, etc) into a Postgres SQL database.
This will allow us to perform ETL on the data and subsequently perform sentimental analysis to study the polarity of tweets across politicians and political supporters.

# Overview
This repository begins with the data processing (lowercase, remove punctuation, etc) and carry out an exploratory data analysis (such as unique word count in each headline, total word length for headline, use of numbers/statistics in headline, etc). To understand the topics of headline, Latent Dirichlet Allocation (LDA) is also used. Before running the LDA model, the necessary steps of tokenization, stop word removal, removal of headlines with a short length, lemmatization, stemming are carried out. For the task of predicting sarcastic headlines, various Recurrent Neural Network (RNN) architectures are used. For example, RNN with Gated Recurrent Unit or RNN with Long Short Term Memory, Convolutional Neural Networks using only 1-Dimensional Convolutional Layer (Conv1D), and finally a combination of CNN and RNN. Based on the performance on the test set, the combined architecture of CNN-RNN performs the best, at 86% accuracy. Further fine-tuning of the model will help to improve this performance. 

# Using the Package

## Set up SQL Server

Ensure that you have setup a SQL server, database and tables. In our example, we have set up a Postgres server with a database `twitter_tweets` and table `profile_tweets`.
The commands used to create the database and table is found in `Postgres SQL.txt`

## Verify the crawler spider exists

```sh
scrapy list
```

## Makefile

To run the package using `Makefile`, simply run the following commands below:

```
crawl_profile
```


## Data Columns of Tweets
* username
* full_name
* twitter_url
* tweet_text
* tweet_time
* number_of_likes
* no_of_retweets
* no_of_replies
* mentions
* no_of_mentions
* hashtags
* no_of_hashtags
* call_to_action
* image_url


### Speeding up the crawls
If you feel like the crawler is a little slow then find the hashtag.py file in the project and edit the custom settings.
```py
custom_settings = {
    'USER_AGENT': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Safari/537.36',
    'CONCURRENT_REQUESTS': 2, 'DOWNLOAD_DELAY': 1, 'LOG_LEVEL': 'INFO'}
```
> Here CONCURRENT_REQUESTS is the number of URLs that will be processed parallelly and DOWNLOAD_DELAY is a wait between each  request. So, Increase CONCURRENT_REQUESTS and decrease DOWNLOAD_DELAY (minimum value for download delay is 0).


# References:
[1] Amit Upreti Github Repository on Web Scraping: https://github.com/amitupreti/Hands-on-WebScraping
