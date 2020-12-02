
from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json

SCOPES = ["https://www.googleapis.com/auth/calendar.events"]

CAL_ID = "c_if5tihbg7n7a5k5261np66o514@group.calendar.google.com"

# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
creds = None
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secret.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)


code_calendar = build("calendar", "v3", credentials=creds)

def convert_to_RFC_datetime(year=2020, month=1, day=1, hour=0, minute=0):
    dt = datetime.datetime(year, month, day, hour, minute, 0).isoformat() + 'Z'
    return dt


def add_slot(summary, start_time, end_time, email):
    slot_details = {
    "summary": summary,
    "start": {"dateTime": start_time},
    "end":   {"dateTime": end_time},
    "attendees": [{"email": email}],
    }
    slot = code_calendar.events().insert(calendarId=CAL_ID,sendNotifications=True, body=slot_details).execute()

    print('''*** %r event added:
        Start: %s
        End:   %s''' % (slot["summary"].encode("utf-8"),
            slot["start"]["dateTime"], slot["end"]["dateTime"]))


def book_slot(eventID, email):
    '''need to see if this replaces info or appends'''
    event = code_calendar.events().get(calendarId=CAL_ID, eventId=eventID).execute()
    event["attendees"].append({"email": email})
    updated_event = code_calendar.events().update(calendarId=CAL_ID, eventId=event['id'], sendNotifications=True, body=event).execute()


def display_slots():
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    elapsed = datetime.timedelta(days=7)
    then = (datetime.datetime.utcnow() + elapsed).isoformat() + 'Z'

    events_result = code_calendar.events().list(calendarId=CAL_ID, timeMax=then, timeMin=now,
                                            singleEvents=True,
                                            orderBy='startTime').execute()

    events = events_result.get('items', [])

    with open("calendar.json", 'w') as calendar_out:
        json.dump(events_result, calendar_out, indent=4)

    for event in events:
        # print(event)
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'], event["id"])


# Delete event by ID
def cancel_event(eventID):
    code_calendar.events().delete(calendarId=CAL_ID, eventId=eventID).execute()


def get_details(eventID):
    event = code_calendar.events().get(calendarId=CAL_ID, eventId=eventID).execute()
    # print(len(event["attendees"]))
    print(event["summary"])
    print(event["start"][0]["dateTime"])
    # print(event["attendees"][0]["email"])
    print(event["attendees"])


def get_calendar_details():
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    elapsed = datetime.timedelta(days=7)
    then = (datetime.datetime.utcnow() + elapsed).isoformat() + 'Z'

    events_result = code_calendar.events().list(calendarId=CAL_ID, timeMax=then, timeMin=now,
                                            singleEvents=True,
                                            orderBy='startTime').execute()

    with open("calendar.json", 'w') as calendar_out:
        json.dump(events_result["items"], calendar_out, indent=4)


def get_attendees(eventID):
    event = code_calendar.events().get(calendarId=CAL_ID, eventId=eventID).execute()
    if len(event["attendees"]) == 1:
        return event["attendees"][0]["email"]
    


# start_time = convert_to_RFC_datetime(2020, 11, 20, hour=11)
# end_time = convert_to_RFC_datetime(2020, 11, 20, hour=13)
# add_slot("Loops", start_time, end_time, "guy@mail")
# book_slot("5pvm7n3jb8r17ul2r7unfgot9s", "guy@mail")
display_slots()
# get_events()
# get_details("kv05pc876po491h90cpcdfa86k")
# get_attendees("kv05pc876po491h90cpcdfa86k")