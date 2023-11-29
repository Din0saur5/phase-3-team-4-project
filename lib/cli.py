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
        if isinstance(verify, Customer) or isinstance(verify, Admin):
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
                login("2")
            elif choice == "1":
                cust_gallery_search(user)
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
                admin_menu(user)
            elif choice == "2":
                admin_gallery_search(user)
            elif choice == "3":
                all_customers(user)



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
        os.system('cls' if os.name == 'nt' else 'clear')
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
            if isinstance(user, Admin):
                admin_menu(user)
            else:
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

def cust_gallery_search(user):
    i = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-- q) exit ||m) log out || 0) back --")
        if i>0:
            print("!!Invalid choice!!")
        if isinstance(user, Customer):
            customer_galleries()
            choice = input("> ")
            if choice == "q":
                exit_program()
            elif choice == "m":
                main()
            elif choice == "0":
                dashboard(user)
            elif choice == "1":
                search_by_owner(user)
            elif choice == "2":
                all_unsold(user)
            elif choice == "3":
                search_as_cust()
            elif choice == "4":
                all_artists(user)
            else:
                i+=1

def admin_gallery_search(user):
    i = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-- q) exit ||m) log out || 0) back --")
        if i>0:
            print("!!Invalid choice!!")
        if isinstance(user, Admin):
            admin_galleries()
            choice = input("> ")
            if choice == "q":
                exit_program()
            elif choice == "m":
                main()
            elif choice == "0":
                dashboard(user)
            elif choice == "1":
                list= user.aquisitions()
                display_art_list(list, user)
            elif choice == "2":
                all_art(user)
                
            elif choice == "3":
                search_as_admin()
                
            elif choice == "4":
                all_artists(user)
                
            elif choice == "5":
                aquire_art(user)

def customer_galleries(user):
    
    print("Please select an option:")
    print("1. View personal gallery")
    print("2. view complete library")
    print("3. search library by")
    print("4. list of all artists names")

def admin_galleries():

    print("Please select an option:")
    print("1. View personal aqusitions")
    print("2. view complete library")
    print("3. search library by")
    print("4. list of all artists names")
    print("5. Add to Gallery")


def admin_menu(user):

    i = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-- q) exit ||m) log out || 0) back --")
        if i>0:
            print("!!Invalid choice!!")

        print("Admin Menu")
        print("1. Account Settings")
        print("2. Add New Admin")
        print("3. View All Admins")
        choice = input("> ")
        if choice == "q":
            exit_program()
        elif choice == "m":
            main()
        elif choice == "0":
            dashboard(user)
        elif choice == "1":
            account_settings(user)
        elif choice == "2":
            register_admin(user)
        elif choice == "3":
            all_admins(user)
        else:
            i+=1

def register_admin(admin):
    i=0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') # clears the terminal
        print("-- q) exit ||0) back --")
        if i>0:
            print("!!Invalid choice!!")
        print("    Username must be between 8 and 25 characters")

        user = input("Admin's Username: ")
        if user == "q":
            exit_program()
        elif user == "0":
            admin_menu(admin)
            break
        elif user != '':
            print("    Password must be over 8 character, and include a capital letter, and a number")
            password = input("Admin's Password: ")
            if password == "q":
                exit_program()
            elif password == "0":
                admin_menu(admin)
            elif password:
                verify = add_admin(user, password)
            if isinstance(verify, Admin):
                print("Admin added")
                dashboard(admin)
            else:
                i+=1
                continue
        else:
            i+=1

if __name__ == '__main__':
    #welcome print interface code
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to our gallery!", )
    input("Press any key to continue...")
    main()
