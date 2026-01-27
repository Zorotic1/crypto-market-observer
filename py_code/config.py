import os
from dotenv import load_dotenv

#environment loading
load_dotenv() # read variables from .env file, setting it in os.environ

COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY")
API_URL = 'https://api.coingecko.com/api/v3/simple/price'
DB = 'crypto.db'