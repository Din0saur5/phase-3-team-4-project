#this is where we will put the customer class
#models should focus on database crud actions
from models.__init__ import CURSOR, CONN
from models.art import Art
class Customer:
    all = {}

    def __init__(self, username, password, id=None):
        self.id = id
        self.username = username
        self.password = password


    def __repr__(self):
        return f"<Customer: {self.username} || id: {self.id}>"
#validate username property before setting
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and len(username) in range(5,16) and ' ' not in username:
            self._username = username
        else:
            self._username = None


    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        if isinstance(password, str) and len(password) >= 8 and ' ' not in password and password != password.lower() and any(char.isdigit() for char in password):
            self._password = password
        else:
            self._username = None

    def delete(self):
        """Delete the table row corresponding to the current customer instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM customers
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    def update(self):
        """Update the table row corresponding to the current customer instance."""
        sql = """
            UPDATE customers
            SET username = ?, password = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.username, self.password, self.id))
        CONN.commit()


    def save(self):
        """ Insert a new row with the username and password values of the current Customer instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO customers (username, password)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.username, self.password))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self


    def aquisitions(self):
        list = Art.search_by("owner", self.id)
        return list

    @classmethod
    def create(cls, username, password):
        """ Initialize a new Customer instance and save the object to the database """
        customer = cls(username, password)
        customer.save()
        if customer._username or customer._password is None:
            customer.delete()
            return False
        else:
            return customer

    @classmethod
    def instance_from_db(cls, row):
        """Return a Customer object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        customer = cls.all.get(row[0])
        if customer:
            # ensure attributes match row values in case local instance was modified
            customer.username = row[1]
            customer.password = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            customer = cls(row[1], row[2])
            customer.id = row[0]
            cls.all[customer.id] = customer
        return customer

    @classmethod
    def get_all(cls):
        """Return a list containing a customer object per row in the table"""
        sql = """
            SELECT *
            FROM customers
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return Customer object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM customers
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_username(cls, username):
        """Return Customer object corresponding to the table row matching the username"""
        sql = """
            SELECT *
            FROM customers
            WHERE username = ?
        """

        row = CURSOR.execute(sql, (username,)).fetchone()
        return cls.instance_from_db(row) if row else None
