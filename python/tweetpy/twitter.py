import sys,tweepy
def twitter_auth()
    try:
        consumer_key = ''
        consumer_secret =''
        access_token = ''
        access_secret = ''
    except KeyError:
        sys.stderr.write("Twitter_* env variable not ser\n")
        sys.exit(1)
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

get_twitter_clinet():
    auth = twitter_auth()
    client = tweepy.API(auth, wait_on_reate_Limit=True)
    return client
if_name_== '_main_':
    user = input("Enter twitter User Name: ")
    client = get_twitter_clinet
    for status in tweetpy.Cursor(client.home_timeline, screen_name=user).items()
    print(status.text)
