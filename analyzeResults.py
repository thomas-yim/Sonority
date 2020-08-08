import pandas as pd
import math
import xlsxwriter


filename = "online.csv"#"othercomputertest_sonorityaoi_2020-07-28_22h14.45.527.csv"#"1_sonority_2020_Jul_20_2230.csv" #input("Input name of experiment output file: ")
df = pd.read_csv("data/" + filename)

def calculateAccuracy(df, phase):
    if phase + "Response.keys" in df.columns:
        audio = df[phase + 'Response.keys']
        questionIndexes = []
        for i in range(0, len(audio)):
            if type(audio[i]) == str:
                questionIndexes.append(i)
        empty = 0
        correctAnswers = 0
        total = 0
        
        correct = []
        reactionTime = []
        
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
                if df[phase + 'Response.keys'][index] == 'None':
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
                    "Correct": correct, "Reaction Time": reactionTime}
                columns = ["Audio", "True Image", "False Image", "Correct", "Reaction Time"]
            elif "test" in phase:
                images.append(df['imageLoc'][index].split('/')[1])
                audio1.append(df['firstAudio'][index].split('/')[1])
                audio2.append(df['secondAudio'][index].split('/')[1])
                trueAudio.append(df['whichAudio'][index])
                reactionTime.append(df[phase + 'Response.rt'][index])
                if df[phase + 'Response.keys'][index] == 'None':
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
                    "Correct": correct, "Reaction Time": reactionTime}
                columns = ["Images", "Audio 1", "Audio 2", "True Audio", "Correct", "Reaction Time"]
            elif "postTest" in phase:
                audioA.append(df['audioA'][index].split('/')[1])
                audioX.append(df['audioX'][index].split('/')[1])
                audioB.append(df['audioB'][index].split('/')[1])
                trueAudio.append(df['correctLabel'][index])
                reactionTime.append(df[phase + 'Response.rt'][index])
                if df[phase + 'Response.keys'][index] == 'None':
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
                    "Correct": correct, "Reaction Time": reactionTime}
                columns = ["Audio A", "Audio X", "Audio B", "True Audio", "Correct", "Reaction Time"]
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
    else:
        return pd.DataFrame(), "N/A", "N/A", "N/A", "N/A"
    
#Cumulative Results
phases = []
numCorrect = []
numEmpty = []
numTotal = []
percentages = []

phaseDict = {"train1": "Train 1", "train2": "Train 2", "test1": "Test 1",
          "test2": "Test 2", "test3": "Test 3", "postTest": "PostTest"}

writer = pd.ExcelWriter('results/' + filename[:-4] + '_results.xlsx', engine='xlsxwriter')
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