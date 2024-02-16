import os
from dotenv import find_dotenv, load_dotenv
import json

load_dotenv(find_dotenv())

file_ids = {"confirm_username": "CgACAgIAAxkDAAIBAAFlz0MaEkbTjEr1xtbBDlPjtvo6VAAC0EgAAveFeUqWdNWgA4vX-zQE",
            "confirm_slot": "CgACAgIAAxkDAAIBA2XPQ1AbZm3r3Omtu7STfsxjNDV3AALZSAAC94V5So9vOiZgBL70NAQ",
            "confirm_request": "CgACAgIAAxkDAAIBKWXPSIWaKSWes9-rKdfU565DwFN7AAIWSQAC94V5SqwLNYnszvI5NAQ"
            }

TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
TABLE_ID = os.getenv('TABLE_ID')
TABLE_NAME = os.getenv('TABLE_NAME')