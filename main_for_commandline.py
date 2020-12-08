
import sys
import ticket
import user_interface
import cc_calendar
import datetime
import json

# ----------------------Isaya"s update-------------------

def app_home():
    print("""
----- Welcome to code clinics --------

-use "cs8 help" for more information -
""")


def help():
    print("""
----- code clinics8 -----

To use the code clinics8 program; type cs8 [valid_command].
eg. cs8 view_slots

valid commands:

    register:       Enter the username of your Choice and Password which consist of six or more characters to register

    login:          Enter the registered username and password to access your account

    switch user:    this command changes the App's default user account

    add:            the simplest way of adding a new slot

                        - add [Topic Date Start-time] -
                
                        eg. add robotics 20/12/2020 13:30

    view slots:     Check the available slots

    book slot:      From the added slots book the available slot

    cancel slot:    Cancel a slot

    cancel booking: Remove your booking from a slot

    logout:         blocks all function from working besides the "login, 
                    help, register and switch_user"

    _to view cs8 shortcut commands type: cs8 shortcuts 

""")

def cuts_help():
    print("""
        ---- Shortcut commands---- [to enable these, type: cs8-cuts]

                        cs8-su   >|<   cs8 switch user

                        cs8-a    >|<   cs8 add

                        cs8-vs   >|<   cs8 view slot

                        cs8-bs   >|<   cs8 book slot

                        cs8-cs   >|<   cs8 cancel slot

                        cs8-cb   >|<   cs8 cancel booking

                        cs8-out  >|<   cs8 logout
""")

clinics_valid_argvs = ["login", "register", "view_slots", "book_slot", "cancel_slot", "cancel_booking", "help", "logout", "add_slot", "switch_user",
"add", "slot", "slots", "view", "cancel", "booking","book" , "switch", "user", "main_for_commandline.py", "help", "shortcuts"]


basic = ["help", "login", "register", "shortcuts"]


def switch_user_account():
    ticket.logout()
    login_ = input("Do you want to login now? [Y/n]: ")
    if login_.lower() == "y":
        user_interface.user_login_menu()
        ticket.create_ticket()
        cc_calendar.create_token()
    elif login_.lower() == "n":
        print("Thank You!")
    else:
        print("invalid entry!")
        switch_user_account()

def process_command():
    valid_ticket = ticket.get_the_diff()

    # ---------strictly considering 1 word commands while the ticket is invalid

    # checks if the user exist in the App's database add creates a new 
    # 1hour ticket/token to use the app
    if len(sys.argv) == 2 and valid_ticket == False:
        # add a new user
        if sys.argv[1] == "register":
            user_interface.create_new_user_menu()

        # provides help
        elif sys.argv[1] == "help":
            help()

        elif sys.argv[1] == "shortcuts":
            cuts_help()

        # login to an existing account
        elif sys.argv[1] == "login":
            user_interface.user_login_menu()
            ticket.create_ticket()
            cc_calendar.create_token()

        else:
            print("Please enter a valid command")
    # ---------strictly considering 1 word commands and user logged in
    # provides help
    elif len(sys.argv) == 2 and valid_ticket == True:
        # provides help
        if sys.argv[1] == "help":
            help()

        elif sys.argv[1] == "login":
            print("You are already logged in.")

        elif sys.argv[1] == "shortcuts":
            cuts_help()

        # logout of the current session and user account
        elif sys.argv[1] == "logout":
            ticket.logout()
            print("....logged out of your account")

        else:
            print("Please enter a valid command")
            cc_calendar.store_calendar_details()

    # ----------strictly considering 2 words commands and user logged in
    elif len(sys.argv) == 3 and valid_ticket == True:
        # cancels a slot
        if sys.argv[1] == "cancel" and sys.argv[2] == "slot":
            cc_calendar.display_slots()
            slot_ID = input("Enter slot ID: ")
            cc_calendar.cancel_slot(slot_ID)

        # enables the patient to cancel a slot that they had booked
        elif sys.argv[1] == "cancel" and sys.argv[2] == "booking":
            cc_calendar.display_slots()
            slot_ID = input("Enter slot ID: ")
            cc_calendar.cancel_booking(slot_ID)

        # prints out all slots
        elif sys.argv[1] == "view" and sys.argv[2] == "slots":
            cc_calendar.display_slots()

        # allows the user to book any availabe slots
        elif sys.argv[1] == "book" and sys.argv[2] == "slot":
            cc_calendar.display_slots()
            event_id = input("Enter slot ID: ")
            cc_calendar.book_slot(event_id)

        # switch to a different user account
        elif sys.argv[1] == "switch" and sys.argv[2] == "user":
            user_interface.switch_account()
            switch_user_account()

        else:
            print("Please enter a valid command")
            cc_calendar.store_calendar_details()

    elif len(sys.argv) == 3 and valid_ticket == False:
        
        if sys.argv[1] == "switch" and sys.argv[2] == "user":
            user_interface.switch_account()
            switch_user_account()

        else:
            print("Please enter a valid command")
            cc_calendar.store_calendar_details()

    elif len(sys.argv) == 5 and valid_ticket == True:
        # adds 3 consecutive slots of equal time span of 30 min each 
        if  sys.argv[1] == "add" :

            summary = sys.argv[2] # gets the topic from the second sys arg 
            start_date = sys.argv[3] # gets the start-date from the third sys arg 
            start_time = sys.argv[4] # gets the start-time from the fouth sys arg

            start_time = datetime.datetime.strptime(start_date + " " + start_time, '%d/%m/%Y %H:%M')
            cc_calendar.add_slot(summary, start_time)

        else:
            print("Please enter a valid command")
            cc_calendar.store_calendar_details()

    elif len(sys.argv) > 1 and valid_ticket == False:
        if sys.argv[1] not in basic:
            print("Your last token expired, Please login!")
    else:
        print("Please enter a valid command")


def main():
    
    if len(sys.argv) <= 4 and len(sys.argv) > 1 :
        counter = 0
        for arg in sys.argv:
            arg.lower()   
            if arg != sys.argv[0]:       
                if arg not in clinics_valid_argvs:                
                    counter += 1
    
        if counter > 0:
            print("""

Sorry, some of your commands are invalid!

-use "cs8 help" for more information -
""")
        else:
            process_command()
    

    # this is the home directory of the program, when a user doesn't provide an argument
    elif len(sys.argv) == 5:
        if sys.argv[1] != "add":
            print("""

Sorry, some of your commands are invalid!

-use "cs8 help" for more information -
""")
        else:
            process_command()

    elif len(sys.argv) == 1:
        app_home()


if __name__ == "__main__":
    main()
    