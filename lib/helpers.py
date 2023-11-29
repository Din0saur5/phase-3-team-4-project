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



def aquire_art(user):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-- 0) back --")
    print("if you screw up inputs it will kick you from the program")
    print("title must be non empty str")
    print("artist must be non empty str")
    print("year must be int (yyyy)")
    print("price must be int or float .00")
    print("for preview: right click img file in gallery_photos select copy relative path and paste into preview input")

    title= input("title: ")
    if title == "0" or title == "": return

    artist = input("artist: ")
    if artist == "0" or artist == "": return

    yearS = input("year (yyyy): ")
    if yearS == "0" or not isinstance(yearS, int): return

    priceS = input("price (0.00): $")
    if priceS == "0" or not isinstance(priceS, int) or not isinstance(yearS, float): return

    year_created = int(yearS)
    price = int(priceS)
    preview = input("preview: ")

    art = user.create_art(title, artist, price, year_created, preview)
    print("succesfully created:")
    print(art)


def all_customers(user):
    custs = Customer.get_all()
    for cust in custs:
        print(f'{custs.index(cust) + 1}) {cust}')

    c1 = input("> ")
    choice = int(c1)-1

    if choice in range(len(custs)):
        pass
        list = search_by_owner(custs.pop(choice))
        display_art_list(list, user)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        from cli import dashboard
        print('invalid input')
        dashboard(user)


def all_admins(user):
    os.system('cls' if os.name == 'nt' else 'clear')
    admins = Admin.get_all()
    for admin in admins:
        print(f'{admins.index(admin) + 1}) {admin}')

    choice = input("     Press any key to go back         ")
    if choice:
        from cli import admin_menu
        admin_menu(user)

def add_admin(username, password):
    new_admin = Admin.create(username, password)
    return new_admin

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
           if user_art != None:
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

def all_art(user):
    arts = Art.get_all()
    display_art_list(arts,user)

def all_sold(user):
    all_sold =  Art.search_sold()
    display_art_list(all_sold,user)

def all_unsold(user):
    all_unsold = Art.search_by("owner", 1)
    display_art_list(all_unsold,user)

def all_artists(user):
    if isinstance(user, Customer):
        all_art =  Art.search_by("owner", 1)
    else:
        all_art = Art.get_all()

    all_artists = list({art.artist for art in all_art})
    for artist in all_artists:
        print(f"{all_artists.index(artist) +1}) {artist}")

    c1 = input("> ")
    choice = int(c1)-1

    if choice in range(len(all_artists)):
        art_list = Art.search_by('artist', all_artists.pop(choice))
        display_art_list(art_list, user)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')

def search_as_admin(user):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Select a Category')
    print('1) Title\n2) Artist\n3) Price Range\n4) Date Range\n5) Specific Date')
    search = input('> ')

    if search == "q": # trusy dusty close button
        exit_program()
    if search == "0": # trusy dusty back button
        from cli import admin_gallery_search
        admin_gallery_search(user)

    elif search == "1":
        # Handle title search
        title_query = input("Enter title: ")
        results = Art.search_by('title', title_query)

    elif search == "2":
        # Handle artist search
        artist_query = input("Enter artist: ")
        results = Art.search_by('artist', artist_query)

    elif search == "3":
        # Handle price range search
        min_price = float(input("Enter minimum price: "))
        max_price = float(input("Enter maximum price: "))
        results = Art.search_range('price', min_price, max_price)

    elif search == "4":
        # Handle date range search
        start_date = int(input("Enter start year (YYYY): "))
        end_date = int(input("Enter end year (YYYY): "))
        results = Art.search_range('year_created', start_date, end_date)

    elif search == "5":
        # Handle specific date search
        specific_date = int(input("Enter specific year(YYYY): "))
        results = Art.search_by('year_created', specific_date)

    else:
        results = "Invalid choice. Please choose a valid option."

    os.system('cls' if os.name == 'nt' else 'clear')
    print(results)
    input(">")

def search_as_cust():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Select a Category')
    print('1) Title\n2) Artist\n3) Price Range\n4) Date Range\n5) Specific Date')
    search = input('> ')

    if search == "1":
        # Handle title search
        title_query = input("Enter title: ")
        results = Art.cust_search_by('title', title_query)

    elif search == "2":
        # Handle artist search
        artist_query = input("Enter artist: ")
        results = Art.cust_search_by('artist', artist_query)


    elif search == "3":
        # Handle price range search
        min_price = float(input("Enter minimum price: "))
        max_price = float(input("Enter maximum price: "))
        res = Art.search_range('price', min_price, max_price)
        results = [art for art in res if art.owner == 1]


    elif search == "4":
        # Handle date range search
        start_date = int(input("Enter start year (YYYY): "))
        end_date = int(input("Enter end year (YYYY): "))
        res = Art.search_range('year_created', start_date, end_date)
        results = [art for art in res if art.owner == 1]


    elif search == "5":
        # Handle specific date search
        specific_date = int(input("Enter specific year(YYYY): "))
        results = Art.cust_search_by('year_created', specific_date)


    else:
        results = "Invalid choice. Please choose a valid option."

    os.system('cls' if os.name == 'nt' else 'clear')
    print(results)
    input(">")



def search_by_owner(owner):
    art_list=Art.search_by('owner',owner.id)
    return art_list


def search_by_id(type_class,id):
    type_class.find_by_id(id)

#CUSTOMER ONLY INTERFACE FNS

def register_cust(username, password):
    Customer.create(username, password)
    cust = cust_login(username,password)
    return cust

def cust_login(username, password):
    #check to see if username is in db
    user = Customer.find_by_username(username)
    if user is None:
        print("Username doesn't exist would you like to make a new account?")
        choice = input("y/n: ")
        if choice == "y":
            from cli import login
            login("1")

        else:
            return False
    else:
        if password == user.password:

            return user
        else:
            #else in any other case return False
            return False

#ART CARD (ON AN INDIVIDUAL ART CARD OPTION MENU)
def display_art_list(list, user):
    from cli import cust_gallery_search, admin_gallery_search
    n = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-- q) exit ||m) log out || 0) back --")
        if n>0:
            print("!!Invalid choice!!")
        print("select from list for more info")
        if list != None:
            for art in list:
                print(f'{list.index(art) + 1}) {art}')
            choice = input("> ")
            if choice == "q":
                exit_program()
            elif choice == "m":
                from cli import main
                main()
            elif choice == "0":
                if isinstance(user, Customer):
                    cust_gallery_search(user)
                else:
                    admin_gallery_search(user)
            if int(choice) in range(1, len(list)+1):
                display_art_card(list[int(choice)-1], user, list)
            else:
                n+=1
        else:
            print("None press any key to go back to gallery search")
            input('> ')
            os.system('cls' if os.name == 'nt' else 'clear')
            if isinstance(user, Customer):
                cust_gallery_search(user)
            else:
                admin_gallery_search(user)

def display_art_card(artpiece, user, list):
    from preview_win import show_preview
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{artpiece.title}")
    print(f"   by {artpiece.artist} -- {artpiece.year_created} ")
    print(f"${artpiece.price:,.2f}")
    show_preview(artpiece)
    if isinstance(user, Customer) and artpiece.owner != user.id:
        choice = input("purchase (y/n): ")
        if choice == "y":
            purchase_art(user, artpiece)
            display_art_list(list, user)
    elif isinstance(user, Customer) and artpiece.owner == user.id:
        choice = input("donate/return art to Gallery (y/n): ")
        if choice == "y":
            donate_art(artpiece)
            display_art_list(list, user)
    else:
        print("--- 1) edit price || 2) remove art --- ")
        choice = input("> ")
        if choice == "1":
            price = input("new price: ")
            edit_price(artpiece, float(price))
            display_art_list(list, user)
        elif choice == "2":
            rus = input("are you sure, cannot be undone? (y/n):  ")
            if rus == "y":
                remove_art(artpiece)
            display_art_list(list, user)
        else:
            display_art_list(list, user)

#ADMIN ONLY OPTIONS
def edit_price(artpiece, price):
    artpiece.price = price
    artpiece.update()

def remove_art(artpiece):
    artpiece.delete()



#CUSTOMER ONLY OPTIONS
def purchase_art(customer, artpiece):
    artpiece.owner = customer.id
    artpiece.update()

def donate_art(artpiece):
    artpiece.owner = 1 #customer id of gallery
    artpiece.update()
