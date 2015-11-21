#!/usr/bin/python
from __future__ import print_function
import random
HANGMANPICS = ['''

 L     
            
===>         |''', '''

 L  O  
            
======>      |''', '''

 L O S   
         
=======>     |''', '''

 L O S E   
        
=========>   |''', ''' 
    
 L O S E R
     
============ |'''] #Persona ahoracada.. fine pero lo cambiamos por esto que mola mas

words = 'rana caballo pato cebra leon tigue cocodrilo casa guapa sol luna'.split() #el split es como el %w es python, divide el array como si fuera ['rana','pato'] etc...



def getRandomWord(listapalabras):
  
  wordIndex = random.randint(0, len(listapalabras) - 1) #obtiene un indice random entre el tamano de la lista
  return listapalabras[wordIndex] #retorna una palabra dentro de la lista segun el indice



def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):

  print(HANGMANPICS[len(missedLetters)]) #segun el contador de letras falladas ensena una imagen u otra
  print()

  print('\nPalabras Falladas:\n\n', end=' ')
  for letter in missedLetters:
      print(letter, end=' ')    #simple imprimir las letras falladas por pantalla//
  print('\n')

  blanks = '_' * len(secretWord)  #creamos las barrabajas necesarias con el length de la palabra secreta obtenida

  for i in range(len(secretWord)): # replace remplazamos por la letra correspondiente
      if secretWord[i] in correctLetters:
          blanks = blanks[:i] + secretWord[i] + blanks[i+1:] 

  for letter in blanks: # las mostramos con un espacio al final
      print(letter, end=' ')
  print()

def getGuess(alreadyGuessed):
  #print ('Me llego esto ' + alreadyGuessed)
  # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
  while True:
      print('\n\nGuess a letter.')
      guess = str(raw_input())
      print ()
      guess = guess.lower()
      if len(guess) != 1:
          print('Por favor introduce una sola letra.')
      elif guess in alreadyGuessed:
          print('Ya has elegido esa letra, escoge otra.')
      elif guess not in 'abcdefghijklmnopqrstuvwxyz':
          print('Por favor introduce una letra.')
      else:
          return guess

def playAgain():
 # This function returns True if the player wants to play again, otherwise it returns False.
 print('Quieres jugar otra vez? (yes or no)')
 return str(raw_input()).lower().startswith('y')


print('\n\nH A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
#print ('secret word is' + secretWord)
gameIsDone = False

while True:
 displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

 # Let the player type in a letter.
 guess = getGuess(missedLetters + correctLetters)

 if guess in secretWord:
     correctLetters = correctLetters + guess

     # Check if the player has won
     foundAllLetters = True
     for i in range(len(secretWord)):
         if secretWord[i] not in correctLetters:
             foundAllLetters = False
             break
     if foundAllLetters:
         print('\nExactoo!! la palabra secreta es  "' + secretWord + '"! Ganasteeee!')
         gameIsDone = True
 else:
     missedLetters = missedLetters + guess

     # Check if player has guessed too many times and lost
     if len(missedLetters) == len(HANGMANPICS) - 1:
         displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
         print('\n\nTe has pasado de intentos!\nDespues de ' + str(len(missedLetters)) + ' intentos fallidos ' + str(len(correctLetters)) + ' de acertar, la palabra correcta era "' + secretWord + '"')
         gameIsDone = True

 # Ask the player if they want to play again (but only if the game is done).
 if gameIsDone:
     if playAgain():
         missedLetters = ''
         correctLetters = ''
         gameIsDone = False
         secretWord = getRandomWord(words)
     else:
         break
         