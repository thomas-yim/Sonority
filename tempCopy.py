def setupBlock(phase, trainingAudio, wordsPerBlock, numBlocks, ranking):
    trainConditions = []
    testConditions = []

    tempAudio = trainingAudio.copy()
    images = os.listdir("pngimages/.")
    
    usedCorrectAudio = []
    usedIncorrectAudio = []
    
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
                audio.append("trainingaudio/" + correctAudio(ranking, tempAudio[audioInd]))
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
        
        #This next part will be setting up the test within the block
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
        
        questionAudio = audio.copy()
        questionImages = imageLoc.copy()
            
        for k in range(0, numQuestions):
            
            if len(questionAudio) > 1:
                trueIndex = random.randint(0, len(questionAudio)-1)
            elif len(questionAudio) == 1:
                trueIndex = 0
            
            while questionAudio[trueIndex] in usedCorrectAudio:
                if len(questionAudio) > 1:
                    trueIndex = random.randint(0, len(questionAudio)-1)
                elif len(questionAudio) == 1:
                    trueIndex = 0
            trueAudio = questionAudio[trueIndex]
            testAudioTrue.append(trueAudio)
            usedCorrectAudio.append(trueAudio)
            
            for image in images:
                if image[0:2] == trueAudio[len("trainingaudio/"):len("trainingaudio/")+2]:
                    imageLocation = "pngimages/" + image
                    break
            testImagesTrue.append(imageLocation)
            
            del questionAudio[trueIndex]
            del questionImages[trueIndex]
            
            if len(questionAudio) == 0:
                questionAudio = audio.copy()
                questionImages = imageLoc.copy()
            
            if len(questionAudio) > 1:
                    falseIndex = random.randint(0, len(questionAudio)-1)
            elif len(questionAudio) == 1:
                falseIndex = 0
            
            while questionAudio[falseIndex] == trueAudio:
                falseIndex = random.randint(0, len(questionAudio)-1)
                
            while questionAudio[falseIndex] in usedIncorrectAudio:
                if len(questionAudio) > 1:
                    falseIndex = random.randint(0, len(questionAudio)-1)
                elif len(questionAudio) == 1:
                    falseIndex = 0
            
            testAudioFalse.append(questionAudio[falseIndex])
            usedIncorrectAudio.append(questionAudio[falseIndex])
            
            for image in images:
                if image[0:2] == questionAudio[falseIndex][len("trainingaudio/"):len("trainingaudio/")+2]:
                    imageLocation = "pngimages/" + image
                    break
            testImagesFalse.append(imageLocation)
            del questionAudio[falseIndex]
            del questionImages[falseIndex]
            
            if len(questionAudio) == 0:
                questionAudio = audio.copy()
                questionImages = imageLoc.copy()
                
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
        testdf.to_excel(os.path.join(toFolder, testConditionName), index=False)
        
        trainConditions.append(os.path.join(toFolder, trainConditionName))
        testConditions.append(os.path.join(toFolder, testConditionName))
    
    return trainConditions, testConditions