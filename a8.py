import requests
import json

filename = input("Dose path arxeiou: ")

f = open(filename, "r")
json_data = json.loads(f.read())
total = 0
for crypto in json_data:
	url = "https://min-api.cryptocompare.com/data/price?fsym="+crypto+"&tsyms=EUR"
	v = requests.get(url).json()['EUR']
	value = v * json_data[crypto]
	total += value
	print("Ta xrhmata se " + crypto + " einai " + str(value))

print("Sinolo " + str(total))
