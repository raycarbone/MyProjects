try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A lexicon program in python',
    'author': 'Raymond Carbone',
    'url': 'none',
    'download_url': 'none',
    'author_email': 'raycarbone@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'lexicon'
}

setup(**config)
