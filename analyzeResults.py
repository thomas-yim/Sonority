import pandas as pd
import math

filename = "1_sonority_2020_Jul_12_1533.csv" #input("Input name of experiment output file: ")
df = pd.read_csv("data/" + filename)

def calculateTrainTest(df):
    audio = df['audioTrue']
    questionIndexes = []
    for i in range(0, len(audio)):
        if type(audio[i]) == str:
            questionIndexes.append(i)
    empty = 0
    correct = 0
    total = 0
    for index in questionIndexes:
        total += 1
        if df['key_resp.keys'][index] == 'None':
            empty += 1
        elif df['truePos'][index] == -0.5 and df['key_resp.keys'][index] == 'f':
            correct += 1
        elif df['truePos'][index] == 0.5 and df['key_resp.keys'][index] == 'j':
            correct += 1
    print(correct)
    print(empty)
    print(total)
    
calculateTest1(df)
    