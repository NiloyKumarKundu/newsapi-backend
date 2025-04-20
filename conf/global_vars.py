import os
import importlib
from dotenv import load_dotenv
load_dotenv()


APPS = ["auth", "newsapi"]


# POSTGRES DB
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_NAME = os.getenv('POSTGRES_NAME')
POSTGRES_USERNAME = os.getenv('POSTGRES_USERNAME')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')


# MISC
DEFAULT_TIMEZONE = os.getenv('DEFAULT_TIMEZONE', 'UTC')
JWT_SECRET = os.getenv('JWT_SECRET', 'test')

# NEWS API
NEWS_API_ENDPOINT = os.getenv('API_ENDPOINT', 'https://newsapi.org/v2/everything')
NEWS_API_KEY = os.getenv('NEWS_API_KEY', 'test')
