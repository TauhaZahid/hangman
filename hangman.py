import random
import os

def clr():
    if os.name == 'nt':
        os.system('cls')

Hangman_Figure= [
    "__________\n"
    "     |    \n"
    "     O    \n"
    "          \n"
    "          \n"
    "          \n",
    "__________\n"
    "     |    \n"
    "     O    \n"
    "     |    \n"
    "     |    \n"
    "          \n",
    "__________\n"
    "     |    \n"
    "     O    \n"
    "   / |    \n"
    "     |    \n"
    "          \n",
    "__________\n"
    "     |    \n"
    "     O    \n"
    "   / | \\  \n"
    "     |    \n"
    "          \n",
    "__________\n"
    "     |    \n"
    "     O    \n"
    "   / | \\  \n"
    "     |    \n"
    "    /     \n",
    "__________\n"
    "     |    \n"
    "     O    \n"
    "   / | \\  \n"
    "     |    \n"
    "    / \\   \n"
]

Hangman_Words=[
    "This",
    "is",
    "Hangman",
    "Game",
    "Code",
]

while True:
    Play_Word=random.choice(Hangman_Words).upper()
    Guess=["-" for i in Play_Word]
    Guessed_Word=[]
    Mistake=0
    clr()
    Game=input("Welcome to Hangman Game! Enter Any Key to start or Q to Quit: ").upper()
    if Game == 'Q':
        break

    while True:
        clr()
        if Mistake < len(Hangman_Figure):
            print(Hangman_Figure[Mistake])
            print("Guessed Letters",Guessed_Word)
            print(" ".join(Guess))
            Player_Guess_Word=input("Enter Guessed Letter: ").upper()

            if len(Player_Guess_Word) > 1 or not Player_Guess_Word.isalpha():
                print("Please Input Only one letter: ")
                continue

            if Player_Guess_Word in Guessed_Word:
                print("You already guessed this word")
                input("Press Enter to continue...")
                continue
            
            GuessFlag=False
            for i in range(len(Play_Word)):
                if Player_Guess_Word ==Play_Word[i]:
                    Guess[i]=Player_Guess_Word
                    GuessFlag=True
            Guessed_Word.append(Player_Guess_Word)
            if GuessFlag is False:
                Mistake+=1
                print("Incorrect Guess,Try again")       
                input("Press Enter to continue...")        
        else:
            clr()
            print("You Lost")
            print("The word was: ",Play_Word)
            input("Press Enter to continue...")  
            break 
        if "".join(Guess)==Play_Word:
            clr()
            print("You Won")
            print("The word was: ",Play_Word)
            input("Press Enter to continue...")  
            break