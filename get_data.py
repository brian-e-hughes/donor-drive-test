import requests
import json

url = "https://www.extra-life.org/api/participants/477670/donations"
donations = requests.get(url)
print(donations.json())


