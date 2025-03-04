import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.service_account import Credentials

SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDS = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", SCOPE)
CLIENT = gspread.authorize(CREDS)

SHEET_ID = "1MYzCg00iIZLSYwg_AR-5_EUx018H2xuvolcyqRa_WlA"
SHEET_NAME = "HINDALCO"

def fetch_data():
    sheet = CLIENT.open_by_key(SHEET_ID).worksheet(SHEET_NAME)
    data = sheet.get_all_records()
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = fetch_data()
    print(df.head())

