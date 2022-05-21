import boto3
import pandas as pd
import csv
import spotipy
import time
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import datetime

client_id = "a7f8f07e56c64ac29377a2061370278d"
client_secret = "4980329f86444c3fa5a49dd1d2b7373b"


auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f"
playlist_URI = playlist_link.split("/")[-1].split("?")[0]
track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

def getTrackIDs(user, playlist_id):
    ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids

ids = getTrackIDs('kai', '37i9dQZF1DX0XUsuxWHRQd')

def getTrackFeatures(id):
  meta = sp.track(id)
  features = sp.audio_features(id)

  # meta
  name = meta['name']
  album = meta['album']['name']
  artist = meta['album']['artists'][0]['name']
  release_date = meta['album']['release_date']
  length = meta['duration_ms']
  popularity = meta['popularity']

  # features
  acousticness = features[0]['acousticness']
  danceability = features[0]['danceability']
  energy = features[0]['energy']
  instrumentalness = features[0]['instrumentalness']
  liveness = features[0]['liveness']
  loudness = features[0]['loudness']
  speechiness = features[0]['speechiness']
  tempo = features[0]['tempo']
  time_signature = features[0]['time_signature']

  track = [name, album, artist, release_date, length, popularity, danceability, acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]
  return track

  # loop over track ids 
tracks = []
for i in range(len(ids)):
  time.sleep(.5)
  track = getTrackFeatures(ids[i])
  tracks.append(track)

# create dataset
df = pd.DataFrame(tracks, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
df.to_csv("spotify.csv", sep = ',')








# def get_artist_from_playlists(playlist_uri):
#     '''
#     :param playlist_uri: PLaylist to analyse
#     :return: A dictionary(artist_uri : artist name) of all primary aritist in a playlist
#     '''
#     artist = {}
#     playlist_tracks = spotipy.playlist_tracks(playlist_id=playlist_uri)
#     for song in playlist_tracks['items']:
#         if song['track']:
#             print(song['track']['artists'][0]['name'])
#             artist[song['track']['artists'][0]['uri']] = song['track']['artist'][0]['name']
#     return artist





# # PLAYLIST = 'rap_caviar'
# def gather_data_local(): # For every artist we are looking for
#     with open("rapcaviar_albums.csv", "w") as file:
#         header = list(final_data_dictionary.key())
#         writer = csv.DictWriter(file, fieldnames=header)
#         writer.writeheader()
#         albums_obtained = []

#         artists = get_artists_from_playlists(spotify_playlists()[PLAYLIST])


#         def get_artist_from_playlists(playlist_uri):
#             '''
#             :param playlist_uri: PLaylist to analyse
#             :return: A dictionary(artist_uri : artist name) of all primary aritist in a playlist
#             '''
#             artist = {}
#             playlist_tracks = spotipy.playlist_tracks(playlist_id=playlist_uri)
#             for song in playlist_tracks['items']:
#                 if song['track']:
#                     print(song['track']['artists'][0]['name'])
#                     artist[song['track']['artists'][0]['uri']] = song['track']['artist'][0]['name']
#             return artist


