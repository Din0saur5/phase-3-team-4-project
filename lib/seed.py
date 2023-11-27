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

Art.create("Salvator Mundi", "Leonardo da Vinci", 475400000.00, 1500, 1, "lib/gallery_photos/Salvator_Mundi.jpg")
Art.create("Portrait of Dr. Gachet", "Van Gogh", 163400000.00, 1890, 1, "lib/gallery_photos/Portrait.jpg")
Art.create("The Scream", "Edvard Munch", 135200000.00, 1895, 1, "lib/gallery_photos/The_Scream.jpg")
Art.create("Diana", "Francesca Castro", 2620.00, 2016, 1, "lib/gallery_photos/Diana.jpg")
Art.create("River", "Duc Dzung Hoang", 62400.00, 2018, 1, "lib/gallery_photos/River.jpg")
Art.create("Continuum", "Naja Utzon Popov", 16000.00, 2021, 1, "")
Art.create("Golden Spiral", "Eva Johnova", 2200.00, 2022, 1, "")
Art.create("Blossoming Ocean 2", "Vafa Majidli", 6500.00, 2022, 1,"")
Art.create("Massilia", "Karine Bartoli", 1000.00, 2022, 1,)
Art.create("XOEL", "Lee Jenkinson", 313.62, 2023, 1, "")
Art.create("Figs", "Albert Kechyan", 2163.23, 2023, 1, "")
Art.create("Shadow", "Victoria Cozmolici", 1971.90, 2023, 1, "")
Art.create("Codeword", "Niki Hare", 3900.00, 2014, 1, "")
Art.create("Red spectra", "Nestor Toro", 2600.00, 2018, 1, "")
