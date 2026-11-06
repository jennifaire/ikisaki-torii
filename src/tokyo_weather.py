import requests

def get_weather(city):
    request = requests.get(url=f"https://wttr.in/{city}?format=j1")
    request.raise_for_status()
    weather_data = request.json()

    outlook = weather_data["current_condition"][0]["weatherDesc"][0]["value"]
    f_temp = weather_data["current_condition"][0]["temp_F"]
    print(f"current weather in {city}")
    print(f"outlook: {outlook}")
    print(f"current temp in F: {f_temp}")

city = input("which city would you like to view the weather for??\n")

get_weather(city)