from tkinter import Tk
from tkinter.filedialog import askopenfilenames, askdirectory
import pandas as pd
from ntpath import basename
import pkg_resources.py2_warn
from datetime import datetime


Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filenames = askopenfilenames(title='Choose file(s)', filetypes = (("CSV Files", "*.xlsx"),)) # show an "Open" dialog box and return the path to the selected file
toFolder = askdirectory(title="Choose output folder")
print(toFolder)

now = datetime.now()
timearray = str(now).split()
time = timearray[0] + timearray[1].split(":")[0] + timearray[1].split(":")[1]

writer = pd.ExcelWriter(toFolder + "/" + time + "_aggregate.xlsx", engine='xlsxwriter')

### AGGREGATES ###
allParticipants = []
allAudio1 = []
allAudio2 = []
allTrueImage = []
allFalseImage = []
allCorrect = []
allReactionTime = []
allTrueKey = []
allStressPos = []
allStressedVowel = []
allPhase = []
allRules = []
allChosenVowel = []
allChosenStressPos = []

"""
TRAIN 1
"""

participants = []
audio = []
trueImage = []
falseImage = []
correct = []
reactionTime = []
trueKey = []
stressedPos = []
stressedVowel = []

for filename in filenames:
    userID = int(filename.split("_")[0].split("/")[-1])
    xls = pd.ExcelFile(filename)
    df = pd.read_excel(xls, "Train 1")
    for ii in range(0, len(df['True Image'])):
        allPhase.append("Train 1")
        
        participants.append(userID)
        allParticipants.append(userID)
        
        audio.append(df["Audio"][ii])
        allAudio1.append(df["Audio"][ii])
        
        trueImage.append(df["True Image"][ii])
        allTrueImage.append(df["True Image"][ii])
        
        falseImage.append(df["False Image"][ii])
        allFalseImage.append(df["False Image"][ii])
        
        correct.append(df["Correct"][ii])
        allCorrect.append(df["Correct"][ii])
        
        reactionTime.append(df["Reaction Time"][ii])
        allReactionTime.append(df["Reaction Time"][ii])
        
        trueKey.append(df["True Key"][ii])
        allTrueKey.append(df["True Key"][ii])
        
        pos = int(df["Audio"][ii].split(".")[0][-1])
        stressedPos.append(pos)
        allStressPos.append(pos)
        if pos == 1:
            vowel = df["Audio"][ii][4]
        elif pos == 2:
            vowel = df["Audio"][ii][6]
        elif pos == 3:
            vowel = df["Audio"][ii][8]
            
        stressedVowel.append(vowel)
        allStressedVowel.append(vowel)
        
        allAudio2.append("na")
        allChosenVowel.append("na")
        allChosenStressPos.append("na")
        allRules.append("na")

data = {"Participant": participants, "Audio": audio, "TrueImage": trueImage, "FalseImage": falseImage,
                "Correct": correct, "ReactionTime": reactionTime, "TrueKey": trueKey,
                "StressedPos": stressedPos, "StressedVowel": stressedVowel}
columns = ["Participant", "Audio", "TrueImage", "FalseImage",
           "Correct","ReactionTime", "TrueKey","StressedPos","StressedVowel"]
dfNew = pd.DataFrame(data, columns=columns)
dfNew.to_excel(writer, sheet_name="Train 1", index = False)



"""
TEST 1, 2, and 3
"""
for j in range(1,4):
    participants = []
    images = []
    audio1 = []
    audio2 = []
    trueAudio = []
    correct = []
    reactionTime = []
    trueKey = []
    stressedPos = []
    stressedVowel = []
    rules = []
    chosenVowel = []
    chosenStressPos = []
    
    for filename in filenames:
        userID = int(filename.split("_")[0].split("/")[-1])
        xls = pd.ExcelFile(filename)
        df = pd.read_excel(xls, "Test " + str(j))
        for ii in range(0, len(df['Images'])):
            allPhase.append("Test" + str(j))
            
            participants.append(userID)
            allParticipants.append(userID)
            
            images.append(df["Images"][ii])
            allTrueImage.append(df["Images"][ii])
            
            audio1.append(df["Audio 1"][ii])
            allAudio1.append(df["Audio 1"][ii])
            
            audio2.append(df["Audio 2"][ii])
            allAudio2.append(df["Audio 2"][ii])
            
            trueAudio.append(df["True Audio"][ii])
            
            correct.append(df["Correct"][ii])
            allCorrect.append(df["Correct"][ii])
            
            reactionTime.append(df["Reaction Time"][ii])
            allReactionTime.append(df["Reaction Time"][ii])
            
            trueKey.append(df["True Key"][ii])
            allTrueKey.append(df["True Key"][ii])
            
            if df["True Key"][ii] == "f":
                correctAudio = df["Audio 1"][ii]
                incorrectAudio = df["Audio 2"][ii]
            elif df["True Key"][ii] == "j":
                correctAudio = df["Audio 2"][ii]
                incorrectAudio = df["Audio 1"][ii]
                
            pos = int(correctAudio.split(".")[0][-1])
            stressedPos.append(pos)
            allStressPos.append(pos)
            
            if pos == 1:
                vowel = correctAudio[4]
                rule = "default"
            elif pos == 2:
                vowel = correctAudio[6]
                rule = "sonority"
            elif pos == 3:
                vowel = correctAudio[8]
                rule = "sonority"
                
            stressedVowel.append(vowel)
            allStressedVowel.append(vowel)
            
            rules.append(rule)
            allRules.append(rule)
            
            if df["Correct"][ii] == True:
                print("here")
                chosenVowel.append(vowel)
                allChosenVowel.append(vowel)
                
                chosenStressPos.append(pos)
                allChosenStressPos.append(pos)
            else:
                pos = int(incorrectAudio.split(".")[0][-1])
                chosenStressPos.append(pos)
                allChosenStressPos.append(pos)
                if pos == 1:
                    vowel = incorrectAudio[4]
                elif pos == 2:
                    vowel = incorrectAudio[6]
                elif pos == 3:
                    vowel = incorrectAudio[8]
                    
                chosenVowel.append(vowel)
                allChosenVowel.append(vowel)
                
            allFalseImage.append("na")
            
    data = {"Participant": participants, "Images": images, "Audio1": audio1, "Audio2": audio2,
                    "TrueAudio": trueAudio, "Correct": correct, "ReactionTime": reactionTime,
                    "TrueKey": trueKey, "StressedPos": stressedPos, "StressedVowel": stressedVowel,
                    "Rule": rules, "ChosenVowel": chosenVowel, "ChosenStressPos": chosenStressPos}
    columns = ["Participant", "Images", "Audio1", "Audio2", "TrueAudio", "Correct", "ReactionTime",
               "TrueKey", "StressedPos", "StressedVowel", "Rule", "ChosenVowel", "ChosenStressPos"]
    dfNew = pd.DataFrame(data, columns=columns)
    dfNew.to_excel(writer, sheet_name="Test " + str(j), index = False)

"""
OVERVIEW
"""
participants = []
phases = []
correct = []
empty = []
total = []
percentCorrect = []
for filename in filenames:
    userID = int(filename.split("_")[0].split("/")[-1])
    xls = pd.ExcelFile(filename)
    df = pd.read_excel(xls, "Overview")
    for ii in range(0, len(df['Phase'])):
        participants.append(userID)
        phases.append(df['Phase'][ii])
        correct.append(df["Correct"][ii])
        empty.append(df["Empty"][ii])
        total.append(df["Total"][ii])
        percentCorrect.append(df["Percent Correct"][ii])

data = {"Participant": participants, "Phase": phases, "Correct": correct, "Empty": empty,
                "Total": total, "PercentCorrect": percentCorrect}
columns = ["Participant", "Phase", "Correct", "Empty", "Total", "PercentCorrect"]

dfNew = pd.DataFrame(data, columns=columns)
dfNew.to_excel(writer, sheet_name="Overview", index = False)


### AGGREGATE
data = {"Participant": allParticipants, "Audio1": allAudio1, "Audio2": allAudio2, "TrueImage": allTrueImage,
                    "FalseImage": allFalseImage, "Correct": allCorrect, "ReactionTime": allReactionTime,
                    "TrueKey": allTrueKey, "StressedPos": allStressPos, "StressedVowel": allStressedVowel,
                    "Phase": allPhase, "Rule": allRules, "ChosenVowel": allChosenVowel,
                    "ChosenStressPos": allChosenStressPos}

columns = ["Participant", "Audio1", "Audio2", "TrueImage", "FalseImage", "Correct", "ReactionTime",
           "TrueKey", "StressedPos", "StressedVowel", "Phase", "Rule", "ChosenVowel", "ChosenStressPos"]

dfNew = pd.DataFrame(data, columns=columns)
dfNew.to_excel(writer, sheet_name="Aggregate all phase", index = False)

writer.save()
