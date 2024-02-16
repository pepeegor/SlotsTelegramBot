import gspread
import httplib2
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery


with open("data/table.txt") as inFile:
    temp = inFile.read().split("\n")
    spreadsheet_id = temp[0]
    table_name = temp[1]


def get_cols(credentials_file, table_name):
    gc = gspread.service_account(filename=credentials_file)
    sh = gc.open(table_name)
    worksheet = sh.sheet1
    all_values = worksheet.get_all_values()

    cols = [list(col) for col in zip(*all_values)][0:2]
    cols = [col[1:] for col in cols]

    print(cols)
    return cols


def push_data(user_id, data):
    credentials_file = 'data/creds_bot_1.json'
    spreadsheet_id = temp[0]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
    credentials_file,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = discovery.build('sheets', 'v4', http=httpAuth)
    rows = get_cols(credentials_file, temp[1])
    if data in rows[1]:
        return 2
    if user_id in rows[0]:
        return 1
    values = service.spreadsheets().values().append(
    spreadsheetId=spreadsheet_id,
    range = "A1:B1",
    valueInputOption = "USER_ENTERED",
    body = {
        "range": "A1:B1",
        "majorDimension": "ROWS",
        "values": [[user_id, data]]
    }).execute()
    return 0
