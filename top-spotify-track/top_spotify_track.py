#! /usr/bin/python
from flask import Flask
from flask import render_template
from flask import request
from flask import abort
from flask import jsonify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os, json

app = Flask(__name__)

@app.route('/')
def default_page():
    return render_template('top_spotify_track.html')

@app.route('/find', methods=['POST'])
def find_artist_top_track():
    configpath = os.environ['TOP_SPOTIFY_CONFIG']
    config = {}

    # Load config for client creds
    if os.path.exists(configpath):
        with open(configpath, "r") as f:
            config = json.loads(f.read())
    if not config or not config["spotify_id"] or not config["spotify_secret"]:
        return abort(404)

    client_credentials_manager = SpotifyClientCredentials(client_id=config["spotify_id"], client_secret=config["spotify_secret"])
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    if "artist" not in request.form:
        return abort(404)

    artist_name = request.form['artist']
    artist_results = spotify.search(q='artist:{}'.format(artist_name), type='artist', limit=1)
    if len(artist_results['artists']['items']) > 0:
        artist = artist_results['artists']['items'][0]
        top_track_results = spotify.artist_top_tracks(artist['id'], country='US')
        top_track = top_track_results['tracks'][0]
        track_info = "{}'s top track: {}".format(artist['name'], top_track['name'])
        return jsonify(track_info=track_info, trackId=top_track['id'])
    else:
        return abort(404)

