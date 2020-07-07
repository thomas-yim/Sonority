import matplotlib.pyplot as plt
import os
import numpy
import random
import pandas as pd
from correctAnswers import correctAudio

def setupBlock(phase, trainingAudio, wordsPerBlock, numBlocks):
    trainConditions = []
    testConditions = []

    tempAudio = trainingAudio.copy()
    images = os.listdir("pngimages/.")
    
    previousBlock = []
    for i in range(1, numBlocks + 1):
        currentBlock = []
        trainConditionName = phase + "Block" + str(i) + ".xlsx"
        testConditionName = phase + "Block" + str(i) + "Test.xlsx"
        audio = []
        imageLoc = []
        for j in range(0, wordsPerBlock):
            if len(tempAudio) > 1:
                audioInd = random.randint(0, len(tempAudio)-1)
            elif len(tempAudio) == 1:
                audioInd = 0
            while tempAudio[audioInd] in previousBlock or tempAudio[audioInd] in currentBlock:
                if len(tempAudio) > 1:
                    audioInd = random.randint(0, len(tempAudio)-1)
                elif len(tempAudio) == 1:
                    audioInd = 0
                    break
            if (tempAudio[audioInd] not in currentBlock) and (tempAudio[audioInd] not in previousBlock):
                currentBlock.append(tempAudio[audioInd])
                
                audio.append("trainaudio/" + tempAudio[audioInd])
                for image in images:
                    if image[0:2] == tempAudio[audioInd][0:2]:
                        imageLoc.append("pngimages/" + image)
                        break
                    
                del tempAudio[audioInd]
                
                if len(tempAudio) == 0:
                    tempAudio = trainingAudio.copy()
        previousBlock = currentBlock
                                
        trainData = {"audio":audio, "imageLoc":imageLoc}
        trainColumns = ["audio", "imageLoc"]
        traindf = pd.DataFrame(trainData, columns=trainColumns)
        traindf.to_excel(os.path.join(toFolder, trainConditionName), index=False)
        
        testAudioTrue = []
        testImagesTrue = []
        truePos = []
        
        testAudioFalse = []
        testImagesFalse = []
        falsePos = []
        
        if phase == "train1":
            numQuestions = int(wordsPerBlock/2)
        else:
            numQuestions = wordsPerBlock
        for k in range(0, numQuestions):
            if phase == "train1":
                trueIndex = k*2
            else:
                trueIndex = k
            if trueIndex + 3 >= wordsPerBlock:
                falseIndex = (trueIndex + 3)%(wordsPerBlock)
            else:
                falseIndex = trueIndex + 3
                
            if random.random() > 0.5:
                truePos.append(0.5)
                falsePos.append(-0.5)
            else:
                truePos.append(-0.5)
                falsePos.append(0.5)
            testAudioTrue.append(audio[trueIndex])
            testImagesTrue.append(imageLoc[trueIndex])

            testAudioFalse.append(audio[falseIndex])
            testImagesFalse.append(imageLoc[falseIndex])
            
        testData = {"audioTrue": testAudioTrue, "imageTrue": testImagesTrue,
                    "audioFalse": testAudioFalse, "imageFalse": testImagesFalse,
                    "truePos": truePos, "falsePos": falsePos}
        testColumns = ["audioTrue", "imageTrue", "audioFalse",
                       "imageFalse","truePos", "falsePos"]
        testdf = pd.DataFrame(testData, columns=testColumns)
        testdf.to_excel(os.path.join(toFolder, testConditionName), index=False)
        
        trainConditions.append(os.path.join(toFolder, trainConditionName))
        testConditions.append(os.path.join(toFolder, testConditionName))
    
    return trainConditions, testConditions

trainingAudio = os.listdir('trainaudio/.')
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
    
    firstVowel = input("What is the vowel to be stressed first? ")
    secondVowel = input("What is the vowel to be stressed second? ")
    thirdVowel = input("What is the vowel to be stressed third? ")
    
    ranking = [firstVowel, secondVowel, thirdVowel]
    
    train1conditions, train1TestConditions = setupBlock("train1", trainingAudio, train1wordsPerBlock, train1blocks)
    dfTrain1 = pd.DataFrame({"condFiles":train1conditions, "testFiles":train1TestConditions},
                                columns=['condFiles', "testFiles"])
    dfTrain1.to_excel(os.path.join(toFolder, "train1LoopCondition.xlsx"), index=False)
    train2conditions, train2TestConditions = setupBlock("train2", trainingAudio, train2wordsPerBlock, train2blocks)
    dfTrain2 = pd.DataFrame({"condFiles":train2conditions, "testFiles":train2TestConditions},
                                columns=['condFiles', 'testFiles'])
    dfTrain2.to_excel(os.path.join(toFolder, "train2LoopCondition.xlsx"), index=False)
    
    
    with open("wordlist.txt", "r") as wordfile:
        words = wordfile.readlines()
        
    images = os.listdir("pngimages/.")
    
    correctAudioFiles = []
    incorrectAudioFiles = []
    relatedImages = []
    for i in range(0, len(words)):
        if i+1 < 10:
            number = "0" + str(i+1)
        else:
            number = str(i+1)
        file = number + "_" + words[i].strip("\n")
        possibilities = [file + "1.wav", file + "2.wav", file + "3.wav"]
        correct = correctAudio(ranking, possibilities[0])
        possibilities.remove(correct)
        incorrect = possibilities[random.randint(0,1)]
        for image in images:
            if image[0:2] == correct[0:2]:
                correspImage = "pngimages/" + image
                break
            
        if i < 27:
            correct = "trainingaudio/" + correct
            incorrect = "trainingaudio/" + incorrect
        else:
            correct = "novelaudio/" + correct
            incorrect = "novelaudio/" + incorrect
            
        correctAudioFiles.append(correct)
        incorrectAudioFiles.append(incorrect)
        relatedImages.append(correspImage)
        
    testData = {"correctAudio": correctAudioFiles,
                "incorrectAudio": incorrectAudioFiles,
                "imageLoc": relatedImages}
    columns = ["correctAudio", "incorrectAudio", "imageLoc"]
    testDf = pd.DataFrame(testData, columns=columns)
    testDf.to_excel(os.path.join(toFolder,"testConditions.xlsx"), index = False)
    
    
        
    
else:
    print("This setup doesn't work")

