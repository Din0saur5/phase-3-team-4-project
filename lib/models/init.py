#this is where we initalize the database 
import sqlite3

CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()