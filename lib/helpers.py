#helpers are functions that connect the user interface to the class functions, class methods; essentially these are fn that connect the db to the interface.
#
#for example exiting the program or going back to the previous menu 

from models.customers import gallery, Customer
from models.admins import Admin
from models.art import Art


def exit_program():
    print("Goodbye!")
    exit()
    



#ADMIN ONLY INTERFACE FNS
def admin_login():
    pass #checks params and raises exceptions as needed and returns either true or false

def admin_change_username():
    print("Remember! username must be between 8 and 25 char")
    input(" new username: ")
    #admin class fn set username add return statment cont
     
def admin_change_pass():
    pass

def aquire_art():
    pass

def remove_admin():
    pass

def all_customers():
    pass

def all_admins():
    pass

def add_admin():
    pass

#SEARCH ART +ART LIST FNS USED FOR ADMIN AND/OR CUST INTERFACE --requires differentiation b12 admin or cust

def all_art():
    pass

def all_sold():
    pass

def all_unsold():
    pass

def all_artists():
    pass

def search_by_price_range():
    pass

def search_by_date():
    pass

def search_by_date_range():
    pass

def search_by_admin():
    pass

def search_by_preview():
    pass

def search_by_owner():
    pass


#CUSTOMER ONLY INTERFACE FNS
 
def register_cust(username, password):
    return True        #checks params and raises exceptions as needed and returns either true or false

def cust_login():
    pass #checks params and raises exceptions as needed and returns either true or false

def cust_change_username():
    pass

def cust_change_pass():
    pass


def remove_cust():
    pass


def cust_gallery():
    pass


#ART CARD (ON AN INDIVIDUAL ART CARD OPTION MENU)
def display_art_card():
    pass

#ADMIN ONLY OPTIONS
def edit_price():
    pass

def remove_art():
    pass


#CUSTOMER ONLY OPTIONS
def purchase_art():
    pass

def sell_art(artpiece):
    artpiece.price = round(artpiece.price*1.2, 2)
    donate_art(artpiece)
    
def donate_art(artpiece):
    artpiece.owner = gallery
    artpiece.update()
