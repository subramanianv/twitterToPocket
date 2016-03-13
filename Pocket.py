import requests
class Pocket:
  def __init__(self, consumer_key, access_token) :
     BASE_URL =  'https://getpocket.com/v3'
     self.access_token = access_token
     self.consumer_key = consumer_key
     self.API_ENDPOINTS = {
       'add' : BASE_URL + '/add'
     } 
  def add(self, url, tags=None):
      payload = {
         'access_token' : self.access_token,
         'consumer_key' : self.consumer_key,
         'url' : url
      }
      if tags is not None:
         payload['tags'] = tags
      requests.post(self.API_ENDPOINTS['add'], payload)
