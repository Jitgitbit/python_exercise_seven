import json

data = json.load(open("data.json"))

def translate(word):
	if word in data:
		return data[word]


word = input("Enter the word that you want to search here: ")
output = translate(word)
print(output)