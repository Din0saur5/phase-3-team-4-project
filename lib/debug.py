

import ipdb
from models.__init__ import CONN, CURSOR
from models.art import Art
from models.customers import Customer
from models.admins import Admin


all_customers=Admin.get_all()
print(all_customers)

ipdb.set_trace
