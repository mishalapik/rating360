import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1pJa9VbRP4arV8mYme-tqosz742Qg5-UGPcFbiEW1zSw'


def sheets_auth(func):
    """
    Decorator for Google Sheets API authentication (obligatory for every function that operates with Google Sheets)
    """

    def wrapper(*args, **kwargs):
        credentials = None
        if os.path.exists('token.json'):
            credentials = Credentials.from_authorized_user_file('token.json', SCOPES)
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                credentials = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(credentials.to_json())
        try:
            service = build("sheets", "v4", credentials=credentials)
            sheets = service.spreadsheets()
            
            # Function that operates straight with Google Sheets (wrapped function)
            # ——————————————————————————————————
            return func(sheets, *args, **kwargs)
            # ——————————————————————————————————
        except HttpError as error:
            print(error)
    return wrapper



@sheets_auth
def check_team(sheets, user_team: str) -> bool:
    """
    Check if the team exists in all teams
    """
    
    Teams_sheet = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range="Teams").execute()
    Members_sheet = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range="Members").execute()
    
    teams: list = Teams_sheet.get('values')
    members: list = Members_sheet.get('values')

    total_teams: int = len(Teams_sheet.get('values')) - 1
    total_members: int = len(Members_sheet.get('values')) - 1

    print(total_teams, total_members)


@sheets_auth
def check_member(sheets, user_team: str) -> bool:
    """
    Check if member exists in members
    """
    
    Teams_sheet = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range="Teams").execute()
    Members_sheet = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range="Members").execute()
    
    teams: list = Teams_sheet.get('values')
    members: list = Members_sheet.get('values')

    total_teams: int = len(Teams_sheet.get('values')) - 1
    total_members: int = len(Members_sheet.get('values')) - 1

    print(total_teams, total_members)