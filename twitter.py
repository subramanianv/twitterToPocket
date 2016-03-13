import tweepy
import opengraph
from  Pocket import Pocket
import json


with open('credentials.json') as c_file:
   credentials = json.load(c_file)





max_id = 0
auth = tweepy.OAuthHandler(credentials['twitter']['consumer_key'],credentials['twitter']['consumer_secret'])
auth.set_access_token(credentials['twitter']['access_token'], credentials['twitter']['access_token_secret'])


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
pocket = Pocket(credentials['pocket']['consumer_key'], credentials['pocket']['access_token'])
for og_url in og_urls:
   pocket.add(og_url, q)
