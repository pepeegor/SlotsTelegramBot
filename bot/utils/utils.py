import asyncio
import json

import gspread
import httplib2
from aiogram.client.session import aiohttp
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery

from bot.data.config import TABLE_ID, TABLE_NAME


import requests
from google.oauth2.service_account import Credentials
from google.auth.transport.requests import Request


async def get_cols(credentials_file, spreadsheet_id):
    creds = Credentials.from_service_account_file(credentials_file,
                                                  scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"])
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, creds.refresh, Request())
    async with aiohttp.ClientSession() as session:
        headers = {"Authorization": f"Bearer {creds.token}"}
        url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/A:B"
        async with session.get(url, headers=headers) as response:
            result = await response.json()
            cols = [list(col) for col in zip(*result.get('values', []))][0:2]
            cols = [col[1:] for col in cols]  # Удаление заголовков первой строки
            print(cols)
            return cols


async def push_data(user_id, data):
    credentials_file = 'bot/data/creds_bot_1.json'
    spreadsheet_id = "1oYDBrNnH9z010ZucKgEnKYHCR0YcrR0n_r6YPk2jlB4"
    creds = Credentials.from_service_account_file(credentials_file,
                                                  scopes=["https://www.googleapis.com/auth/spreadsheets"])
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, creds.refresh, Request())

    cols = await get_cols(credentials_file, spreadsheet_id)
    if len(cols) > 1 and any(data == row for row in cols[1]):
        return 2
    if len(cols) > 0 and any(user_id == row for row in cols[0]):
        return 1

    async with aiohttp.ClientSession() as session:
        headers = {"Authorization": f"Bearer {creds.token}", "Content-Type": "application/json"}
        url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/A:B:append?valueInputOption=USER_ENTERED"
        body = {"values": [[user_id, data]]}
        print()
        async with session.post(url, headers=headers, data=json.dumps(body)) as response:
            if response.status == 200:
                return 0  # Успешно добавлено
            else:
                return -1  # Ошибка при добавлении данных
