#This is the translator for the english-to-morse-code repo

#Fetching message
english = input("Message to translate:\n")
#Making lowercase for ease and seperating into characters
english = english.lower()
chars = list(english)

#This is the dictionary of morse to english
dicts = {
	"a": ".- ",
	"b": "-... ",
	"c": "-.-. ",
	"d": "-.. ",
	"e": ". ",
	"f": "..-. ",
	"g": "--. ",
	"h": ".... ",
	"i": ".. ",
	"j": ".--- ",
	"k": "-.- ",
	"l": ".-.. ",
	"m": "-- ",
	"n": "-. ",
	"o": "--- ",
	"p": ".--. ",
	"q": "--.- ",
	"r": ".-. ",
	"s": "... ",
	"t": "- ",
	"u": "..- ",
	"v": "...- ",
	"w": ".-- ",
	"x": "-..- ",
	"y": "-.-- ",
	"z": "--.. ",
	"1": ".---- ",
	"2": "..--- ",
	"3": "...-- ",
	"4": "....- ",
	"5": "..... ",
	"6": "-.... ",
	"7": "--... ",
	"8": "---.. ",
	"9": "----. ",
	"0": "----- ",
	" ": "  ",
	".": ".-.-.- ",
	"!": "-.-.-- ",
	"?": "..--.. ",
	",": "--..-- ",
	"'": ".----. ",

}

#Creating the new characters
newchars = [dicts[i] for i in chars]

#Print!
print("".join(newchars))