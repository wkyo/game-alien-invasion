import os

RESOURCE_DIR = os.path.join(os.path.dirname(__file__), 'res')


def resource_path(s):
    p = os.path.join(RESOURCE_DIR, s)
    return os.path.normpath(p)
