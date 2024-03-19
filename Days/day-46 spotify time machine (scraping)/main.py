import requests, bs4, spotipy; from spotipy.oauth2 import SpotifyClientCredentials;

GETTING_AUTH = False

token = 'BQAw3v3_hOfpAJ2W983YAWaiJLXxNy0h1RER266g9Ad0QANvKqDbOiIAEZ2aqyMkNvH4fN-T4CeUGSVgg0lBBahcnYKCS0APFexSu-bpsoZ5onfJPcNm3axiSBblY0Ui8CWJg78NxyFYsXDeK571EM-dSABHxZHYCLQtpp-BwfqBrwfzniV5i48hcNW1pNzQ8z9SJ0r9YDpGcecvjacAwsXvyVtgeyJSDgTh1JQOKQ'
refresh_token = 'AQCbtQl1wAbv4zBkAJukr0_xpAZWqANBIwkwC_3tsHCI6pNSupLR0VyreL0HpllvPdDl4BJsbDHMbmpbIYS-3VLzQFjnVQtQy4CeRLzQhlGcQGvEt7FLMvNYMzds8IH-dBE'

my_spotify_user_id = '31sdxydrcqxxljkculegb7yf3mz4'

headers = {'Authorization': f'Bearer {token}'}


def main():
    # date = input('What year do you want to travel to? Type the date in this format YYYY-MM-DD: ')
    
    html = get_billboard_html()

    songs = get_songs(html)

    # print(songs)

    playlist_id = create_playlist(date='2000-01-01')

    add_songs_to_playlist(songs, playlist_id)


def spotify_auth():
    sp = spotipy.oauth2.SpotifyOAuth(client_id='7358f96b2f244982ae0227ba3f900528', client_secret='aa680c3f9de44be691d091a0a48ec8c1', redirect_uri='https://example.com', scope="playlist-modify-private")
    data = sp.get_access_token(sp.get_authorization_code())
    token = data['access_token']
    refresh_token = data['refresh_token']

    print('token:', token)
    print('refresh_token:', refresh_token)


def get_current_user():
    res = requests.get('https://api.spotify.com/v1/me', headers=headers)
    print(res.text)
    

def get_billboard_html(date='2000-01-01'):
    res = requests.get(f'https://www.billboard.com/charts/hot-100/{date}/')
    res.raise_for_status()

    return res.text


def get_songs(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')

    songs = [song.text.strip() for song in soup.select("li > ul > li > h3")]
    artists = [artist.text.strip() for i, artist in enumerate(soup.select("li > ul > li > span")) if i % 7 == 0]

    return {song: artists[i] for i, song in enumerate(songs)}


def create_playlist(date):
    body = {
        "name": f"{date} Billboard 100",
        "description": "Travel back in time",
        "public": False
    }

    res = requests.post(f'https://api.spotify.com/v1/users/{my_spotify_user_id}/playlists', json=body, headers=headers)
    res.raise_for_status()
    playlist_id = res.json()['id']

    return playlist_id


def add_songs_to_playlist(songs, playlist_id):
    uris = []
    count = 1
    for song, artist in songs.items():
        query = create_search_query(song, artist)

        params = {
            'q': query,
            'type': 'track',
            'limit': 1,
        }

        search_res = requests.get('https://api.spotify.com/v1/search', params=params, headers=headers)
        search_res.raise_for_status()
        data = search_res.json()

        try:
            song_id = data['tracks']['items'][0]['id']
            uris.append(f'spotify:track:{song_id}')
            print(f'song {count} added to playlist')
            count += 1
        except:
            print(f'No song found, song: {song}, artist: {artist}, query: {query}')

    body = {
        "uris": uris,
        "position": 0
    }

    print(uris)
    print(len(uris))

    print('sending add song to playlist request')

    add_res = requests.post(f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks', json=body, headers=headers)
    add_res.raise_for_status()
    data = add_res.json()
    print(data)


def create_search_query(song_name, artist_name):
    song_name_parts = song_name.split()
    artist_name_parts = artist_name.split()

    # Join the parts with '%2520' for URL encoding
    song_name_encoded = " ".join(song_name_parts)
    artist_name_encoded = " ".join(artist_name_parts)

    search_query = f"track:{song_name_encoded} artist:{artist_name_encoded} year:1950-2010"
    
    return search_query


if __name__ == '__main__':
    if GETTING_AUTH:
        spotify_auth()
    else:
        main()