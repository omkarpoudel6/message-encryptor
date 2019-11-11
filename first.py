import re

regex = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
def validateemail(email):

    if re.search(regex,email):
        return 1
    else:
        return 0

def passcheck(pass1,pass2):
    if pass1==pass2:
        return 1
    else:
        return 0

def login():
    username=input("Username: ")
    password=input("Password: ")

def Register():
    email = input("Email: ")
    username = input("Username: ")
    password = input("Password: ")
    password2 = input("Re Enter Password: ")
    vemail = validateemail(email)
    vpass = passcheck(password, password2)
    if (vemail == 1 and vpass == 1):
        print("Registered")
    else:
        print("Email or Password donot match")

print("Enter Your Choice")
choice=int(input("1. Login\n2. Register"))
if choice==1:
    login()
elif choice==2:
    Register()