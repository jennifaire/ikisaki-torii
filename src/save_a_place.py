saved_places = []

while True:
    place = input("what place would you like to save?")
    city = input("which city is this place located in? ")
    note = input("would you like to save a note alongside your place?")

    saved_place = {
        "user_id": 1,
        "place_id": len(saved_places) +1,
        "city": city,
        "place_name": place,
        "note": note,
    }

    saved_places.append(saved_place)
    print(saved_place)

    another = input("would you like to save another place??")

    if another.lower() != "yes":
        print(saved_places)
        break