import datetime
import time
import os


# global var
time_difference_capture = datetime.datetime.today()
# time_difference_capture

# create a new ticket
def logout():
    expired_ticket = "2020-11-16 15:40:32.045747"
    ticket = open("app_data/ticket.txt", "a+")
    ticket.write(f"{expired_ticket}\n")
    ticket.close()


def create_ticket():

    # add current time to the ticket.txt file
    ticket = open("app_data/ticket.txt", "a+")
    ticket.write(f"{datetime.datetime.today()}\n")
    ticket.close()

    get_the_diff()
    remaining_time()




def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `-.,:/`
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_time_to_list(datetime_stamp):
    return list(filter(lambda x: x != '', split("-.,:/ ", datetime_stamp)))


def get_the_diff():
    global time_difference_capture


    unwanted = ['\n']
    usable_ticket = ''
    # open and read the tickets file
    tickets_file = open("app_data/ticket.txt", "r")
    tickets = tickets_file.readlines()
    tickets_file.close()

    # get the latest ticket
    latest_ticket = tickets[len(tickets)-1]
    

    # filter the ticket to remove the \n chars
    latest_ticket_filtered = list(filter(lambda char: char not in unwanted, latest_ticket))
    
    for char in latest_ticket_filtered:
        usable_ticket += char

    # get the current time and convert it to a list
    now = datetime.datetime.today()
    

    # calculate the difference between the latest ticket and the current time
    ticket_time = datetime.datetime.strptime(usable_ticket, '%Y-%m-%d %H:%M:%S.%f')

    # min30 = "01:00:0.000000"

    time_diff = now - ticket_time 

    time_difference_capture = ticket_time

 
    
    time_diff = convert_time_to_list(str(time_diff))

    if len(time_diff) == 4:
        if int(time_diff[0]) > 0:
<<<<<<< HEAD
            print("Your last ticket expired, please login")
            # if os.path.exists("token.pickle"):
            #     os.remove("token.pickle")
=======
            print("The last token expired, please login")
            if os.path.exists("token.pickle"):
                os.remove("token.pickle")
>>>>>>> master
            return False
        else:
            return True

    elif len(time_diff) > 4:
        print("Your last ticket expired, please login")
        if os.path.exists("token.pickle"):
            os.remove("token.pickle")
        return False
    
    print("something went wrong with the programme files, please contact the developer for assistance")
    return False

def remaining_time():
    global time_difference_capture
    get_the_diff()
    # this code calculates the remaining time
    t_d_c = list(str(time_difference_capture))

    if int(t_d_c[12]) < 9:
        t_d_c[12] = int(t_d_c[12]) + 1
    
    elif int(t_d_c[12]) == 9:
        t_d_c[11] = int(t_d_c[11]) + 1
        t_d_c[12] = 0

    time_string = ""
    for char in t_d_c:
        time_string += str(char)

    time_string_time = datetime.datetime.strptime(str(time_string), '%Y-%m-%d %H:%M:%S.%f')
    countdown = time_string_time - datetime.datetime.today()
    # print("your current date and time: " + str(datetime.datetime.today()))
    days = countdown.days
    hours = int(countdown.total_seconds()/60**2)
    minutes = int(countdown.total_seconds()/60)
    seconds = int(countdown.total_seconds())

    print(f"Your token expires in {days} days {hours} hours {minutes} minutes at {time_string_time} +02:00")

<<<<<<< HEAD
    return time_string, time_string_time

#  create_ticket()
=======
    return time_string, time_string_time
>>>>>>> master
