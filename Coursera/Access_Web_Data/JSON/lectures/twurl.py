import urllib.request, urllib.parse, urllib.error
import hidden

# https://apps.twitter.com/
# Creat app and get the four strings, put them in hidden.py

def augment(url, parameters):
    secrets = hidden.oauth()
    consumer = hidden.oauth.OAuthConsumer(secrets['8tkMOwumyrY69lPuEkONWx9Hm'],
                                    secrets['l0LzL5qesRvhOiLdvHB7H17jO7JYPP6ED7s9m5qe5jV2r4Wa19'])
    token  = hidden.oauth.OAuthToken(secrets['AAAAAAAAAAAAAAAAAAAAANgfYQEAAAAAo0F7YvlpJ47dxLZMVpHWA4jvE4Y'])

    oauth_request = hidden.oauth.OAuthRequest.from_consumer_and_token(consumer,
                    token=token, http_method='GET', http_url=url,
                    parameters=parameters)
    oauth_request.sign_request(hidden.oauth.OAuthSignatureMethod_HMAC_SHA1(),
                                consumer, token)
    return oauth_request.to_url()
