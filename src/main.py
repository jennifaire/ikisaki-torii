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

welcome_msg = print("welcome to ikisaki torii!!\n")

# to be turned into functions:
# 1. sort by category or destination & view corresponding data
# 2. choose where to go or randomize

def select_destination():
    where = input("choose your destination or say 'surprise me'.\n").lower()
    random_city = random.choice(cities)
    if where == "surprise me":
        print(f"let's explore {random_city}")
    elif where in cities:
        print(f"welcome to {where}")
    else:
        print("sorry, that city is not currently supported. try again!!")

def select_category():
    choice = (input("which category would you like to view?\ntype destinations, food, or shrines\n")).lower()
    if choice == "destinations":
        print(cities)
    elif choice == "food":
        print(food)
    elif choice == "shrines":
        print(shrines)
    else:
        print("sorry, that category is not supported at this time. try again!!")    

select_destination()
select_category()
