import socket

from poreikis.settings.base import *  # noqa

DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    socket.gethostname(),
]
