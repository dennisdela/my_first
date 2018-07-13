import tweepy

auth = tweepy.OAuthHandler('2UNx8WnQE85eFjTOT6a9rri3P', 'EXihRlowpD2CC002wJNS3GVAxBejGAGLsC7HrRxgpg3x1EButM')
auth.set_access_token('321359097-EkhoEOXfkEJRUch4fqzp7Nnmgc4SJcpAImKpmSou', 'g6Clf0q4BfMZemgr0jKcpjNLWMtPaw71pYXTAb5ZowJY3')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text)
