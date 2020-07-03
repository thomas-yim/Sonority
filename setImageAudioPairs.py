import json
import os

with open("wordList.txt", 'r') as wordFile:
    words = wordFile.readlines()

images = os.listdir("pngimages/.")
images = images[0:len(words)]

pairings = {}
for i in range(0, len(words)):
    word = words[i]
    word = word.rstrip('\n')
    pairings[images[i]] = [word+"1.wav", word+"2.wav", word+"3.wav"]
    
with open("pairings.json", 'w') as pairFile:
    json.dump(pairings, pairFile, indent=4)