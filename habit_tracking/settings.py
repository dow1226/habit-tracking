import os
from dotenv import load_dotenv

load_dotenv()

PIXELA_APIKEY = os.getenv('PIXELA_APIKEY')
PIXELA_USERNAME = os.getenv('PIXELA_USERNAME')