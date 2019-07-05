import requests
import pprint
url = "https://googledictionaryapi.eu-gb.mybluemix.net/"
params= {'define':'', 'lang':"en"}
while True:
	word = input("Word: ")
	if word == "q":
		break
	params['define'] = word
	r = requests.get(url, params)
	dict = r.json()[0]
	meaning = dict['meaning']
	pprint.pprint(meaning)
	print(dict['origin'])