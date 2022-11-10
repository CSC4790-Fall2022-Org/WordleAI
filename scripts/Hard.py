import numpy as np
import sys
import string


if __name__ == '__main__':
    #Read in WordList
    my_file = open("resources/solutions.txt", "r")
    wordList = my_file.read().split("\n")
    my_file.close()
    # Create Map to store possible letters
    possible_letters = dict.fromkeys(range(5), list(string.ascii_lowercase))
    greens = [None, None, None, None, None]
    yellows = []

    guessHistory = sys.argv[1].strip("[]").split(",")
    context = sys.argv[2].strip("[]").split(",")

    for i in range(len(context)):
        for j in range(5):
            currLetter = guessHistory[i][j]

            #If we recieve gray, remove that letter from all positions in map
            if context[i][j] == '0':
                for k in range(5):
                    currLetters = possible_letters.get(k)
                    currLetters = currLetters.remove(currLetter)
                    possible_letters.update({k: currLetters})

            #If we recieve yellow, remove that postion from that letter in map
            elif context[i][j] == '1':
                currLetters = possible_letters.get(j)
                currLetters = currLetters.remove(currLetter)
                possible_letters.update({j: currLetters})
                yellows.append(currLetter)

            #If we recieve green, remove all other letters from that position in map    
            else:
                possible_letters.update({j: list(currLetter)})
                greens[j] = currLetter
                
                


    
    #If we recieve green, remove all other letters from that position in map

    # Receive information as letter --> 0,1,2 (gray, yellow, green) or two arrays matching [row,col]

    #CASE TO CONSIDER:
    #Guess is "guess" and one 's' is yellow and one is gray
    #Solution: Remove from those positions, leave in the other positions


    guess = np.random.choice(wordList)
    print(guess)

    # print(sys.argv[1]) argv 1 is word. argv 2 is 0,1,2 context
    sys.stdout.flush()


    
    