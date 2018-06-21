import sys

import psutil

from random import choices
from string import ascii_lowercase

from requests import Response, session, Session

from .config import DEFAULT_PORT, DEFAULT_ORIGIN

s: Session = session()


def get_url(url):
    """Ranomdly generates a url for use in requests.
    Generates a hostname with the port and the provided suffix url provided

    :param url: A url fragment to use in the creation of the master url
    """
    sub = "{0}.spotilocal.com".format("".join(choices(ascii_lowercase, k=10)))
    return "http://{0}:{1}{2}".format(sub, DEFAULT_PORT, url)


def get_oauth_token():
    """Retrieve a simple OAuth Token for use with the local http client."""
    url = "{0}/token".format(DEFAULT_ORIGIN["Origin"])
    r = s.get(url=url)
    return r.json()["t"]


def get_csrf_token():
    """Retrieve a simple csrf token for to prevent cross site request forgery."""
    url = get_url("/simplecsrf/token.json")
    r = s.get(url=url, headers=DEFAULT_ORIGIN)
    return r.json()["token"]


def is_spotify_running():
    procs = [p.name() for p in psutil.process_iter()]
    if sys.platform == "win32":
        return "Spotify.exe" in procs


def is_spotify_web_helper_running():
    procs = [p.name() for p in psutil.process_iter()]
    if sys.platform == "win32":
        return "SpotifyWebHelper.exe" in procs

