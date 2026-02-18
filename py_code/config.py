import os
from dotenv import load_dotenv

#environment loading
load_dotenv() # read variables from .env file, setting it in os.environ

COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY")
API_URL = 'https://api.coingecko.com/api/v3/coins/markets'
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")