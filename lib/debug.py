

import ipdb
from models.__init__ import CONN, CURSOR
# from models.art import Art
# from models.customers import Customer
# from models.admins import Admin
# from helpers import *
from cli import *
usern = 'Gallery'
pas= "Gallery1"
user = cust_login(usern, pas)

gallery_search(user)
# ipdb.set_trace
