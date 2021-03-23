# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 12:57:09 2019

@author: frani
"""

def getGuessedWord(secretWord, lettersGuessed):
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
#
def isWordGuessed(secretWord, lettersGuessed):
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

def getAvailableLetters(lettersGuessed):
    import string
    Todaslasletras=list(string.ascii_lowercase)
    for i in lettersGuessed:
        Todaslasletras.remove(i)
    salida="".join(Todaslasletras)
    return salida

secretWord="hola"
print("Welcome to the game, Hangman")
print("I am thinking of a word that is",len(secretWord),"letters long")
print("-------------")
acertaste=False
oportunidades=8
lettersGuessed=[]
palabrabuscada=getGuessedWord(secretWord, lettersGuessed)
while acertaste==False:
    print("You have",oportunidades,"guesses left.")
    Letras=getAvailableLetters(lettersGuessed)
    print("Available letters:",Letras)
    entrada=input("Please guess a letter:")
    pedirletra=entrada.lower()
    if pedirletra in lettersGuessed:
        print("Oops! You've already guessed that letter:",getGuessedWord(secretWord, lettersGuessed))
    else:
        lettersGuessed.append(pedirletra)
        if palabrabuscada!=getGuessedWord(secretWord, lettersGuessed):
            palabrabuscada=getGuessedWord(secretWord, lettersGuessed)
            print("Good guess:",palabrabuscada)

        else:
            print("Oops! That letter is not in my word:",palabrabuscada)
            oportunidades=oportunidades-1
    acertaste=isWordGuessed(secretWord, lettersGuessed)
    if oportunidades==0:
        break
if isWordGuessed(secretWord, lettersGuessed)==True:
    print("Congratulations, you won!")
elif isWordGuessed(secretWord, lettersGuessed)==False:
    print("Sorry, you ran out of guesses. The word was",secretWord)