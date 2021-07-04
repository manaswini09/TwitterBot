import tweepy
import time

consumer_key = 'OVcjt5PJKxISubBcha0Ta0naG'
consumer_secret = '1YD3sBapPFKSGQfiBMZK3TtOYFeHU9mJTbNbBv9MGs7PFglmaQ'
key = '1410230280040849415-G2PuwbrgUHoKUlfrd4nuGA912UEUb8'
secret = 'Zn7hZftlDLeZhjPxgnTpTUDHckFoBDwwf4XGTpcwuQruz'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
#api.update_status('Hello again from twitterbot!')

FILE_NAME='last_seen_tweet.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return
def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME),tweet_mode="extended")
    for tweet in reversed(tweets):
        if "#randomtweet" in tweet.full_text.lower():
            print("Replied to ID-" + str(tweet.id))
            api.update_status("@" + tweet.user.screen_name + " Gook Luck!", tweet.id)
            api.create_favorite(tweet.id)
            store_last_seen(FILE_NAME,tweet.id)
while True:
    reply()
    time.sleep(15)


