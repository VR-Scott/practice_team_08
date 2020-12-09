import pyrebase
from getpass import getpass
import json



firebaseconfig = {

        "apiKey": "AIzaSyBTfl19uzGWTyqWp_rvR28B2hbGNizA9vM",
        "authDomain": "code-clinic-295906.firebaseapp.com",
        "databaseURL": "https://code-clinic-295906.firebaseio.com",
        "projectId": "code-clinic-295906",
        "storageBucket": "code-clinic-295906.appspot.com",
        "messagingSenderId": "439232799728",
        "appId": "1:439232799728:web:723585e4e0e86b2c563335",
        "measurementId": "G-64V37ZCNHN"
    }

#initialise
firebase = pyrebase.initialize_app(firebaseconfig)
auth = firebase.auth()



def register_user():    

    #get user information
    email = input("Please enter your email addresss.\n")
    password = input("Please enter your password")

    auth = firebase.auth()

    """
    Todo: Add emal verification
    """
    try:
        verify = auth.send_email_verification (email)
    except expression as identifier:
        return False

    
    # Registor
    try:
        new_user = auth.create_user_with_email_and_password(email, password)
        return True
    except expression as identifier:
        return False
    
def login_user():
    #sign in
    login =  False
    while login == False:
        #get user information
        email = input("Please enter your email addresss.\n")
        password = input("Please enter your password")
        try:
            new_user = auth.sign_in_with_email_and_password(email, password)
            print("logged in sucessfully, token exprires in 1 hour")
            login = True
        except:
            print("invalid login credentials")
            return False
        if login:
            token = open("./.token.txt", "+w")
            cookie = auth.create
            token.write(new_user['idToken'])
    return login


def verify_token():
    try:
        get_token = open("./.token.txt", "+r")
    except expression as identifier:
        print("An error occured ")
    
    token = str(get_token.read())
    print(token)
    try:
        verify = auth.sign_in_with_custom_token(token)
        return True
    except:
        print("You do not have valid token please login.")
        return False

login_user()
print(verify_token())