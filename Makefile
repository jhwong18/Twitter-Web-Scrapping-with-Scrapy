#################################################################################
# COMMANDS                                                                      #
#################################################################################

crawl_profile:
	scrapy crawl TwitterCrawler -a filename=input/profile_input.csv

# crawl_hashtag:
#	scrapy crawl twittercrawler -a filename=input/hashtag_input.csv -o output/hashtag_output.csv
