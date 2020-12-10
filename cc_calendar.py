
from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json
from prettytable import PrettyTable


SCOPES = ["https://www.googleapis.com/auth/calendar"]

CAL_ID = "c_if5tihbg7n7a5k5261np66o514@group.calendar.google.com"

# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.

code_calendar = None
creds = None

def create_token():
    """
    Creates the token needed to use and alter the google calendar.
    """
    global creds
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

# Checks if token exists and builds calendar if it does.
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
    code_calendar = build("calendar", "v3", credentials=creds)


def convert_to_RFC_datetime(year=2020, month=1, day=1, hour=0, minute=0):
    dt = datetime.datetime(year, month, day, hour, minute, 0).isoformat() + 'Z'
    return dt


def add_slot(summary, start_time):
    '''
    Creates event/slot on Google calendar.
    '''
    email = get_user_email()

    # Creates start and end time for freebusy to check if timeslot is available.
    end_time = start_time + datetime.timedelta(minutes=90)
    start_str = str(start_time).replace(" ", "T")+"Z"
    end_str = str(end_time).replace(" ", "T")+"Z"
    the_start = start_str

    # Checks if time period is open on Code Clinics calendar
    if free_busy(start_str, end_str) == True:
        print("Slot not available.")
        return

    # Creates three seperate 30 minute slots.
    for i in range(3):
        end_time = start_time + datetime.timedelta(minutes=30)
        start_str = str(start_time).replace(" ", "T")+"Z"
        end_str = str(end_time).replace(" ", "T")+"Z"

        slot_details = {
        "summary": summary,
        "start": {"dateTime": start_str},
        "end":   {"dateTime": end_str},
        "attendees": [{"email": email},
                    {"email": "codeclinic@mail"}],
        }
        slot = code_calendar.events().insert(calendarId=CAL_ID, sendNotifications=True, body=slot_details).execute()
        start_time = end_time


    print('''*** %r event added:
        Start: %s
        End:   %s''' % (slot["summary"].encode("utf-8"),
            the_start, end_str))


def book_slot(eventID):
    
    '''
    Books available slot by adding user email to created event
    '''
    eventID = eventID.strip()
    try:
        email = get_user_email()
        event = code_calendar.events().get(calendarId=CAL_ID, eventId=eventID).execute()
        if len(event["attendees"]) == 2:
            event["attendees"].append({"email": email})
            updated_event = code_calendar.events().update(calendarId=CAL_ID, eventId=event['id'], sendNotifications=True, body=event).execute()
            print("Slot booked successfully.")
    except:
        print("something went wrong when trying to book slot. please make sure the event ID is correct")
    


def display_slots():
    # Gets the time now an then 7 days from now.
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    elapsed = datetime.timedelta(days=7)
    then = (datetime.datetime.utcnow() + elapsed).isoformat() + 'Z'
    time_zone = pytz.timezone("Africa/Johannesburg")

    events_result = code_calendar.events().list(calendarId=CAL_ID, timeMax=then, timeMin=now,
                                            singleEvents=True,
                                            orderBy='startTime').execute()

    events = events_result.get('items', [])
    table = PrettyTable(["Topic", "Start", "ID", "Status"])

    # Displays all events in table format.
    table = PrettyTable(["Topic", "Start", "ID", "Status"])
    status = ""
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        start = start.replace("T", "  ").replace("+02:00", "")
        if len(event["attendees"]) == 2:
            status = "Available"
        elif len(event["attendees"]) == 3:
            status = "Booked"
        table.add_row([event['summary'], start, event["id"], status])
    print(table)


# Delete event by ID
def cancel_slot(eventID):
    event = code_calendar.events().get(calendarId=CAL_ID, eventId=eventID).execute()
    email = get_user_email()
    
    # checks if only codeclinic and slot creator email in attendees
    if len(event["attendees"]) == 2 and event["attendees"][1]["email"] == email:
        code_calendar.events().delete(calendarId=CAL_ID, eventId=eventID).execute()
        print("Slot removed.")
    elif len(event["attendees"]) == 3:
        print("The slot is booked.")
    else:
        print("Not your slot")


def cancel_booking(eventID):
    event = code_calendar.events().get(calendarId=CAL_ID, eventId=eventID).execute()
    email = get_user_email()

    # Checks if slot is booked and removes booking if it is.
    if len(event["attendees"]) == 3:
        for attendee in range(len(event["attendees"])):
            if event["attendees"][attendee]["email"] == email:
                event["attendees"].pop(attendee)
                print("Booking canceled.")
    code_calendar.events().update(calendarId=CAL_ID, eventId=event['id'], body=event).execute()


def store_calendar_details():
    '''
    Creates calendar.json which stores the calendar information.
    '''
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    elapsed = datetime.timedelta(days=7)
    then = (datetime.datetime.utcnow() + elapsed).isoformat() + 'Z'

    events_result = code_calendar.events().list(calendarId=CAL_ID, timeMax=then, timeMin=now,
                                            singleEvents=True,
                                            orderBy='startTime').execute()

    if events_result == []:
        return

    if os.path.exists("calendar.json"):
        with open("calendar.json") as open_calendar:
            calendar_data = json.load(open_calendar)
        if calendar_data == events_result["items"]:
            return
    with open("calendar.json", 'w') as calendar_out:
        json.dump(events_result["items"], calendar_out, indent=4)


def free_busy(start_time, end_time):
    """
    Checks if any events exist during a specified time period.
    """
    body = {
        "timeMin": start_time,
        "timeMax": end_time,
        "timeZone": "Africa/Johannesburg",
        "items": [{"id": CAL_ID}]
    }

    eventsResult = code_calendar.freebusy().query(body=body).execute()
    email = get_user_email()
    
    if eventsResult["calendars"][CAL_ID]["busy"]:
        return True
    else:
        return False


def get_user_email():
    calendar = code_calendar.calendars().get(calendarId='primary').execute()
    return calendar["id"]