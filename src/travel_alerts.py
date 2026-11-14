import requests
import smtplib
from email.message import EmailMessage
import os
import dotenv

dotenv.load_dotenv()

my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("MY_PASSWORD")



# STEP 2: RETRIEVE DISRUPTION DATA

# TODO 1: Make a GET request to the endpoint.

url = "https://api.gachi-tokusuru.com/example/train-status"

response = requests.get(url)
response.raise_for_status()

train_data = response.json()

# TODO 2: Convert the response to JSON.

# json_data = json.dumps(train_data, indent=4)
# print(json_data)

# STEP 3: FILTER RELEVANT INFORMATION

# TODO 3: Identify the destination or train line

yamanote = train_data["lines"][0]["line_en"]

# TODO 4: Filter the API data for disruptions.
current_delays = []

for line_info in train_data["lines"]:
    status = line_info["status"]
    route = line_info["line_en"]
    reason = line_info["cause"]
    last_updated = line_info["source_published_at"]
    if status != "normal":
        current_delays.append((route, status, reason, last_updated))

delay_msg = ""

for route, status, reason, last_updated in current_delays:
    delay_msg += (
        f"route: {route}\n"
        f"status: {status}\n"
        f"reason: {reason}\n"
        f"last updated: {last_updated}\n"
    )
# STEP 4: GENERATE AN ALERT

# TODO 9: Format and display a readable alert.

if current_delays:
    msg = EmailMessage()
    msg["subject"] = "current train delays"
    msg["from"] = my_email
    msg["to"] = "ikisakitorii@gmail.com"

    msg.set_content(f"this is an alert from ikisaki torii.\n\n"
                    f"the following tokyo train routes are experiencing delays:\n"
                    f"{delay_msg}", charset="utf-8")

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.send_message(msg)
else:
    print("all train lines are running normally.")