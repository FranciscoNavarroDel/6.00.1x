# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    lista=list(secretWord)
    Dict={}
    for agregar in lista:
        Dict[agregar]=0
    for borrar in lettersGuessed:
        if borrar in Dict:
            del Dict[borrar]
    if len(Dict)==0:
        acertaste=True
    else:
        acertaste=False
    return acertaste

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    Palabra=[]
    for agregar in range(len(secretWord)):
        Palabra.append("_ ")
    for Mostrar in lettersGuessed:
        i=0
        for unir in secretWord:
            if Mostrar==unir:
                Palabra[i]=Mostrar
            i=i+1
    Letras=" ".join(Palabra)
    return Letras

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    Todaslasletras=list(string.ascii_lowercase)
    for i in lettersGuessed:
        Todaslasletras.remove(i)
    Letrasavalibles="".join(Todaslasletras)
    return Letrasavalibles
    
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman")
    print("I am thinking of a word that is",len(secretWord),"letters long")
    print("-------------")
    acertaste=False
    oportunidades=8
    lettersGuessed=[]
    palabrabuscada=getGuessedWord(secretWord, lettersGuessed)
    while acertaste==False:
        print("You have",oportunidades,"guesses left")
        Letras=getAvailableLetters(lettersGuessed)
        print("Available Letters:",Letras)
        entrada=input("Please guess a letter:")
        pedirletra=entrada.lower()
        if pedirletra in lettersGuessed:
            print("Oops! You've already guessed that letter:",getGuessedWord(secretWord, lettersGuessed))
            print("-----------")
        else:
            lettersGuessed.append(pedirletra)
            if palabrabuscada!=getGuessedWord(secretWord, lettersGuessed):
                palabrabuscada=getGuessedWord(secretWord, lettersGuessed)
                print("Good guess:",palabrabuscada)
                print("-----------")
            else:
                print("Oops! That letter is not in my word:",palabrabuscada)
                print("-----------")
                oportunidades=oportunidades-1
        acertaste=isWordGuessed(secretWord, lettersGuessed)
        if oportunidades==0:
            break
    if isWordGuessed(secretWord, lettersGuessed)==True:
        print("Congratulations, you won!")
    elif isWordGuessed(secretWord, lettersGuessed)==False:
        print("Sorry, you ran out of guesses. The word was",secretWord)

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
