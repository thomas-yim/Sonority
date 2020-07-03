import matplotlib.pyplot as plt
import os
import numpy
import random
import pandas as pd

def setupBlock(phase, trainingImages, wordsPerBlock, numBlocks):
    trainConditions = []
    tempImages = trainingImages.copy()
    for j in range(1, numBlocks + 1):
        currentBlock = []
        currentConditionName = phase + "Block" + str(j) + "Condition.xlsx"
        audio = []
        imageLoc = []
        for k in range(0, wordsPerBlock):
            audio.append("wavaudio/pakito" + phase[-1] + ".wav")
            if len(tempImages) > 1:
                imageInd = random.randint(0, len(tempImages)-1)
            elif len(tempImages) == 1:
                imageInd = 0
            imageLoc.append("pngimages/" + tempImages[imageInd])
            del tempImages[imageInd]
            if len(tempImages) == 0:
                tempImages = trainingImages.copy()
        
        data = {"audio":audio, "imageLoc":imageLoc}
        columns = ["audio", "imageLoc"]
        df = pd.DataFrame(data, columns=columns)
        df.to_excel(os.path.join(toFolder, currentConditionName), index=False)
        trainConditions.append(toFolder + currentConditionName)
    return trainConditions

listOfFiles = os.listdir('pngimages/.')
wordCount = 81
novelCount = 54
trainingCount = 27
train1blocks = 9
train1wordsPerBlock = 6
train2blocks = 3
train2wordsPerBlock = 9
toFolder = "autoConditions/"
random.seed(30)

setupWorks = True
if ((novelCount + trainingCount) != wordCount):
    setupWorks = False
elif (train1blocks*train1wordsPerBlock%trainingCount != 0):
    setupWorks = False
elif (train2blocks*train2wordsPerBlock%trainingCount != 0):
    setupWorks = False
    
if setupWorks:
    availableImages = []
    for i in range(0, wordCount):
        availableImages.append(listOfFiles[i])
        
    trainingImages = availableImages[0:trainingCount]
    novelImages = availableImages[trainingCount:wordCount]    
    
    train1conditions = setupBlock("train1", trainingImages, train1wordsPerBlock, train1blocks)
    dfTrain1 = pd.DataFrame({"condFiles":train1conditions}, columns=['condFiles'])
    dfTrain1.to_excel(os.path.join(toFolder, "train1LoopCondition.xlsx"), index=False)
    train2conditions = setupBlock("train2", trainingImages, train2wordsPerBlock, train2blocks)
    dfTrain2 = pd.DataFrame({"condFiles":train2conditions}, columns=['condFiles'])
    dfTrain2.to_excel(os.path.join(toFolder, "train2LoopCondition.xlsx"), index=False)
    
    
else:
    print("This setup doesn't work")

