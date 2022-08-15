import numpy as np
chords = ["C", "D", "E", "F", "G", "A", "B"]

newChords = []

chordProg = np.random.randint(0,6,5)

for i in chordProg:
    newChords.append(chords[i])

newChords = list(set(newChords)) 

                        
print(newChords)
