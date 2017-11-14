import ConfigParser
import json

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API


config = ConfigParser.ConfigParser()
config.read('twitter.conf')

## Consumer
consumer_key = config.get('apikey', 'key')
consumer_secret = config.get('apikey', 'secret')
## Token
access_token = config.get('token', 'token')
access_token_secret = config.get('token', 'secret')

print ("==> Start Listening with:")
print ("====> Consumer Key: " + consumer_key)
print ("====> Consumer Secret: " + consumer_secret)
print ("====> Access Token: " + access_token)
print ("====> Access Token Secret: " + access_token_secret)


## Configure access
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitterApi = API(auth)

## Users
USERS = config.get('accounts', 'accounts').split(',')
USERS_id = []

print ("====> Accounts IDs:")
for actual_user in USERS:
    user = twitterApi.get_user(actual_user)
    user_id = str(user.id_str)
    USERS_id.append(user_id)
    print ("                     " + actual_user + " - ID: " + user_id)

print ('\n')

class StartStreamingRT(StreamListener):

    def on_data(self, status):
        tweet = json.loads(status.strip())

        tweetId = tweet.get('id_str')
        retweeted = tweet.get('retweeted')

        ## Tweet not empty
        if tweetId is not None:
            try: 
                twitterApi.retweet(tweetId)
                print tweet

                print ('\n')
                print ("   ==========================")
                print ('\n')
            except:
                print ('\n')

    def on_error(self, status):
        print status

        print ('\n')
        print ("   ==========================")
        print ('\n')
        if status == 420:
            #returning False in on_data disconnects the stream
            return False


if __name__ == '__main__':
    ## Start streaming
    streamListener = StartStreamingRT()
    twitterStream = Stream(auth, streamListener)

    #twitterStream.filter(follow=['721871893150744576'])
    twitterStream.filter(follow=USERS_id)