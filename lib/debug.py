

import ipdb
from models.__init__ import CONN, CURSOR
from models.art import Art
# from models.customers import Customer
# from models.admins import Admin
# from helpers import *
from lib.preview_win import *
list = Art.get_all
pic = list[0]
preview = pic.preivew
show_preview(preview)
print("works")
# ipdb.set_trace
