import os
from dotenv import find_dotenv, load_dotenv
import json

load_dotenv(find_dotenv())

TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')