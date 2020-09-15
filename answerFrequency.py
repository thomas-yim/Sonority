import os
import pandas as pd

conditionName = "aoiConditions"

conditionFiles = os.listdir(conditionName + '/.')

writer = pd.ExcelWriter('answers.xlsx', engine='xlsxwriter')

fCount1 = 0
jCount1 = 0
answer = []

print("Train")
for file in conditionFiles:
    if file[0:5] == "train" and file[-9:] == "Test.xlsx":
        df = pd.read_excel(conditionName + "/" + file)
        for option in df['truePos']:
            if option == -0.5:
                print("f")
                fCount1 += 1
                answer.append("f")
            else:
                print("j")
                jCount1 += 1
                answer.append("j")
data = {"Answer": answer}
columns = ["Answer"]

pd.DataFrame(data,columns=columns).to_excel(writer, sheet_name="Train", index = False)

print("Number of f: " + str(fCount1))
print("Number of j: " + str(jCount1))
        
fCount2 = 0
jCount2 = 0
answer = []

print("Test 1")
df = pd.read_excel(conditionName + "/test1Conditions.xlsx")
for option in df['whichAudio']:
    if option == 1:
        print("f")
        fCount2 += 1
        answer.append("f")
    else:
        print("j")
        jCount2 += 1
        answer.append("j")
        
data = {"Answer": answer}
columns = ["Answer"]

pd.DataFrame(data,columns=columns).to_excel(writer, sheet_name="Test 1", index = False)

print("Number of f: " + str(fCount2))
print("Number of j: " + str(jCount2))




fCount3 = 0
jCount3 = 0
answer = []

print("Test 2")
df = pd.read_excel(conditionName + "/test2Conditions.xlsx")
for option in df['whichAudio']:
    if option == 1:
        print("f")
        fCount3 += 1
        answer.append("f")
    else:
        print("j")
        jCount3 += 1
        answer.append("j")

data = {"Answer": answer}
columns = ["Answer"]

pd.DataFrame(data,columns=columns).to_excel(writer, sheet_name="Test 2", index = False)
        
print("Number of f: " + str(fCount3))
print("Number of j: " + str(jCount3))




fCount4 = 0
jCount4 = 0
answer = []
        
print("Test 3")
df = pd.read_excel(conditionName + "/test3Conditions.xlsx")
for option in df['whichAudio']:
    if option == 1:
        print("f")
        fCount4 += 1
        answer.append("f")
    else:
        print("j")
        jCount4 += 1
        answer.append("j")
    
data = {"Answer": answer}
columns = ["Answer"]

pd.DataFrame(data,columns=columns).to_excel(writer, sheet_name="Test 3", index = False)

print("Number of f: " + str(fCount4))
print("Number of j: " + str(jCount4))

phases = ["Train", "Test 1", "Test 2", "Test 3"]
data = {"Phase": phases, "Number of F": [fCount1, fCount2, fCount3, fCount4], "Number of J": [jCount1, jCount2, jCount3, jCount4]}
columns = ["Phase", "Number of F", "Number of J"]

pd.DataFrame(data,columns=columns).to_excel(writer, sheet_name="Overview", index = False)

writer.save()