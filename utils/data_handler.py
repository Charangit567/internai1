# utils/data_handler.py

import pandas as pd

def load_data(file):
    """Loads a CSV file and returns it as a DataFrame."""
    return pd.read_csv(file)

def authenticate_google_sheets(credentials_file):
    """Authenticates and returns a Google Sheets API service instance."""
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    
    creds = service_account.Credentials.from_service_account_file(credentials_file)
    service = build("sheets", "v4", credentials=creds)
    return service