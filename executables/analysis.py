from tkinter import Tk
from tkinter.filedialog import askopenfilenames, askdirectory
import pandas as pd
from ntpath import basename
import pkg_resources.py2_warn

def calculateAccuracy(df, phase):
    questionIndexes = []
    if phase == "postTest":
        if 'correctLabel' in df:
            postTestRows = df['correctLabel']
            for i in range(0, len(postTestRows)):
                if type(postTestRows[i]) == str:
                    questionIndexes.append(i)
    else:
        if 'currentPhase' in df:
            allPhases = df['currentPhase']
            for i in range(0, len(allPhases)):
                if type(allPhases[i]) == str:
                    if phase in allPhases[i]:
                        questionIndexes.append(i)
    if len(questionIndexes) == 0:
        return pd.DataFrame(), "N/A", "N/A", "N/A", "N/A"
                
    empty = 0
    correctAnswers = 0
    total = 0
    
    correct = []
    reactionTime = []
    trueKey = []
    
    #These are the arrays for train phases
    audio = []
    trueImage = []
    falseImage = []
    
    #These are the arrays for test phases
    images = []
    audio1 = []
    audio2 = []
    trueAudio = []
    
    #These are the arrays for the post test phase
    audioA = []
    audioX = []
    audioB = []
    trueAudio = []
    
    for index in questionIndexes:
        
        total += 1

        if "train" in phase:
            audio.append(df['audioTrue'][index].split('/')[1])
            trueImage.append(df['imageTrue'][index].split('/')[1])
            falseImage.append(df['imageFalse'][index].split('/')[1])
            reactionTime.append(df[phase + 'Response.rt'][index])
            
            if df['truePos'][index] == -0.5:
                trueKey.append('f')
            else:
                trueKey.append('j')
            
            if type(df[phase + 'Response.keys'][index]) != str:
                empty += 1
                correct.append("None")
            elif df['truePos'][index] == -0.5 and df[phase + 'Response.keys'][index] == 'f':
                correctAnswers += 1
                correct.append(True)
            elif df['truePos'][index] == 0.5 and df[phase + 'Response.keys'][index] == 'j':
                correctAnswers += 1
                correct.append(True)
            else:
                correct.append(False)
            data = {"Audio": audio, "True Image": trueImage, "False Image": falseImage,
                "Correct": correct, "Reaction Time": reactionTime, "True Key": trueKey}
            columns = ["Audio", "True Image", "False Image", "Correct", "Reaction Time", "True Key"]
        elif "test" in phase:
            images.append(df['imageLoc'][index].split('/')[1])
            audio1.append(df['firstAudio'][index].split('/')[1])
            audio2.append(df['secondAudio'][index].split('/')[1])
            trueAudio.append(df['whichAudio'][index])
            reactionTime.append(df[phase + 'Response.rt'][index])
            
            if df['whichAudio'][index] == 1:
                trueKey.append('f')
            else:
                trueKey.append('j')
            
            if type(df[phase + 'Response.keys'][index]) != str:
                empty += 1
                correct.append("None")
            elif df['whichAudio'][index] == 1 and df[phase + 'Response.keys'][index] == 'f':
                correctAnswers += 1
                correct.append(True)
            elif df['whichAudio'][index] == 2 and df[phase + 'Response.keys'][index] == 'j':
                correctAnswers += 1
                correct.append(True)
            else:
                correct.append(False)
            data = {"Images": images, "Audio 1": audio1, "Audio 2": audio2, "True Audio": trueAudio,
                "Correct": correct, "Reaction Time": reactionTime, "True Key": trueKey}
            columns = ["Images", "Audio 1", "Audio 2", "True Audio", "Correct", "Reaction Time", "True Key"]
        elif "postTest" in phase:
            audioA.append(df['audioA'][index].split('/')[1])
            audioX.append(df['audioX'][index].split('/')[1])
            audioB.append(df['audioB'][index].split('/')[1])
            trueAudio.append(df['correctLabel'][index])
            reactionTime.append(df[phase + 'Response.rt'][index])
            
            if df['correctLabel'][index] == "audioA":
                trueKey.append('f')
            else:
                trueKey.append('j')
            
            if type(df[phase + 'Response.keys'][index]) != str:
                empty += 1
                correct.append("None")
            elif df['correctLabel'][index] == "audioA" and df[phase + 'Response.keys'][index] == 'f':
                correctAnswers += 1
                correct.append(True)
            elif df['correctLabel'][index] == "audioB" and df[phase + 'Response.keys'][index] == 'j':
                correctAnswers += 1
                correct.append(True)
            else:
                correct.append(False)
            data = {"Audio A": audioA, "Audio X": audioX, "Audio B": audioB, "True Audio": trueAudio,
                "Correct": correct, "Reaction Time": reactionTime, "True Key": trueKey}
            columns = ["Audio A", "Audio X", "Audio B", "True Audio", "Correct", "Reaction Time", "True Key"]
        else:
            print("Invalid phase")
    
    df = pd.DataFrame(data, columns=columns)
    
    print("Phase: " + phase.title())
    print("Correct: ", correctAnswers)
    print("Unanswered: ", empty)
    print("Total: ", total)
    print("Percentage Correct: ", str(100*(correctAnswers/total)) + "%")
    print()
    
    return df, correctAnswers, empty, total, str(round(100*(correctAnswers/total), 2)) + "%"

print("Here")
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filenames = askopenfilenames(title='Choose file(s)', filetypes = (("CSV Files", "*.csv"),)) # show an "Open" dialog box and return the path to the selected file
toFolder = askdirectory(title="Choose output folder")
print(toFolder)

for filename in filenames:
    df = pd.read_csv(filename)
    expType = df['ID Number']
    expNumber = 0
    for value in expType:
        if value != None:
            expNumber = value
            
    
    if expNumber == 0:
        expNumber = ""
    
    #Cumulative Results
    phases = []
    numCorrect = []
    numEmpty = []
    numTotal = []
    percentages = []
    
    phaseDict = {"train1": "Train 1", "test1": "Test 1",
              "test2": "Test 2", "test3": "Test 3", "postTest": "PostTest"}
    
    writer = pd.ExcelWriter(toFolder + "/" + str(expNumber) + "_" + basename(filename)[:-4] + '_results.xlsx', engine='xlsxwriter')
    for phase in phaseDict.keys():    
        dfPhase, correct, empty, total, percent = calculateAccuracy(df, phase)
        phases.append(phaseDict[phase])
        numCorrect.append(correct)
        numEmpty.append(empty)
        numTotal.append(total)
        percentages.append(percent)
        dfPhase.to_excel(writer, sheet_name=phaseDict[phase], index = False)
    
    data = {"Phase": phases, "Correct": numCorrect, "Empty": numEmpty,
            "Total": numTotal, "Percent Correct": percentages}
    columns = ["Phase", "Correct", "Empty", "Total", "Percent Correct"]
    pd.DataFrame(data,columns=columns).to_excel(writer, sheet_name="Overview", index = False)
    
    writer.save()
