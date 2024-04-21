#PYTHON DICTIONARY METHOD
#USERNAME AND PASSWORD AUTHENTICATION 
user_login = {
    "person1": "pass1",
    "person2": "pass2",
    "person3": "pass3",
    "person4": "pass4",
    "person5": "pass5",
    "person6": "pass6",
    "person7": "pass7",
    "person8": "pass8",
    "person9": "pass9",
    "person10": "pass10",
}

def login():
    username = input("Username: ")
    password = input("Password: ")

    if username in user_login:
        if user_login[username] == password:
            print("You are now logged in.")
        else:
            print("Invalid password.")
    else:
        print("Invalid username.")

#CALL LOGIN FUNCTION 
login()
    
