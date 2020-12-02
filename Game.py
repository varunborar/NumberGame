import random
from os import system 
from time import sleep

def clearScreen():
    _ = system('cls')
    

def generateGoldenNumber(lowerBound, upperBound):
    return random.randint(lowerBound, upperBound)

def StartLevel(level, goldenNumber, score):
    clearScreen()
    lowerBound = 0
    upperBound = level + 10
    print(f"\t\t You are on level {level}")
    print(f"I am a number between {lowerBound} and {upperBound}")
    print("Can you tell me who am I ?", end=" ")
    guess = False
    tryCount = 0
    totalTryCount = int((level + 5)/2)
    while not guess:
        tryCount += 1
        playerGuess = int(input())
        if playerGuess == goldenNumber:
            guess = True
            score += (level + 10 - tryCount)
            print(f"Congratulations! You guessed it right")
            print(f"Your score is {score}")
            return False, score
        elif tryCount >= totalTryCount:
            return True, score
        else:
            lowerBound = int((goldenNumber + lowerBound)/2)
            upperBound = int((goldenNumber + upperBound)/2)
            print(f"Nope! you have {totalTryCount - tryCount} tries left. Try again")
            print(f"Here's another hint i am in range {lowerBound} to {upperBound}")  
                
                        

def StartGame():
    print("Hey! What should I call you ? ", end=" : ")
    playerName = input()
    score = 0
    level = 0
    gameOver = False
    while not gameOver:
        level += 1
        goldenNumber = generateGoldenNumber(0, level + 10)
        gameOver, score = StartLevel(level, goldenNumber, score)
        if not gameOver:
            print(f"Do you want to continue playing (y/n) ? ")
            choice = input()
            if choice == "y":
                gameOver = False
            else:
                gameOver = True
    print(f"{playerName} you have scored {score} points")
    sleep(5)

StartGame()

