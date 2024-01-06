import random
import time #need to add time.sleep() s
list_of_houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']

chosen_house = random.choice(list_of_houses)
sorting_hat_speech = ["Ahh, right then.\n  Mmm...right.\n Okay,\n ", "Where should I put you,\n lets see \n I know ...", "Ha! Another Weasley\n I know just what to do with you \n", "Hmm... difficult,\n very difficult.\n Plenty of courage I see,\n Not a bad mind either\n There's talent,\n oh yes, and a thirst to prove yourself\n.But where to put you? \nWell if you're sure, better be \n" ]

speech = random.choice(sorting_hat_speech)

print("Sorting hat:\n", speech , chosen_house, "!" )
