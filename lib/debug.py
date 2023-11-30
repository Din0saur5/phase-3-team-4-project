

import ipdb

import os
from models.__init__ import CONN, CURSOR
from models.art import Art
# from models.customers import Customer
# from models.admins import Admin
# from helpers import *
from preview_win import *
os.system('cls' if os.name == 'nt' else 'clear')
list = Art.get_all()
print(list)
for pic in list:

    show_preview(pic)
print("works")

