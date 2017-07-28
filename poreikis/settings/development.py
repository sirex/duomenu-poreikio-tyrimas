import socket

from poreikis.settings.base import *  # noqa

DEBUG = True

ALLOWED_HOSTS = [
    socket.gethostname(),
]
