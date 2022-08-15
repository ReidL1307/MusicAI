import random

chords = {
    "0": "C",
    "1": "D",
    "2": "E",
    "3": "F",
    "4": "G",
    "5": "A",
    "6": "B"
}
chordProg = []

for i in range(0, random.randint(2, 5)):
    chordProg.append(chords[str(random.randint(0, 6))])
    if chordProg[i] == chordProg[i-1]:
        print("")
                        
print(chordProg)
print(chords.get(chordProg[0]))
