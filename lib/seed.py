#this is where we seed the data base (add all starting data)
#example vv
# from models.__init__ import CONN, CURSOR
# from models.department import Department
# from models.employee import Employee

# def seed_database():
#     Employee.drop_table()
#     Department.drop_table()
#     Department.create_table()
#     Employee.create_table()

#     # Create seed data
#     payroll = Department.create("Payroll", "Building A, 5th Floor")
#     human_resources = Department.create(
#         "Human Resources", "Building C, East Wing")
#     Employee.create("Amir", "Accountant", payroll.id)
#     Employee.create("Bola", "Manager", payroll.id)
#     Employee.create("Charlie", "Manager", human_resources.id)
#     Employee.create("Dani", "Benefits Coordinator", human_resources.id)
#     Employee.create("Hao", "New Hires Coordinator", human_resources.id)


# seed_database()
# print("Seeded database")


# Art.create(title, artist, price, year_created, admin_acquisition, preview)
# title should be a not empty string 
# artist should be a not empty string 
# price should be a int or float with .00 at end
# year created should be an int
# admin aquisition should 1
# preview to string "./path to photo" 

