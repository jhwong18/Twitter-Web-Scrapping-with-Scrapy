# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TwitterprofilecrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    username = scrapy.Field()
    full_name = scrapy.Field()
    twitter_url = scrapy.Field()
    tweet_text = scrapy.Field()
    tweet_time = scrapy.Field()
    number_of_likes = scrapy.Field()
    no_of_retweets = scrapy.Field()
    no_of_replies = scrapy.Field()
    mentions = scrapy.Field()
    no_of_mentions = scrapy.Field()
    hashtags = scrapy.Field()
    no_of_hashtags = scrapy.Field()
    call_to_action = scrapy.Field()
    image_url = scrapy.Field()
    pass
