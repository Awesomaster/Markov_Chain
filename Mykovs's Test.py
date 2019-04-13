import random
import re

# ------------ GATHERING THE DATA ----------------

def gatherData(inputString):
    fileInput = open(inputString, "r")
    # From file

    fileLines = fileInput.readlines()
    # In lines

    fileWords = []
    # In Words

    for i in range(len(fileLines)):
        fileWords += fileLines[i].split()

    for i in range(len(fileWords)):
        fileWords[i] = re.sub('[^a-zA-Z.]+', '', fileWords[i]).lower()
    # All words from input separate
    # print(inputFinal)

    return fileWords

def dataToInteractions(inputWords):
    interactions = []
    # List of word interactions
    
    words = []
    # List of words
    
    lastWord = ""
    pos = 0
    appendSize = 0
    for i in range(len(inputWords)):
        if inputWords[i] in words:
            pos = words.index(inputWords[i])
            # Position of word in words
        else:
            interactions.append([])
            for k in range(appendSize):
                interactions[len(interactions) - 1].append(0.0)
            for j in range(len(interactions)):
                interactions[j].append(0.0)
            # Initiate new interaction

            appendSize += 1  # Each new interaction needs to start with more 0's
            words.append(inputWords[i])  # Add the word to the list of words as well as show where it is in interactions
            pos = words.index(inputWords[i])  # The position in words/interactions

        if i > 0:
            interactions[words.index(lastWord)][pos] += 1
            # Add a connection

        lastWord = inputWords[i]
        # Define what the last word was

    return [interactions, words]



# ------------ TURNING THE DATA INTO AN APPROPRIATE FORM

def numbersToPercent(interactionList):
    total = 0
    for i in range(len(interactionList)):
        for j in range(len(interactionList[i])):
            total += interactionList[i][j]
        if total < 1:
            total = 1
        for k in range(len(interactionList[i])):
            interactionList[i][k] = interactionList[i][k] / total
        total = 0

    return interactionList


# ------------ PRINTING OF THE DATA --------------

def generateSentences(interactions, words):
    chance = 0
    current = 0
    sentence = ""
    while True:
        randNum = random.random()
        for j in range(len(interactions)):
            chance += interactions[current][j]
            if randNum <= chance:
                if '.' in words[j]:
                    return sentence + words[j]
                else:
                    sentence += words[j] + " "
                current = j
                
                break
            
        chance = 0

data = gatherData("markov.txt")
print("1")
interactionsAndWords = dataToInteractions(data)
print("2")
interactions = interactionsAndWords[0]
print("3")
words = interactionsAndWords[1]
print("4")
interactions = numbersToPercent(interactions)
print("5")
for i in range(15):
    print(generateSentences(interactions, words))
print("6")
