from helpers import *
import os

#the cli is the main program this is what we run to start it up, all user interface takes place here 

def main():
    i =0 
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        if i>0:
            print("!!Invalid choice!!")
        main_menu()
        choice = input("> ")
        if choice == "q":
            exit_program()
        elif choice == "1" or choice == "2" or choice == "admin":
            login(choice)
            break
        else:
            i+=1


def login(choice):
    i=0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') # clears the terminal
        if i in range(1, 6):
            print("!!try again!!")
        print("-- q) exit ||m) main menu --")
        print("enter username and password:")  # || 2 to main menu")
        if choice == "1":
            print("    Remember! username must be between 8 and 25 char and password must be over 8 char and must include a capital letter and a number\n")
        user = input("username: ")
        if user == "q":
            exit_program()
        elif user == "m":
            main()
        elif user:
            password = input("password: ")
            if choice == "1":
                verify = register_cust(user, password)
            elif choice == "2":
                verify = cust_login(user, password)
            else:
                verify = admin_login(user, password)
        if verify is True:
            print()
            dashboard(choice, user)
            break    
        else:
            i+=1     

def dashboard(user_type, user):
    i = 0 
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-- q) exit ||m) main menu || 0) back --")
        print(f"Welcome {user}!\n")  
        if i>0:
            print("!!Invalid choice!!")
        if user_type == "1" or user_type =="2":
            customer_cmd()
            choice = input("> ")
            os.system('cls' if os.name == 'nt' else 'clear')
            if choice == "q":
                exit_program()
            elif choice == "m":
                main()
            elif choice == "0":
                login(user_type)
            elif choice == "1":
                pass
            elif choice == "2":
                pass
            elif choice == "3":
                account_settings(user, user_type)
            
            else:
                i+=1
            
def customer_cmd():
    print("Please select an option:")
    print("1. View our gallery")
    print("2. View your gallery")
    print("3. account info")


def admin_cmd():
    print("Please select an option:")
    print("1. Admin controls/account")
    print("2. Art library")
    print("3. Customer list")
    
def account_settings(user, user_type):
    print("Settings")
    print("1. change username") 
    print("2. change password")
    print("3. delete account")
    input("> ")
def main_menu():
    print("-- q) exit --")
    print("Please select an option:")
    print("1. Register new customer")
    print("2. Login")
  









#welcome print interface code
print("Welcome to our gallery!\n\n\n\n\n\n\n\n\n\n\n", )
input("press any key to continue..")
os.system('cls' if os.name == 'nt' else 'clear')
main()