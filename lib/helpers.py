#helpers are functions that connect the user interface to the class functions, class methods; essentially these are fn that connect the db to the interface.
#
#for example exiting the program or going back to the previous menu 

from models.customers import Customer
from models.admins import Admin
from models.art import Art
import os

def exit_program():
    print("Goodbye!")
    exit()
    



#ADMIN ONLY INTERFACE FNS
def admin_login(username, password):
     #check to see if username is in db
    user = Admin.find_by_username(username)
    if user is None:
            return False
    else:
        if password == user.password:
            # if it does return cust.id
            return user
        else:
            #else in any other case return False
            return False



def aquire_art():
    pass


def all_customers():
    pass

def all_admins():
    pass

def add_admin():
    pass

#SEARCH ART +ART LIST FNS USED FOR ADMIN AND/OR CUST INTERFACE --requires differentiation b12 admin or cust
def change_username(user):
    i =0
    while True:
        if i>0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("invalid username entry, try again or press 0 to cancel")
        print("Remember! Username must be a string between 5-15 characters and no spaces")
        new_name = input(" new username: ")
        if new_name == "0":
            break
        user.username = new_name
        if user.username == new_name:
            print("update successful press any key to return to go back to settings")
            input("> ")
            return True
        else: 
            i+=1
    
        
def change_password(user):
    i =0
    while True:
        if i>0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("invalid password entry, try again or press 0 to cancel")
        print("Remember! Password must be a string over 8 characters and no spaces, include a capital letter, and a number")
        new_name = input(" new password: ")
        if new_name == "0":
            break
        user.password = new_name
        if user.username == new_name:
            print("update successful press any key to return to go back to settings")
            input("> ")
            return True
        else: 
            i+=1
            
def remove_user(user):
    print("Warning!! this cannot be undone and we will remove all of your art from our database!")
    print("enter password to PERMANANTLY remove your account")
    password = input("password: ")
    if password == user.password:
        if isinstance(user, Customer):
           user_art = Art.search_by('owner', user.id)
           if len(user_art)>0:
            for art in user_art:
               art.delete()
        if isinstance(user, Admin):
            admin_art = Art.search_by('admin_acquisition',user.id)
            if len(admin_art)>0:
                for art in admin_art:
                    art.admin_acquisition = 2
                    art.update()
        user.delete()
        exit_program()
    else:
        from cli import main
        main()

def all_art():
    pass

def all_sold():
    pass

def all_unsold():
    pass #use search_by fn setting the owner to 1

def all_artists():
    pass

def search_by():
    print('1) Title\n2) Artist\n3) Price Range\n4) Date Range\n5) Specific Date')
search = input('> ')

if search == "1":
    # Handle title search
    title_query = input("Enter title: ")
    results = Art.search_by('title', title_query)
    # Process results...

elif search == "2":
    # Handle artist search
    artist_query = input("Enter artist: ")
    results = Art.search_by('artist', artist_query)
    # Process results...

elif search == "3":
    # Handle price range search
    min_price = float(input("Enter minimum price: "))
    max_price = float(input("Enter maximum price: "))
    results = Art.search_range('price', min_price, max_price)
    # Process results...

elif search == "4":
    # Handle date range search
    start_date = int(input("Enter start year (YYYY): "))
    end_date = int(input("Enter end year (YYYY): "))
    results = Art.search_range('year_created', start_date, end_date)
    # Process results...

elif search == "5":
    # Handle specific date search
    specific_date = int(input("Enter specific year(YYYY): "))
    results = Art.search_by('year_created', specific_date)
    # Process results...

else:
    print("Invalid choice. Please choose a valid option.")

       



def search_by_owner_id(owner):
    art_list=Art.search_by('owner',owner.id)
    
    display_art_list(art_list, owner)
    
def search_by_id(type_class,id):
    type_class.find_by_id(id)

#CUSTOMER ONLY INTERFACE FNS
 
def register_cust(username, password):
    cust = Customer.create(username, password)
    return cust       

def cust_login(username, password):
    #check to see if username is in db
    user = Customer.find_by_username(username)
    if user is None:
        print("Username doesn't exist would you like to make a new account or try again?")
        choice = input("y/n: ")
        if choice == "y":
            from cli import login
            login(1)
            
        else:
            return False
    else:
        if password == user.password:
            # if it does return cust.id
            return user
        else:
            #else in any other case return False
            return False
        


def cust_gallery(user):
    pass

    

#ART CARD (ON AN INDIVIDUAL ART CARD OPTION MENU)
def display_art_list(list, user):
    n = 0 
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-- q) exit ||m) log out || 0) back --")
        if n>0:
            print("!!Invalid choice!!")
        for art in list:
            print(f'{list.index(art) + 1}) {art}')
        # l = len(list)
        # lm = round(l/3)
        # lm2 = lm*2
        # list1 = list[:lm]
        # list2 = list[lm:lm2]
        # list3 = list[lm2:]
        # i=0
        # for i in range(max(len(list1), len(list2), len(list3))):
        #     col1 = f"{i+1}) {list1[i]}" if i < len(list1) else ""
        #     col2 = f"{i+lm+1}) {list2[i]}" if i < len(list2) else ""
        #     col3 = f"{i+lm2+1}) {list3[i]}" if i < len(list3) else ""
            
        #     print(f'{col1:<5}{col2:<5}{col3:<5}')
        #     i+=1
        choice = input("> ")
        if choice == "q":
            exit_program()
        elif choice == "m":
            from cli import main
            main()
        elif choice == "0":
            from cli import gallery_search
            gallery_search(user)
        if int(choice) in range(1, len(list)+1):
            display_art_card(list[int(choice)-1])
        else:
            n+=1
def display_art_card(artpiece):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(artpiece)

#ADMIN ONLY OPTIONS
def edit_price():
    pass

def remove_art():
    pass


#CUSTOMER ONLY OPTIONS
def purchase_art(customer, artpiece):
    artpiece.owner = customer.id
    artpiece.update()

def sell_art(artpiece):
    artpiece.price = round(artpiece.price*1.2, 2)
    donate_art(artpiece)
    
def donate_art(artpiece):
    artpiece.owner = 1 #customer id of gallery 
    artpiece.update()
