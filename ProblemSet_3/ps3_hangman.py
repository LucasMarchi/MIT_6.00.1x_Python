# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

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
    ans = False
    
    for letter in secretWord:
        if letter in lettersGuessed:          
            ans = True
        else:
            return False

    return ans

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    ans = ''
    
    for letter in secretWord:
        if letter in lettersGuessed:          
            ans += letter + ' '
        else:
            ans += '_ '

    return ans



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    ans = ''
    
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            ans += letter
    
    return ans

def hangman(secretWord):

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    print('-------------')

    guessesLeft = 8 
    lettersGuessed = []            

    while guessesLeft > 0 :
        if isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!')
            break
        else:
            print('You have ' + str(guessesLeft) + ' guesses left.')
            print('Available Letters: ' + getAvailableLetters(lettersGuessed))
            guess = input('Please guess a letter: ')
            guess = guess.lower()

            if guess in lettersGuessed:
                print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            elif guess in secretWord:
                lettersGuessed.append(guess)
                print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
            else:
                lettersGuessed.append(guess)
                print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
                guessesLeft -= 1

            print('------------')

    if guessesLeft == 0 :
        print('Sorry, you ran out of guesses. The word was '+secretWord+'.') 

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
