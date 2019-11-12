import re
import sys

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
    '''username=input("Username: ")
    password=input("Password: ")'''
    print("Enter Your Choice: ")
    choice=int(input("1: Encryption\n2: Decryption\n3: Exit"))
    if choice==1:
        print("########### Welcome to Message Encryption ############")
        message=input("Enter Your Message: ")
        image=input("Enter The Path of Your Image In Which You Want To Encrypt Your Message: ")
        for i in range(1,10):
            print("!"*i)
        print("Message Was Sucessfully Encrypted")
        login()
    elif choice ==2:
        print("########### Welcome to Message Decryption ############")
        image=input("Enter The Path of The Image You Want To Decrypt")
        for i in range(1,10):
            print("!"*i)
        print("Message Was Sucessfully Decrypted")
        login()
    elif choice==3:
        sys.exit()
    else:
        print("Wrong Input Entered!!!")
        login()


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
def first():
    print("Enter Your Choice")
    choice=int(input("1. Login\n2. Register"))
    if choice==1:
        login()
    elif choice==2:
        Register()
    else:
        print("Wrong Input Entered!!!!")
        first()

first()