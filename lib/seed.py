#this is where we seed the data base (add all starting data)


from models.__init__ import CONN, CURSOR
from models.art import Art
from models.customers import Customer
from models.admins import Admin
def seed_database():



 # Create seed data
    #admin seed data
    # Admin.create("MastaP", "1234Five") 
    # Admin.create("4Rudy", "4Rudy2booty")
    # Admin.create("FatherCode", "supremeWizard6") 
    # #customer seed data
    # Customer.create("Gallery", "Gallery1")

# Art.create(title, artist, price, year_created, admin_acquisition, preview)
# title should be a not empty string 
# artist should be a not empty string 
# price should be a int or float with .00 at end
# year created should be an int
# admin aquisition should 1
# preview to string "./path to photo" 

    # Art.create("Salvator Mundi", "Leonardo da Vinci", 475400000.00, 1500, 1, "lib/gallery_photos/Salvator_Mundi.jpg")
    # Art.create("Portrait of Dr. Gachet", "Van Gogh", 163400000.00, 1890, 1, "lib/gallery_photos/Portrait.jpg")
    # Art.create("The Scream", "Edvard Munch", 135200000.00, 1895, 1, "lib/gallery_photos/The_Scream.jpg")
    # Art.create("Diana", "Francesca Castro", 2620.00, 2016, 1, "lib/gallery_photos/Diana.jpg")
    # Art.create("River", "Duc Dzung Hoang", 62400.00, 2018, 1, "lib/gallery_photos/River.jpg")
    # Art.create("Continuum", "Naja Utzon Popov", 16000.00, 2021, 1, "lib/gallery_photos/Continuum.jpg")
    # Art.create("Golden Spiral", "Eva Johnova", 2200.00, 2022, 1, "lib/gallery_photos/Golden_Spiral.jpg")
    # Art.create("Blossoming Ocean 2", "Vafa Majidli", 6500.00, 2022, 1,"lib/gallery_photos/Blossoming_Ocean_2.jpg")
    # Art.create("Massilia", "Karine Bartoli", 1000.00, 2022, 1, "lib/gallery_photos/Massilia.jpg")
    # Art.create("XOEL", "Lee Jenkinson", 313.62, 2023, 1, "lib/gallery_photos/XOEL.jpg")
    # Art.create("Figs", "Albert Kechyan", 2163.23, 2023, 1, "lib/gallery_photos/Figs.jpg")
    # Art.create("Shadow", "Victoria Cozmolici", 1971.90, 2023, 1, "lib/gallery_photos/Shadow.jpg")
    # Art.create("Codeword", "Niki Hare", 3900.00, 2014, 1, "lib/gallery_photos/Codeword.jpg")
    # Art.create("Red spectra", "Nestor Toro", 2600.00, 2018, 1, "lib/gallery_photos/Red_spectra.jpg")
    # Art.create("Pleasure", "Maria Moretti", 7140.00, 2023, 1, "lib/gallery_photos/Pleasure.jpg")
    # Art.create("Hot Blood", "Tatiana Yabloed", 4471.00, 2023, 1, "lib/gallery_photos/Hot_Blood.jpg")
    # Art.create("Hangover Daddy", "Kristin Kossi", 4720.00, 2019, 1, "lib/gallery_photos/Hangover_Daddy.jpg")
    # Art.create("The Big Dipper", "Khodakivskyi Vasyl", 4470.00, 2019, 1, "lib/gallery_photos/The_Big_Dipper.jpg")
    # Art.create("Sound Of Life", "Nick Molloy", 854.49, 2023, 1, "lib/gallery_photos/Sound_of_Life.jpg")
    # Art.create("Autumn flowers", "Lilia Orlova-Holmes", 2759.89, 2023, 1, "lib/gallery_photos/End_Of_Cont_Art.jpg")
    # Art.create("The End of the Contemporary Art", "Dima Braga", 65000.00, 2016, 1, "lib/gallery_photos/End_Of_Cont_Art.jpg")
    # Art.create("Paris contrasts", "Dennis Kuvayev", 60252.50, 2018, 1, "lib/gallery_photos/Paris_Contrasts.jpg")
    # Art.create("The one raw brown in different earth tones", "Tiny de Bruin", 55897.89, 2021, 1, "lib/gallery_photos/The_One_Raw_Brown.jpg")
    # Art.create("Caoutchouc II", "Abhishek Kumar", 40000.00, 2018, 1, "lib/gallery_photos/Caotchouc_2.jpg")
    # Art.create("Circe", "Eric Armusik", 32000.00, 2015, 1, "lib/gallery_photos/Circe.jpg")
    # Art.create("Skull", "Daniel Hackworth", 475400000.01, 2020, 1, "lib/gallery_photos/Skull.jpg")
    # Art.create("Kaleidoscope Tears", "Sheila James", 475400001.01, 2020, 1, "lib/gallery_photos/Kaleidoscope.jpg")
    pass







seed_database()
print("Seeded database")