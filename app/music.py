import discogs_client
import config

def get_releases(artist):
    releases = []

    consumer_key = config.consumer_key
    consumer_secret = config.consumer_secret
    oauth_token = config.oauth_token
    oauth_token_secret = config.oauth_token_secret

    user_agent = 'pawc-trupy/2.0'

    discogsclient = discogs_client.Client(user_agent)
    discogsclient.set_consumer_key(consumer_key, consumer_secret)
    discogsclient.set_token(oauth_token, oauth_token_secret)

    results = discogsclient.search(type='master', artist=artist)

    for result in results:

        id = result.id
        title = result.title

        obj = {
            'id': id,
            'title': title
        }

        releases.append(obj)

    return releases

def get_release(id):
    consumer_key = config.consumer_key
    consumer_secret = config.consumer_secret
    oauth_token = config.oauth_token
    oauth_token_secret = config.oauth_token_secret

    user_agent = 'pawc-trupy/2.0'

    discogsclient = discogs_client.Client(user_agent)
    discogsclient.set_consumer_key(consumer_key, consumer_secret)
    discogsclient.set_token(oauth_token, oauth_token_secret)

    masterRelease = discogsclient.master(id)
    mainRelease = masterRelease.main_release

    artist = mainRelease.artists[0].name
    title = mainRelease.title
    year = mainRelease.year
    label = mainRelease.labels[0].name
    img_url = mainRelease.images[0].get('resource_url')

    return {
        'artist': artist,
        'title': title,
        'year': year,
        'label': label,
        'img_url': img_url
    }