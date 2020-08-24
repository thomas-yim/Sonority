"""
Thomas Yim
August 10 2020
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
        
def setupBlockTest(blockAudioTrue, blockAudioFalse, ranking, phase):
    #This next part will be setting up the test within the block
    testAudioTrue = []
    testImagesTrue = []
    truePos = []
    
    testImagesFalse = []
    falsePos = []
    
    currentPhase = []
    for k in range(0, len(blockAudioTrue)):
        trueIndex = random.randint(0, len(blockAudioTrue)-1)
        trueAudio = blockAudioTrue[trueIndex]
        testAudioTrue.append("trainingaudio/" + correctAudio(ranking, trueAudio))
        
        imageLocation = findImage(trueAudio)            
        testImagesTrue.append(imageLocation)

        del blockAudioTrue[trueIndex]
    
        
        falseIndex = random.randint(0, len(blockAudioFalse)-1)
        falseAudio = blockAudioFalse[falseIndex]
        
        imageLocation = findImage(falseAudio)
        testImagesFalse.append(imageLocation)
        
        del blockAudioFalse[falseIndex]
        
            
        if random.randint(0,1) == 1:
            truePos.append(0.5)
            falsePos.append(-0.5)
        else:
            truePos.append(-0.5)
            falsePos.append(0.5)
            
        currentPhase.append(phase)
    

    testData = {"audioTrue": testAudioTrue, "imageTrue": testImagesTrue,
                "currentPhase": currentPhase, "imageFalse": testImagesFalse,
                "truePos": truePos, "falsePos": falsePos}
    testColumns = ["audioTrue", "imageTrue", "currentPhase",
                   "imageFalse","truePos", "falsePos"]
    testdf = pd.DataFrame(testData, columns=testColumns)
    return testdf

"""
This will set up the condition files for the first blocks of the training files
and then link them all to one loop condition file.
It will return the lists of block and test files
"""
def setupTrain(trainingAudio, wordsPerBlock, numBlocks, ranking, toFolder, usedTrue, usedFalse, phase):
    trainConditions = []
    testConditions = []
    
    tempAudio = trainingAudio.copy()

    for i in range(1, numBlocks + 1):
        
        trainConditionName = phase + "Block" + str(i) + ".xlsx"
        testConditionName = phase + "Block" + str(i) + "Test.xlsx"

        blockAudio = []
        blockTrue = []
        blockFalse = []
        imageLoc = []
        
        for j in range(0, int(wordsPerBlock/2)):
            trueInd = random.randint(0, int(len(tempAudio)-1))
            
            while tempAudio[trueInd] in usedTrue:
                trueInd = random.randint(0, int(len(tempAudio)-1))
            
            trueAudio = tempAudio[trueInd]
            usedTrue.append(trueAudio)
            blockTrue.append(trueAudio)
            
            blockAudio.append("trainingaudio/" + correctAudio(ranking, trueAudio))
                    
            del tempAudio[trueInd]
            
            falseInd = random.randint(0, int(len(tempAudio)-1))
            while tempAudio[falseInd] in usedFalse:
                falseInd = random.randint(0, int(len(tempAudio)-1))

            falseAudio = tempAudio[falseInd]
            usedFalse.append(falseAudio)
            blockFalse.append(falseAudio)
            
            blockAudio.append("trainingaudio/" + correctAudio(ranking, falseAudio))
                    
            del tempAudio[falseInd]
            
            random.shuffle(blockAudio)
                

        for audio in blockAudio:
            imageLoc.append(findImage(audio.split('/')[1]))

        trainData = {"audio":blockAudio, "imageLoc":imageLoc}
        trainColumns = ["audio", "imageLoc"]
        traindf = pd.DataFrame(trainData, columns=trainColumns)
        traindf.to_excel(toFolder + trainConditionName, index=False)
        
        testdf = setupBlockTest(blockTrue, blockFalse, ranking, phase)
        testdf.to_excel(toFolder + testConditionName, index=False)
        
        trainConditions.append(toFolder + trainConditionName)
        testConditions.append(toFolder + testConditionName)
    
    return usedTrue, usedFalse, trainConditions, testConditions
            

def setupTest(audioFolder, uniqueAudio, totalQuestions, pastList1, pastList2, phase):
    firstAudioFiles = []
    secondAudioFiles = []
    whichAudioCorrect = []
    relatedImages = []
    currentPhase = []
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
        print(correct)
        
        if incorrect in pastList1 or incorrect in pastList2:
            incorrect = possibilities[0]
        if incorrect in firstAudioFiles or incorrect in secondAudioFiles:
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
            print(secondAudioFiles[-1])
            whichAudioCorrect.append(2)

        relatedImages.append(correspImage)
        currentPhase.append(phase)
        
    return firstAudioFiles, secondAudioFiles, relatedImages, whichAudioCorrect, currentPhase
    

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
    

    """
    TRAIN 1
    """
    #Part 1
    usedTrue, usedFalse, audioCond, testCond = setupTrain(
        uniqueTrainAudio, 2, 14, ranking, toFolder, [], [], "train1P1")
    #Create a Data Frame to be exported. This will be the second loop condition.
    df = pd.DataFrame({"condFiles":audioCond, "testFiles":testCond},
                                columns=['condFiles', "testFiles"])
    df.to_excel(toFolder + "train1P1LoopCondition.xlsx", index=False)
    
    #Part 2
    usedTrue, usedFalse, audioCond, testCond = setupTrain(
        uniqueTrainAudio, 4, 7, ranking, toFolder, usedTrue, usedFalse, "train1P2")
    df = pd.DataFrame({"condFiles":audioCond, "testFiles":testCond},
                                columns=['condFiles', "testFiles"])
    df.to_excel(toFolder + "train1P2LoopCondition.xlsx", index=False)


    """
    TRAIN 2
    """
    #Part 1
    usedTrue, usedFalse, audioCond, testCond = setupTrain(
        uniqueTrainAudio, 2, 14, ranking, toFolder, [], [], "train2P1")
    df = pd.DataFrame({"condFiles":audioCond, "testFiles":testCond},
                                columns=['condFiles', "testFiles"])
    df.to_excel(toFolder + "train2P1LoopCondition.xlsx", index=False)
    
    #Part 2
    usedTrue, usedFalse, audioCond, testCond = setupTrain(
        uniqueTrainAudio, 4, 7, ranking, toFolder, usedTrue, usedFalse, "train2P2")
    df = pd.DataFrame({"condFiles":audioCond, "testFiles":testCond},
                                columns=['condFiles', "testFiles"])
    df.to_excel(toFolder + "train2P2LoopCondition.xlsx", index=False)


    """
    TEST 1
    """
    firstAudio, secondAudio, images, correctLabels, currentPhase = setupTest('trainingaudio/',
                                            uniqueTrainAudio, 2*trainingCount, [], [], "test1")
    test1Data = {"firstAudio": firstAudio,
                "secondAudio": secondAudio,
                "imageLoc": images,
                "whichAudio": correctLabels,
                "currentPhase": currentPhase}

    columns = ["firstAudio", "secondAudio", "imageLoc", "whichAudio", "currentPhase"]
    test1Df = pd.DataFrame(test1Data, columns=columns)
    test1Df.to_excel(toFolder + "test1Conditions.xlsx", index = False)
    
    
    """
    TEST 2
    """
    firstAudio, secondAudio, images, correctLabels, currentPhase = setupTest('novelaudio/',
                                        uniqueNovelAudio, novelCount, [], [], "test2")
    test2Data = {"firstAudio": firstAudio,
                "secondAudio": secondAudio,
                "imageLoc": images,
                "whichAudio": correctLabels,
                "currentPhase": currentPhase}
    columns = ["firstAudio", "secondAudio", "imageLoc", "whichAudio", "currentPhase"]
    test2Df = pd.DataFrame(test2Data, columns=columns)
    test2Df.to_excel(toFolder + "test2Conditions.xlsx", index = False)
    
    
    """
    TEST 3
    """
    firstAudio, secondAudio, images, correctLabels, currentPhase = setupTest('novelaudio/', uniqueNovelAudio,
                                    novelCount, firstAudio, secondAudio, "test3")
    test3Data = {"firstAudio": firstAudio,
                "secondAudio": secondAudio,
                "imageLoc": images,
                "whichAudio": correctLabels,
                "currentPhase": currentPhase}
    columns = ["firstAudio", "secondAudio", "imageLoc", "whichAudio", "currentPhase"]
    test3Df = pd.DataFrame(test3Data, columns=columns)
    test3Df.to_excel(toFolder + "test3Conditions.xlsx", index = False)
    
else:
    print("This setup doesn't work")
