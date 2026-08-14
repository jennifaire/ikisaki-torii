print("welcome to ikisaki torii")

cities = ["tokyo", "kyoto", "osaka", "hakone", "nara", "hiroshima", "kanazawa"]
food = ["katsu", "sushi", "ramen", "curry", "ice cream"]
shrines = ["asakusa", "hanazono", "shibuya", "meiji"]

#list of potential destinations:
#coffee shops
#pastry shops
#general eateries
#shrines
#temples
#hotels
#subway & train stations
#hotels
#onsen & sento - tattoo friendly
#sanrio stores
#public restrooms
#konbinis
#theme parks
#government buildings
#vending machines??
#not technically a place but data that will tell you WHICH FLOOR SOMETHING IS ON
#pokemon centers - is this technically a theme park??
#airports
#exhibitions - ie hello kitty in kyoto
#gardens?? ie murinan
#landmarks ie shibuya crossing, tokyo tower etc.
#day spas - tattoo friendly
#tea houses
#museums
#laundromats
#gyms??


import random

choose_display = (input("welcome!! what would you like to view today?\n")).lower()

if choose_display in "destinations":
    print(cities)
elif choose_display in "food":
    print(food)
elif choose_display in "shrines":
    print(shrines)
else:
    print("sry babe, that's not supported at this time!! try again")

print("your japan destinations:")
for number, city in enumerate(cities, start = 1):
    print(f"{number}. {city}")

where = input("choose your destination or say 'surprise me'\n").lower()
random_city = random.choice(cities)

if where == "surprise me":
    print(f"you're going to {random_city}!!")
elif where in cities:
    print(f"welcome to {where}!!")
else:
    print("sry babe, that's not one of your destinations!! try again")


