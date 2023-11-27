#this is where we will put the admin class
#models should focus on database crud actions 
from models.__init__ import CURSOR, CONN
from models.art import Art

class Admin:
    
    all = {}
    
    def __init__(self, username, password, id=None):
        self.id = id
        self.username = username
        self.password = password
        
    
    def __repr__(self):
        return f"<Admin {self.id}: {self.username}>"
#validate username property before setting    
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and len(username) in range(5,16) and ' ' not in username:
            self._username = username
        else:
            raise Exception(
                "Username must be a string between 5-15 characters and no spaces"
            )
            
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        if isinstance(password, str) and len(password) > 7 and ' ' not in password and password != password.lower() and any(char.isdigit() for char in password):
            self._password = password
        else:
            raise Exception(
                "Password must be a string over 8 characters and no spaces, include a capital letter, and a number"
            )
            
    def delete(self):   
        """Delete the table row corresponding to the current admin instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM admins
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None
    
    def update(self):
        """Update the table row corresponding to the current admin instance."""
        sql = """
            UPDATE admins
            SET username = ?, password = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.username, self.password, self.id))
        CONN.commit()
    
    def aquisitions(self):
        list = Art.search_by("admin_acquisition", self.id)
        return list
    
    def create_art(self, title, artist, price, year_created, preview):
        Art.create(title,artist, price, year_created, self, preview)
    
        
    def save(self):
        """ Insert a new row with the username and password values of the current Admin instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO admins (username, password)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.username, self.password))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    
    @classmethod
    def create(cls, username, password):
        """ Initialize a new Admin instance and save the object to the database """
        admin = cls(username, password)
        admin.save()
        return admin
    
    @classmethod
    def instance_from_db(cls, row):
        """Return a Admin object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        admin = cls.all.get(row[0])
        if admin:
            # ensure attributes match row values in case local instance was modified
            admin.username = row[1]
            admin.password = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            admin = cls(row[1], row[2])
            admin.id = row[0]
            cls.all[admin.id] = admin
        return admin

    @classmethod
    def get_all(cls):
        """Return a list containing a admin object per row in the table"""
        sql = """
            SELECT *
            FROM admins
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]