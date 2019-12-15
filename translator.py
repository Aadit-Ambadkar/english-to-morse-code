#This is the translator for the english-to-morse-code repo
english = input("Code to translate:\n")
print()
english = english.lower()
# print(english)
chars = list(english)
# print(chars)
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
newchars = [dicts[i] for i in chars]
print("".join(newchars))