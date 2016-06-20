test__entries = [
	[
		"Szymon",
		"Analogiczna misja tego roku?",
		["analogia", "misja"]
	],
	[	
		"Agatka",
		"Jaka klawiature kupic?",
		["klawiatura", "kupno"],
	],
	[
		"Agatka",
		"Piekne drzewa owocowe naszły na się...",
		["wazne", "pieknedrzewa", "owadynocne"],
	],
	[
		"Agatka",
		"Czym sa drzewa? Pieknem?",
		["wazne", "pieknedrzewa"]
	]
]

test__user = []
for entry in test__entries:
	user = entry[0]
	if not user in test__user:
		test__user.append(entry[0])
test__user = test__user.sort()

test__sentenes__agata_wazne = [
	"Piekne drzewa owocowe naszły na się..."
	"Czym sa drzewa? Pieknem?",
]