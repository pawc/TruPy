import discogs_client
import config

def get_releases(artist):
    releases = []

    consumer_key = config.consumer_key
    consumer_secret = config.consumer_secret
    oauth_token = config.oauth_token
    oauth_token_secret = config.oauth_token_secret

    user_agent = 'pawc-music/2.0'

    discogsclient = discogs_client.Client(user_agent)
    discogsclient.set_consumer_key(consumer_key, consumer_secret)
    discogsclient.set_token(oauth_token, oauth_token_secret)

    results = discogsclient.search(type='master', artist=artist)

    for result in results:
        releases.append(result.title)

    return releases