from shutil import copyfile
import os


#This sets up novelAudio
with open("wordlist.txt", 'r') as file:
    words = file.readlines()

for i in range(27, len(words)):
    word = words[i].strip("\n")
    if i < 10:
        number = "0" + str(i+1)
    else:
        number = str(i+1)
    for j in range(1,4):
        copyfile("a.wav", "novelaudio/" + number + "_" + word + str(j) + ".wav")
     
"""
words = os.listdir("trainaudio/.")
for i in range(0, 27):
    word = words[i].strip("\n")
    if i < 10:
        number = "0" + str(i+1)
    else:
        number = str(i+1)
    for j in range(1,4):
        copyfile("trainaudio/" + word, "trainingaudio/" + word[:-4] + str(j) + ".wav")
"""