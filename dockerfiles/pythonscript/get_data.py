import requests
from time import sleep
from elasticsearch import Elasticsearch

extra_life_url = "https://www.extra-life.org/api/participants/477670/donations"
donations = requests.get(extra_life_url)

sleep(60)

es = Elasticsearch("http://elasticsearch:9200")
response = es.indices.create(index="donations")
print(response)
for donation in donations.json():
    responses = es.index(
        index = "donations",
        body = donation)
    print(responses)