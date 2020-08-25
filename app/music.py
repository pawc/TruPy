import discogs_client
import config
from discogs_client.exceptions import HTTPError

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

def get_record(id):
    consumer_key = config.consumer_key
    consumer_secret = config.consumer_secret
    oauth_token = config.oauth_token
    oauth_token_secret = config.oauth_token_secret

    user_agent = 'pawc-trupy/2.0'

    discogsclient = discogs_client.Client(user_agent)
    discogsclient.set_consumer_key(consumer_key, consumer_secret)
    discogsclient.set_token(oauth_token, oauth_token_secret)

    try:
        masterRelease = discogsclient.master(id)
        mainRelease = masterRelease.main_release

        artist = mainRelease.artists[0].name
        title = mainRelease.title
        year = mainRelease.year
        label = mainRelease.labels[0].name
        img_url = mainRelease.images[0].get('resource_url')
        tracks = []
        for track in mainRelease.tracklist:
            if track.duration:
                tracks.append(track.title + ' (' + track.duration + ')')
            else:
                tracks.append(track.title)

        return {
            'artist': artist,
            'title': title,
            'year': year,
            'label': label,
            'img_url': img_url,
            'tracks': tracks
        }
    except HTTPError:
        return {
            'artist': 'not found',
            'title': 'not found',
            'year': 'not found',
            'label': 'not found',
            'img_url': 'not found',
            'tracks': 'not found'
        }


def get_artist(id):
    consumer_key = config.consumer_key
    consumer_secret = config.consumer_secret
    oauth_token = config.oauth_token
    oauth_token_secret = config.oauth_token_secret

    user_agent = 'pawc-trupy/2.0'

    discogsclient = discogs_client.Client(user_agent)
    discogsclient.set_consumer_key(consumer_key, consumer_secret)
    discogsclient.set_token(oauth_token, oauth_token_secret)

    result = discogsclient.artist(id)

    name = result.name
    profile = result.profile
    img_url = None
    if result.images is not None and len(result.images) > 0:
        img_url = result.images[0].get('resource_url')

    return {
        'name': name,
        'profile': profile,
        'img_url': img_url
    }

def get_artists(artist):
    artists = []

    consumer_key = config.consumer_key
    consumer_secret = config.consumer_secret
    oauth_token = config.oauth_token
    oauth_token_secret = config.oauth_token_secret

    user_agent = 'pawc-trupy/2.0'

    discogsclient = discogs_client.Client(user_agent)
    discogsclient.set_consumer_key(consumer_key, consumer_secret)
    discogsclient.set_token(oauth_token, oauth_token_secret)

    results = discogsclient.search(q=artist, type='artist')

    for result in results:

        id = result.id
        name = result.name

        obj = {
            'id': id,
            'name': name
        }

        artists.append(obj)

    return artists

def get_releases_by_artistId(artistId):
    releases = []

    consumer_key = config.consumer_key
    consumer_secret = config.consumer_secret
    oauth_token = config.oauth_token
    oauth_token_secret = config.oauth_token_secret

    user_agent = 'pawc-trupy/2.0'

    discogsclient = discogs_client.Client(user_agent)
    discogsclient.set_consumer_key(consumer_key, consumer_secret)
    discogsclient.set_token(oauth_token, oauth_token_secret)

    artist = discogsclient.artist(artistId)

    for result in artist.releases:

        id = result.id
        title = result.title

        obj = {
            'id': id,
            'title': title
        }

        releases.append(obj)

    return releases