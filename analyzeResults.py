import pandas as pd
import math
import xlsxwriter


filename = "1_sonority_2020_Jul_20_2230.csv" #input("Input name of experiment output file: ")
df = pd.read_csv("data/" + filename)

def calculateAccuracy(df, phase):
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
        else:
            print("Invalid phase")
    
    if "train" in phase:
        data = {"Audio": audio, "True Image": trueImage, "False Image": falseImage,
                "Correct": correct, "Reaction Time": reactionTime}
        columns = ["Audio", "True Image", "False Image", "Correct", "Reaction Time"]
    elif "test" in phase:
        data = {"Images": images, "Audio 1": audio1, "Audio 2": audio2, "True Audio": trueAudio,
                "Correct": correct, "Reaction Time": reactionTime}
        columns = ["Images", "Audio 1", "Audio 2", "True Audio", "Correct", "Reaction Time"]
    
    df = pd.DataFrame(data, columns=columns)
    
    print("Phase: " + phase.title())
    print("Correct: ", correctAnswers)
    print("Unanswered: ", empty)
    print("Total: ", total)
    print("Percentage Correct: ", str(100*(correctAnswers/total)) + "%")
    print()
    
    return df
    
    

dfTrain1 = calculateAccuracy(df, "train1")
dfTrain2 = calculateAccuracy(df, "train2")
dfTest1 = calculateAccuracy(df, "test1")

writer = pd.ExcelWriter('results/' + filename[:-4] + '_results.xlsx', engine='xlsxwriter')
dfTrain1.to_excel(writer, sheet_name='Train 1', index = False)
dfTrain2.to_excel(writer, sheet_name='Train 2', index = False)
dfTest1.to_excel(writer, sheet_name='Test 1', index = False)

writer.save()