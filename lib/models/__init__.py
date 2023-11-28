#this is where we initalize the database 
import sqlite3

CONN = sqlite3.connect('art_gallery.db')
CURSOR = CONN.cursor()