main_cities = ["Tokyo", "Kyoto", "Osaka", "Hakone", "Nara", "Hiroshima", "Kanazawa"]

class Destination:
    def __init__(self, select_location):
        self.select_location = select_location
        self.cities = main_cities
    def show_location(self):
        print(self.select_location)
tokyo = Destination("Tokyo")
kyoto = Destination("kyoto")

tokyo.show_location()
kyoto.show_location()
        
class Category:
    def __init__(self, choice):
        self.choice = choice
    def show_category(self):
        print(self.choice)    


shrines = Category("shrines")
restaurants = Category("restaurants")

shrines.show_category()
restaurants.show_category()