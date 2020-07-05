from shutil import copyfile
import os

with open("wordlist.txt", 'r') as file:
    words = file.readlines()

#words = os.listdir("trainaudio/.")
for i in range(27, len(words)):
    word = words[i].strip("\n")
    if i < 10:
        number = "0" + str(i)
    else:
        number = str(i)
    for j in range(1,4):
        copyfile("a.wav", "novelaudio/" + number + "_" + word + str(j) + ".wav")
        