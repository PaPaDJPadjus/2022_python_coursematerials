"""Api v hoopis Appi."""
from __future__ import print_function

import os.path

import google_auth_oauthlib
import googleapiclient
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SAMPLE_RANGE_NAME = 'A1:Z'
scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def get_links_from_spreadsheet(id: str, token_file_name: str) -> list:
    """
    Return a list of strings from the first column of a Google Spreadsheet with the given ID.

    Example input with https://docs.google.com/spreadsheets/d/1WrCzu4p5lFwPljqZ6tMQEJb2vSJQSGjyMsqcYt-yS4M
        get_links_from_spreadsheet('1WrCzu4p5lFwPljqZ6tMQEJb2vSJQSGjyMsqcYt-yS4M', 'token.json')

    Returns
        ['https://www.youtube.com/playlist?list=PLPszdKAlKCXUhU3r25SOFgBxwCEr-JHVS', ... and so on]
    """
    final_list_of_links = []
    creds = None
    if os.path.exists(token_file_name):
        creds = Credentials.from_authorized_user_file(token_file_name, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'Credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_file_name, 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=id,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values')

        if not values:
            print('No data found.')
            return

        for row in values:
            for link in row:
                final_list_of_links.append(link)
    except HttpError as err:
        print(err)

    return final_list_of_links


def get_links_from_playlist(link: str, developer_key: str) -> list:
    """
    Return a list of links to songs in the Youtube playlist with the given address.

    Example input
        get_links_from_playlist('https://www.youtube.com/playlist?list=PLFt_AvWsXl0ehjAfLFsp1PGaatzAwo0uK',
                                'ThisIsNotARealKey_____ThisIsNotARealKey')

    Returns
        ['https://youtube.com/watch?v=r_It_X7v-1E', 'https://youtube.com/watch?v=U4ogK0MIzqk', ... and so on]
    """
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    list_of_links = []
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyCGrpTOTFZG1AYHeWPDSJuREEotIk5uqSo"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    request = youtube.playlistItems().list(
        part="contentDetails",
        playlistId="PLFt_AvWsXl0ehjAfLFsp1PGaatzAwo0uK"
    )

    response = request.execute()

    while len(list_of_links) != response["pageInfo"]["totalResults"]:
        for el in response["items"]:
            for content_dict_key in el["contentDetails"]:
                vid_id = el["contentDetails"][content_dict_key]
                full_link = f"youtube.com/watch?v={vid_id}"
                list_of_links.append(full_link)
                break

        token = response.get("nextPageToken", None)
        request = youtube.playlistItems().list(
            part="contentDetails",
            pageToken=token,
            playlistId="PLFt_AvWsXl0ehjAfLFsp1PGaatzAwo0uK"
        )
        response = request.execute()

    return list_of_links

