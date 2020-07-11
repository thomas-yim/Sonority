def correctAudio(ranking, filename):
    #Based on our naming convention, vowels will always be in these places.
    vowels = [filename[4], filename[6], filename[8]]
    
    #for each vowel in the word, it will add what ranking it is (according to parameter)
    wordRanking = []
    
    for i in range(0, len(vowels)):
        wordRanking.append(ranking.index(vowels[i]))
    
    minIndex = -1
    #This makes sure that the leftmost (highest sonority) syllable is stressed
    for i in range(len(vowels)-1, -1, -1):
        if wordRanking[minIndex] >= wordRanking[i]:
            minIndex = i
            
    #Our naming convention is not 0 indexed so we add 1
    stressLoc = minIndex + 1
            
    return filename[:9] + str(stressLoc) + ".wav"

#rint(correctAudio(['a','o','i'], "01_kitipi"))