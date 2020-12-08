
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

    add:            add [Topic Date start-time], the simpler way of adding 
                    a new slot

    view slots:     Check the available slots

    book slot:      From the added slots book the available slot

    cancel slot:    Cancel a slot

    cancel booking: Remove your booking from a slot

    logout:         blocks all function from working besides the "login, 
                    help, register and switch_user"

    cancel_booking: Remove your booking from a slot
""")

clinics_valid_argvs = ["login", "register", "view_slots", "book_slot", "cancel_slot", "cancel_booking", "help", "logout", "add_slot", "switch_user",
"add", "slot", "slots", "view", "cancel", "booking","book" , "switch", "user", "main_for_commandline.py"]


basic = ["help", "login", "register"]


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
    # view_slots

    if len(sys.argv) > 1 and valid_ticket == True:
        if sys.argv[1] == "view" and sys.argv[2] == "slots":
            cc_calendar.display_slots()

        # book availabe slots
        elif sys.argv[1] == "book" and sys.argv[2] == "slot":
            cc_calendar.display_slots()
            event_id = input("Enter slot ID: ")
            cc_calendar.book_slot(event_id)


        # add a new slot / slots
        elif  sys.argv[1] == "add":
            if len(sys.argv) != 5:
                print("""incorrect format!
                
                - add [Topic Date Start-time] -
                
                eg. add robotics 20/12/2020 13:30
                """)
                return

            summary = sys.argv[2] # gets the topic from the second sys arg 
            start_date = sys.argv[3] # gets the start-date from the third sys arg 
            start_time = sys.argv[4] # gets the start-time from the fouth sys arg

            start_time = datetime.datetime.strptime(start_date + " " + start_time, '%d/%m/%Y %H:%M')
            cc_calendar.add_slot(summary, start_time)

        # cancels a slot
        elif sys.argv[1] == "cancel" and sys.argv[2] == "slot":
            cc_calendar.display_slots()
            slot_ID = input("Enter slot ID: ")
            cc_calendar.cancel_slot(slot_ID)

        # cancels a booking
        elif sys.argv[1] == "cancel" and sys.argv[2] == "booking":
            cc_calendar.display_slots()
            slot_ID = input("Enter slot ID: ")
            cc_calendar.cancel_booking(slot_ID)

        # logout of the current session and user account
        elif sys.argv[1] == "logout":
            ticket.logout()
            print("....logged out of your account")
        
        else:
            print("Please enter valid command")

        cc_calendar.store_calendar_details()


    # provide help
    elif sys.argv[1] == "help":
        help()

    # switch to a different user account
    elif sys.argv[1] == "switch" and sys.argv[2] == "user":
        user_interface.switch_account()
        switch_user_account()        

    # login to an existing account
    elif sys.argv[1] == "login":
        user_interface.user_login_menu()
        ticket.create_ticket()
        cc_calendar.create_token()

    # add a new user
    elif sys.argv[1] == "register":
        user_interface.create_new_user_menu()


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
    