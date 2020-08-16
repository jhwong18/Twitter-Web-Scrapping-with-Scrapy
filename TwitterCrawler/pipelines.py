# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2


class TwittercrawlerPipeline(object):

    def open_spider(self, spider):
        hostname = 'localhost'
        username = 'postgres'
        password = '*****'  # your password
        database = 'twitter_tweets'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cur.execute("INSERT INTO profile_tweets(username, full_name, twitter_url, tweet_text, tweet_time, number_of_likes, no_of_retweets, no_of_replies, mentions, no_of_mentions, hashtags, no_of_hashtags, call_to_action, image_url) "
                         "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (item['username'], item['full_name'], item['twitter_url'],
                                                                                 item['tweet_text'], item['tweet_time'], item['number_of_likes'],
                                                                                 item['no_of_retweets'], item['no_of_replies'], item['mentions'],
                                                                                 item['no_of_mentions'], item['hashtags'], item['no_of_hashtags'],
                                                                                 item['call_to_action'], item['image_url']))
        self.connection.commit()
        pass
