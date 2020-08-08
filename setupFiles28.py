"""
Thomas Yim
July 1 2020
Sonority Experiment Setup 14x2 and 7x4
"""

import matplotlib.pyplot as plt
import os
import numpy
import random
import pandas as pd
from correctAnswers import correctAudio


def findImage(audioFile):
    images = os.listdir("pngimages/.")
    for image in images:
        if image[0:2] == audioFile[0:2]:
            location = "pngimages/" + image
            return location
        
def setupBlockTest(blockAudioTrue, blockAudioFalse, ranking):
    #This next part will be setting up the test within the block
    testAudioTrue = []
    testImagesTrue = []
    truePos = []
    
    testAudioFalse = []
    testImagesFalse = []
    falsePos = []
    previousAudio = ""
    for k in range(0, len(blockAudioTrue)):
        trueIndex = random.randint(0, len(blockAudioTrue)-1)
        trueAudio = blockAudioTrue[trueIndex]
        testAudioTrue.append("trainingaudio/" + correctAudio(ranking, trueAudio))
        
        imageLocation = findImage(trueAudio)
            
        testImagesTrue.append(imageLocation)
        previousAudio = trueAudio
        del blockAudioTrue[trueIndex]
    
        
        falseIndex = random.randint(0, len(blockAudioFalse)-1)
        while blockAudioFalse[falseIndex] == trueAudio:
            falseIndex = random.randint(0, len(blockAudioFalse)-1)
        falseAudio = blockAudioFalse[falseIndex]            
        testAudioFalse.append("trainingaudio/" + correctAudio(ranking, falseAudio))
        
        imageLocation = findImage(falseAudio)
            
        testImagesFalse.append(imageLocation)
        del blockAudioFalse[falseIndex]
        
            
        if random.randint(0,1) == 1:
            truePos.append(0.5)
            falsePos.append(-0.5)
        else:
            truePos.append(-0.5)
            falsePos.append(0.5)
        
    testData = {"audioTrue": testAudioTrue, "imageTrue": testImagesTrue,
                "audioFalse": testAudioFalse, "imageFalse": testImagesFalse,
                "truePos": truePos, "falsePos": falsePos}
    testColumns = ["audioTrue", "imageTrue", "audioFalse",
                   "imageFalse","truePos", "falsePos"]
    testdf = pd.DataFrame(testData, columns=testColumns)
    return testdf

def setupTrainSubPhase(trainingAudio, trainConditions, testConditions, start, end, wordsPerBlock, phase):
    #This will be used to make sure a word is the right answer once.
    tempAudio = trainingAudio.copy()
    
    #This array is to check if the word was used in the previous block
    #We want to space out the words
    previousBlock = []

    for i in range(start, end):
        currentBlock = []
        
        trainConditionName = phase + "Block" + str(i) + ".xlsx"
        testConditionName = phase + "Block" + str(i) + "Test.xlsx"
        
        blockAudioTrue = []
        blockAudioFalse = []
        blockAudio = []
        imageLoc = []
        
        for j in range(0, int(wordsPerBlock/2)):
            trueInd = random.randint(0, int(len(tempAudio)-1))
            while tempAudio[trueInd] in previousBlock or tempAudio[trueInd] in currentBlock:
                trueInd = random.randint(0, int(len(tempAudio)-1))
            trueAudio = tempAudio[trueInd]
            currentBlock.append(trueAudio)
            blockAudioTrue.append(trueAudio)
            blockAudio.append("trainingaudio/" + correctAudio(ranking, trueAudio))
            imageLoc.append(findImage(tempAudio[trueInd]))
                    
            del tempAudio[trueInd]
            
            falseInd = random.randint(0, int(len(tempAudio)-1))
            while tempAudio[falseInd] in previousBlock or tempAudio[falseInd] in currentBlock or tempAudio[falseInd] == trueAudio:
                falseInd = random.randint(0, int(len(tempAudio)-1))
            currentBlock.append(tempAudio[falseInd])
            blockAudioFalse.append(tempAudio[falseInd])
            blockAudio.append("trainingaudio/" + correctAudio(ranking, tempAudio[falseInd]))
            imageLoc.append(findImage(tempAudio[falseInd]))
                    
            del tempAudio[falseInd]
            
            if len(tempAudio) == 0:
                tempAudio = trainingAudio.copy()
                 
        previousBlock = currentBlock
                                
        trainData = {"audio":blockAudio, "imageLoc":imageLoc}
        trainColumns = ["audio", "imageLoc"]
        traindf = pd.DataFrame(trainData, columns=trainColumns)
        traindf.to_excel(toFolder + trainConditionName, index=False)
        
        testdf = setupBlockTest(blockAudioTrue, blockAudioFalse, ranking)
        testdf.to_excel(toFolder + testConditionName, index=False)
        
        trainConditions.append(toFolder + trainConditionName)
        testConditions.append(toFolder + testConditionName)    
    return trainConditions, testConditions


"""
This will set up the condition files for the first blocks of the training files
and then link them all to one loop condition file.
It will return the lists of block and test files
"""
def setupTrain(trainingAudio, ranking, toFolder, phase):
    trainConditions = []
    testConditions = []


    trainConditions, testConditions = setupTrainSubPhase(trainingAudio, trainConditions, testConditions, 1, 15, 2, phase)
    trainConditions, testConditions = setupTrainSubPhase(trainingAudio, trainConditions, testConditions, 15, 22, 4, phase)
    
    return trainConditions, testConditions
            

def setupTest(audioFolder, uniqueAudio, totalQuestions, pastList1, pastList2):
    firstAudioFiles = []
    secondAudioFiles = []
    whichAudioCorrect = []
    relatedImages = []
    audioCopy = uniqueAudio.copy()
    
    for i in range(0, totalQuestions):
        if len(audioCopy) > 1:
            randomIndex = random.randint(0, len(audioCopy)-1)
        else:
            randomIndex = 0
        file = audioCopy[randomIndex]
        del audioCopy[randomIndex]
        
        if len(audioCopy) == 0:
            audioCopy = uniqueAudio.copy()
        
        possibilities = [file + "1.wav", file + "2.wav", file + "3.wav"]
        correct = correctAudio(ranking, file)
        possibilities.remove(correct)
        incorrectIndex = random.randint(0,1)
        incorrect = possibilities[incorrectIndex]
        del possibilities[incorrectIndex]
        
        if incorrect in pastList1 or incorrect in pastList2:
            incorrect = possibilities[0]
        elif incorrect in firstAudioFiles or incorrect in secondAudioFiles:
            incorrect = possibilities[0]
        
        correspImage = findImage(correct)
            
        
        #This is how we randomize the presentation of the audio. There is no random for start time in builder (or coder for that matter)
        if random.randint(0,1) == 0:
            firstAudioFiles.append(audioFolder + correct)
            secondAudioFiles.append(audioFolder + incorrect)
            whichAudioCorrect.append(1)
        else:
            firstAudioFiles.append(audioFolder + incorrect)
            secondAudioFiles.append(audioFolder + correct)
            whichAudioCorrect.append(2)

        relatedImages.append(correspImage)
        
    return firstAudioFiles, secondAudioFiles, relatedImages, whichAudioCorrect
    

wordCount = 82
novelCount = 54
trainingCount = 28
train1blocksP1 = 14
train1wordsPerBlockP1 = 2
train1blocksP2 = 7
train1wordsPerBlockP2 = 4
train2blocksP1 = 14
train2wordsPerBlockP1 = 2
train2blocksP2= 7
train2wordsPerBlockP2 = 4

trainingAudioFilenames = os.listdir('trainingaudio/.')
novelAudioFilenames = os.listdir('novelaudio/.')
#Get a list of all the unique audio in the form number_word. No wav or stress location
uniqueTrainAudio = list(dict.fromkeys([x[0:-5] for x in trainingAudioFilenames]))
uniqueNovelAudio = list(dict.fromkeys([y[0:-5] for y in novelAudioFilenames]))

#IMPORTANT!!! if this is set then it will randomize the same way every time.
random.seed(31)

setupWorks = True
if ((novelCount + trainingCount) != wordCount):
    setupWorks = False
elif (train1blocksP1*train1wordsPerBlockP1 + train1blocksP2*train1wordsPerBlockP2) % trainingCount != 0:
    setupWorks = False
elif (train2blocksP1*train2wordsPerBlockP1 + train2blocksP2*train2wordsPerBlockP2) % trainingCount != 0:
    setupWorks = False
    
    
if setupWorks:
    
    firstVowel = input("What is the vowel to be stressed first? ")
    secondVowel = input("What is the vowel to be stressed second? ")
    thirdVowel = input("What is the vowel to be stressed third? ")
    
    ranking = [firstVowel, secondVowel, thirdVowel]
    
    toFolder = "".join(ranking) + "Conditions/"
    
    train1conditions, train1TestConditions = setupTrain(uniqueTrainAudio, ranking, toFolder, "train1")
    dfTrain1 = pd.DataFrame({"condFiles":train1conditions, "testFiles":train1TestConditions},
                                columns=['condFiles', "testFiles"])
    dfTrain1.to_excel(toFolder + "train1LoopCondition.xlsx", index=False)

    train2conditions, train2TestConditions = setupTrain(uniqueTrainAudio, ranking, toFolder, "train2")
    dfTrain2 = pd.DataFrame({"condFiles":train2conditions, "testFiles":train2TestConditions},
                                columns=['condFiles', 'testFiles'])
    dfTrain2.to_excel(toFolder + "train2LoopCondition.xlsx", index=False)

    firstAudio, secondAudio, images, correctLabels = setupTest('trainingaudio/',uniqueTrainAudio, 2*trainingCount, [], [])
    test1Data = {"firstAudio": firstAudio,
                "secondAudio": secondAudio,
                "imageLoc": images,
                "whichAudio": correctLabels}
    columns = ["firstAudio", "secondAudio", "imageLoc", "whichAudio"]
    test1Df = pd.DataFrame(test1Data, columns=columns)
    test1Df.to_excel(toFolder + "test1Conditions.xlsx", index = False)
    
    firstAudio, secondAudio, images, correctLabels = setupTest('novelaudio/', uniqueNovelAudio, novelCount, [], [])
    test2Data = {"firstAudio": firstAudio,
                "secondAudio": secondAudio,
                "imageLoc": images,
                "whichAudio": correctLabels}
    columns = ["firstAudio", "secondAudio", "imageLoc", "whichAudio"]
    test2Df = pd.DataFrame(test2Data, columns=columns)
    test2Df.to_excel(toFolder + "test2Conditions.xlsx", index = False)
    
    firstAudio, secondAudio, images, correctLabels = setupTest('novelaudio/', uniqueNovelAudio, novelCount, firstAudio, secondAudio)
    test3Data = {"firstAudio": firstAudio,
                "secondAudio": secondAudio,
                "imageLoc": images,
                "whichAudio": correctLabels}
    columns = ["firstAudio", "secondAudio", "imageLoc", "whichAudio"]
    test3Df = pd.DataFrame(test3Data, columns=columns)
    test3Df.to_excel(toFolder + "test3Conditions.xlsx", index = False)
else:
    print("This setup doesn't work")
