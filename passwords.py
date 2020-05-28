import json

password={
    "user":"KALYAN",
    "password":"Kalyan@1010",
    "account":"kga99513.us-east-1"
    }

with open("data_file.json", "w") as write_file:
    json.dump(password, write_file)
