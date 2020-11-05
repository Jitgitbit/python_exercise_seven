import json

from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
	word = word.lower()
	if word in data:
		return data[word]
	elif word.title() in data:
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]
	elif len(get_close_matches(word , data.keys())) > 0:
		print("Did you mean '%s' instead?" %get_close_matches(word , data.keys())[0])
		decide = input("Press y for yes or n for no: ")
		if decide == "y":
			return data[get_close_matches(word , data.keys())[0]]
		elif decide == "n":
			return("That must have been a typo.")
		else:
			return("Please enter valid input, y or n.")

	else:
		print("That word is not listed in this dictionary.")


word = input("Enter the word that you want to search here: ")
output = translate(word)
if type(output) == list:
	for item in output:
		print("- " + item)
else:
	print(output)