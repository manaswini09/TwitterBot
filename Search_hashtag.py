import tweepy
import time

consumer_key = 'OVcjt5PJKxISubBcha0Ta0naG'
consumer_secret = '1YD3sBapPFKSGQfiBMZK3TtOYFeHU9mJTbNbBv9MGs7PFglmaQ'
key = '1410230280040849415-G2PuwbrgUHoKUlfrd4nuGA912UEUb8'
secret = 'Zn7hZftlDLeZhjPxgnTpTUDHckFoBDwwf4XGTpcwuQruz'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
hashtag="python"

tweetNumber=3

tweets=tweepy.Cursor(api.search,hashtag).items(tweetNumber)

def searchTweet():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet done!")
            time.sleep(15)
        except tweepy.TweepError as e:
                print(e.reason)
searchTweet()
