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
        if isinstance(verify, (Customer,Admin)):             
            dashboard(verify)  
        else:
            i+=1

def dashboard(user):
    i = 0 
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-- q) exit ||m) log out || 0) back --")
        print(f"Welcome {user.username}!\n")  
        if i>0:
            print("!!Invalid choice!!")
        if isinstance(user, Customer):
            customer_cmd()
            choice = input("> ")
            os.system('cls' if os.name == 'nt' else 'clear')
            if choice == "q":
                exit_program()
            elif choice == "m":
                main()
            elif choice == "0":
                login(2)
            elif choice == "1":
                gallery_search(user)
            elif choice == "2":
                account_settings(user)
            
            else:
                i+=1
        elif isinstance(user, Admin):
            admin_cmd()
            choice = input("> ")
            os.system('cls' if os.name == 'nt' else 'clear')
            if choice == "q":
                exit_program()
            elif choice == "m":
                main()
            elif choice == "0":
                login("admin")
            elif choice == "1":
                pass
            elif choice == "2":
                pass
            elif choice == "3":
                pass 
            
            
            
def customer_cmd():
    print("Please select an option:")
    print("1. View galleries")
    print("2. account settings")


def admin_cmd():
    print("Please select an option:")
    print("1. Admin controls/account")
    print("2. Art library")
    print("3. Customer list")
    
def account_settings( user):
    i = 0 
    while True:
        
        print("-- q) exit ||m) log out || 0) back --")
        if i>0:
            print("!!Invalid choice!!")
        print("Settings")
        print("1. change username") 
        print("2. change password")
        print("3. delete account")
        choice = input("> ")
        if choice == "q":
            exit_program()
        elif choice == "m":
            main()
        elif choice == "0":
            dashboard(user)
        elif choice == "1":
            change_username(user)
        elif choice == "2":
            change_password(user)
        elif choice == "3":
            remove_user(user)
        else:
            i+=1
            
def main_menu():
    print("-- q) exit --")
    print("Please select an option:")
    print("1. Register new customer")
    print("2. Login")
  
def gallery_search(user):
   
        if isinstance(user, Customer):
            customer_galleries()
            choice = input("> ")
            os.system('cls' if os.name == 'nt' else 'clear')
            if choice == "q":
                exit_program()
            elif choice == "m":
                main()
            elif choice == "0":
                dashboard(user)
            elif choice == "1":
                search_by_owner(user)
            elif choice == "2":
               all_unsold()
            elif choice == "3":
                search_by()
            else:
                i+=1
                
        elif isinstance(user, Admin):
            admin_galleries()
            choice = input("> ")
            os.system('cls' if os.name == 'nt' else 'clear')
            if choice == "q":
                exit_program()
            elif choice == "m":
                main()
            elif choice == "0":
                dashboard(user)
            elif choice == "1":
                user.aquisitions()
            elif choice == "2":
                pass
            elif choice == "3":
                pass 

def customer_galleries():
    print("Please select an option:")
    print("1. View personal gallery")
    print("2. view complete library")
    print("3. search library by")
def admin_galleries():
    pass





#welcome print interface code
os.system('cls' if os.name == 'nt' else 'clear')
print("Welcome to our gallery!", )
input("press any key to continue..")
os.system('cls' if os.name == 'nt' else 'clear')
main()