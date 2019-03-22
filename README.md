# Top Spotify Track utilizing Flask framework
In order to run this app, you will need Flask installed, in addition to the spotipy package. You can install all of these packages using pip.

To run the app, please make sure you have configured everything in the **Configuration** section below and run the following commands from the `top-spotify-track` directory:
```
export FLASK_APP=__init__.py
flask run
```

## Tests
To run tests, run the following:
```
python setup.py test
```

## Configuration
To configure this app to access Spotify services, you will need a configuration file. Currently, the configuration file is just a JSON file with a variety of parameters. In order for the app to read from this file, you must declare the following environment variable.
```
TOP_SPOTIFY_CONFIG=/path/to/config.json
```
The configuration file should be a JSON object with the following parameters at the top level of the object:
- spotify\_id: a string denoting the ID for communicating with the Spotify API.
- spotify\_secret: a string denoting the password for the specified Spotify ID.
