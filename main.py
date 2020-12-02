import time
from datetime import datetime, timedelta
from app_data import get_input
import user_interface
import cc_calendar
# from user_data.user_storage import *
# from user_data.encryption import encrypt_password
# from user_data.json_handling import *

def help_me():
    help1 = """
        register:   Enter the username of your Choice and Password which consist of six or more characters to register
        login:      Enter the registered username and password to access your account
        exit:       Exit the program as it shutdown
    """
    return help1

def help_me2():
    help2 = """
        add slots :  Add the slots NB: slots can't be duplicated
        view slots:  check the available slots
        book slots:  from the added slots book the available slot
        exit:        Exit the program as it shutdown
    """

    return help2

def add_slots(username):

    #Assign Slot ID
    slots = open("./app_data/slots.txt", "r")
    slots_list = slots.readlines()
    slots.close()
    last = slots_list[-1]
    last = last.split("-")
    last = last[-1]
    ID = int(last) + 1

    # Add slots
    topic = input("please add topic \n >")
    while True:
        if get_input.get_topic(topic):
            break
        else:
            print("Topic can't be blank")
            topic = input("please add topic \n >")
    date = input("please add date (DD/MM/YYYY)\n")
    while True:
        if get_input.get_date(date):
            break
        else:
            date = input("please add date in this format (DD/MM/YYYY)\n")
    time = input("please add time (HH:MM)\n")
    while True:
        if get_input.get_time(time, date):
            break
        else:
            time = input("please add time in this format (HH:MM)\n")

    status = "Available"

    duration = input("duration")
    date = date.split("/")
    print(date)
    #convert to google format
    time = time.split(":")
    Google_date_start = ""
    Google_date_end = ""
    Google_date_start = str(date[2]) + "-" + str(date[1]) + "-" + str(date[0]) + "T" + str(time[0]) + ":" +str(time[1]) + ":00+02:00"
    Google_date_end =  str(date[2]) + "-" + str(date[1]) + "-" + str(date[0]) + "T"+ str(time[0]) + ":" +str(int(time[1]) + int(duration)) + ":00+02:00"
    
    # start_date = datetime.strptime(date + " " + time, '%d/%m/%y %H:%M')
    # end_date = start_date + timedelta(minutes=90)

    cc_calendar.add_slot(topic, Google_date_start, Google_date_end, "thing@mail")

    # Write infor to file
    slots = open("./app_data/slots.txt", "a+")
    slots.write(f"{username}-{topic}-{date}-{time}-{status}-{str(ID)}\n")
    slots.close()
    print("adding slot...")
    print("slot has been added successfully")


def view_slots():
    cc_calendar.display_slots()


def book_slot():
    view_slots()
    book_slot = input("Enter booking id of slot you want to book \n > ")
    
    cc_calendar.book_slot(book_slot, "dude@mail")
    print("slot has been booked successfully")
    


def cancel_slot():
    view_slots()
    slot_id = input("Enter ID of slot you want to cancel\n > ")
    cc_calendar.cancel_event(slot_id)
    print("Slot has been successfully cancelled")


# User session
def session(username):
    print("Welcome to your account " + username)
    print("Menu: view slots | add slot | book slot | cancel slot | logout | help\nmanage slots(not yet available)")
    while True:
        print("What do you want to do next?")
        option = input(username + " > ")
        if option == "logout":
            print("Logging out...")
            break
        elif option == "view slots":
            view_slots()
        elif option == "add slot":
            add_slots(username)
        elif option == "book slot":
            book_slot()
        elif option == "cancel slot":
            cancel_slot()
        elif option == "help":
            print(help_me2())
        elif option == "logout" or option == "exit":
            break
        else:
            print(option + " is not an option")

# On start
print("----- Welcome to code clinics --------")
select = user_interface.main_menu()
if select == 1:
    if user_interface.create_new_user_menu():
        print("redirecting to login page ...")
Auth, username = user_interface.user_login_menu()        
if Auth:
    session(username)
print("Shutting down...")