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
    pairings[word+"1.wav"] = images[i]
    pairings[word+"2.wav"] = images[i]
    pairings[word+"3.wav"] = images[i]
    
with open("audioToImagePairing.json", 'w') as pairFile:
    json.dump(pairings, pairFile, indent=4)