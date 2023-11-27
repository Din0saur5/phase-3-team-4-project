#this is where we will put the art class
#models should focus on database crud actions 
from models.__init__ import CURSOR, CONN
from models.customers import gallery

class Art:
     
    all = {}
    
    def __init__(self, title, artist, price, year_created, admin_acquisition, preview, id=None):
        
        self.id = id
        self.title = title
        self.artist = artist
        self.price = price
        self.year_created = year_created
        self.admin_acquisition = admin_acquisition
        self.preview = preview
        self.owner = gallery
        
        
    
    def __repr__(self):
        return f"<{self.title}\t{self.artist}\t${self.price}>"
  
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) and not hasattr(self, "title"):
            raise Exception("Title must be a non-empty string")
        elif not value:
            raise Exception("Title cannot be an empty string")
        else:
            self._title = value.capitalize()

    @property
    def artist(self):
        return self._artist

    @artist.setter
    def artist(self, value):
        if not isinstance(value, str) and not hasattr(self, "artist"):
            raise Exception("Artist must be a non-empty string")
        elif not value:
            raise Exception("Artist cannot be an empty string")
        else:
            self._artist = value.capitalize()
      
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (float, int)):
            raise Exception("Price must be a float or integer")
        elif not (0 <= value % 1 < 0.01):  # Check for two decimal places
            raise Exception("Price must have exactly two decimal places")
        else:
            self._price = float(f"{value:.2f}")       
    
    @property
    def year_created(self):
        return self._year_created

    @year_created.setter
    def year_created(self, value):
        if not isinstance(value, int) and not hasattr(self, "year_created"):
            raise Exception("Year created must be an integer")
        else:
            self._year_created = value
    
    @property
    def admin_acquisition(self):
        return self._admin_acquisition

    @admin_acquisition.setter
    def admin_acquisition(self, value):
        from models.admins import Admin
        if not isinstance(value, Admin) and not hasattr(self, "admin_acquisition"):
            raise Exception("Admin acquisition must be an instance of the Admin class")
        else:
            self._admin_acquisition = value  
    
    @property
    def owner(self):
        return self._owner
    @owner.setter
    def owner(self, owner):
        from models.customers import Customer
        if isinstance(owner, (Customer, None)):
            self._owner = owner
        else:
            raise Exception('error setting owner')    
        
    
    
    def delete(self):   
        """Delete the table row corresponding to the current art instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM art
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None
    
    def update(self):
        """Update the table row corresponding to the current art instance."""
       
        sql = """
            UPDATE art
            SET   price = ?, owner = ?,  
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.price, self.owner[id], self.id))
        CONN.commit()
    
   
    
    def save(self):
        """ Insert a new row with the username and password values of the current Admin instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO art (title, artist, price, year_created, admin_acquisition, preview, owner)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.title, self.artist, self.price, self.year_created, self.admin_acquisition[id], self.preview, self.owner[id]))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    @classmethod
    def create(cls, title, artist, price, year_created, admin_acquisition, preview):
        """ Initialize a new Art instance and save the object to the database """
        art = cls( title, artist, price, year_created, admin_acquisition, preview)
        art.save()
        return art
    
    @classmethod
    def instance_from_db(cls, row):
        """Return a Art object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        art = cls.all.get(row[0])
        if art:
            # ensure attributes match row values in case local instance was modified
            art.title = row[1]
            art.artist = row[2]
            art.price = row[3]
            art.year_created = row[4]
            art.admin_acquisition = row[5]
            art.preview = row[6]
            art.owner = row[7]
            art.sold = row[8]
        else:
            # not in dictionary, create new instance and add to dictionary
            art = cls(row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8])
            art.id = row[0]
            cls.all[art.id] = art
        return art

    @classmethod
    def get_all(cls):
        """Return a list containing a art object per row in the table"""
        sql = """
            SELECT *
            FROM art
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def search_by(cls, column, query):
        # Validate the column name to prevent SQL injection
        allowed_columns = ['title', 'artist', 'year_created', 'admin_aquisition', 'preview', 'owner']
        if column not in allowed_columns:
            raise Exception(f"Invalid column name: {column}")

        sql = f"""
            SELECT *
            FROM art
            WHERE {column} = ?
        """

        rows = CURSOR.execute(sql, (query,))
        return [cls.instance_from_db(row) for row in rows] if rows else None
    
    @classmethod
    def search_range(cls, column, min, max):
        allowed_columns = ['price', 'year_created']
        if column not in allowed_columns:
            raise Exception(f"Invalid column name: {column}")
        sql = f"""
            SELECT *
            FROM art
            WHERE {column} BETWEEN ? AND ?
        """

        rows = CURSOR.execute(sql, (min, max))
        return [cls.instance_from_db(row) for row in rows] if rows else None
    
    @classmethod
    def search_sold(cls):
        sql = """
            SELECT *
            FROM art
            WHERE owner != ?
        """

        rows = CURSOR.execute(sql, (gallery[id],))
        return [cls.instance_from_db(row) for row in rows] if rows else None
    