import tweepy
import opengraph
from  Pocket import Pocket


twitter_consumer_key = '9LzPjApi2PCIyyL80ronDQs6Z'
twitter_consumer_secret = 'ix8vNqZ7SnGLO8uC96AJfch61zrgXd6Xu8WpJsPH6e2ijbq0Oy' 
twitter_access_token = '118045724-I7aOpcED9HAoZUjbKWuTlBVqCGnJzoIy8NAi0Gzk'
twitter_access_token_secret = 'kINfq5zX256pBWomADEShy8x4FQlSCPR9vOOSwh7ix840'

pocket_consumer_key = '52305-e530cd1f11383695d708bc76'
pocket_access_token = '773939bb-7eed-1f81-5633-c501a2'

max_id = 0
auth = tweepy.OAuthHandler(twitter_consumer_key,twitter_consumer_secret)
auth.set_access_token(twitter_access_token, twitter_access_token_secret)

api = tweepy.API(auth)
q = 'blockchain'
public_tweets = api.search('#' +  q +' -RT filter:links', lang='en', since_id=708178604635480067)
all_urls = []
for tweet in public_tweets:
    tweet = tweet.__dict__
    print tweet['id'] 
    if tweet['id'] > max_id:
       max_id = tweet['id']

    if 'entities' in tweet and 'urls' in tweet['entities']:
      urls = tweet['entities']['urls']
      for url in urls:
          print tweet['text'], url['expanded_url'] 
          all_urls.append( url['expanded_url'])




all_urls = list(set(all_urls))
og_urls = []
for _url in all_urls:
    try :
      page = opengraph.OpenGraph(url = _url)
      print page.url, page.type, page.site_name
      if page.type == 'article' or page.type== 'video':
        og_urls.append(page.url)
    except:
      pass


og_urls = list(set(og_urls))
print og_urls
print "Max id", max_id
pocket = Pocket(pocket_consumer_key, pocket_access_token)
for og_url in og_urls:
   pocket.add(og_url, q)
