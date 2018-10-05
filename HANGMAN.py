# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 14:08:31 2018

@author: Daniel
"""
import random
playing = True
#%%
def choose_word():
        with open('SOWPODS.txt') as myfile:
            words = []
            for line in myfile:
                words.append(line)
            word = random.choice(words)
            return word[0:-2].lower()

class Word:
    
    def __init__(self, word):
        self.word = word
        self.letters = list(self.word)
        self.count = len(set(self.letters))
    
#%%
class Letters:
    
    def __init__(self):
        self.active_letters = ['a','b','c','d','e','f','g','h','i','j','k','l',
                               'm','n','o','p','q','r','s','t','u','v','w','x',
                               'y','z']
        self.guessed_letters = []
        self.correct_letters = []
    
    def __str__(self):
        print('you have guessed the following letters: ')
        for letter in self.guessed_letters:
            print(letter)
            
    def remove_letter(self, letter):
        for i in self.active_letters:
            if i == letter:
                self.active_letters.remove(i)
        self.guessed_letters.append(letter)

#%%
    
class Hanged_Man:
    
    def __init__(self):
        self.count = 0
    
    def __str__(self):
        if self.count == 0:
            print('0000000000000\n0           0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0')
        elif self.count == 1:
            print('0000000000000\n0           0\n0           1 \n0          1 1\n0           1 \n0\n0\n0\n0\n0\n0\n0\n0\n0')
        elif self.count == 2:
            print('0000000000000\n0           0\n0           1 \n0          1 1\n0           1 \n0           2 \n0           2 \n0           2 \n0\n0\n0\n0\n0\n0')
        elif self.count == 3:
            print('0000000000000\n0           0\n0           1 \n0          1 1\n0           1 \n0          32 \n0         3 2 \n0        3  2   \n0\n0\n0\n0\n0\n0')
        elif self.count == 4:
            print('0000000000000\n0           0\n0           1 \n0          1 1\n0           1 \n0          324\n0         3 2 4\n0        3  2  4\n0\n0\n0\n0\n0\n0')
        elif self.count == 5:
            print('0000000000000\n0           0\n0           1 \n0          1 1\n0           1 \n0          324\n0         3 2 4\n0        3  2  4\n0          5  \n0         5    \n0        5      \n0       5        \n0\n0')
        elif self.count == 6:
            print('0000000000000\n0           0\n0           1 \n0          1 1\n0           1 \n0          324\n0         3 2 4\n0        3  2  4\n0          5 6\n0         5   6\n0        5     6\n0       5       6\n0\n0')

#%%

def win_check(word, alphabet, hangman):
    
    global playing
    
    if hangman.count == 6:
        print('lol you lost')
        print(f'the word was {word.word}')
        playing = False
    elif hangman.count < 6 and word.count == len(alphabet.correct_letters):
        print('lol you won')
        print(f'the word was {word.word}')
        playing = False

#%%
        
def player_guess(alphabet):
    
    while True:
        guess = input('please select a letter: ')
        if guess.lower() not in alphabet.active_letters:
            print('you cannot select the same letter more than once')
            continue
        else:
            print(f'you selected the letter {guess}')
            return guess.lower()
            break

#%%

def show_word(word, alphabet):
        revealed_word = ''
        for i in word.letters:
            if i in alphabet.guessed_letters:
                revealed_word += i + ' '
            else:
                revealed_word += '_ '
        print(revealed_word)

#%%
                
def letter_check(word, alphabet, hanged_man, letter):
    
    if letter not in word.letters:
        hanged_man.count += 1
        alphabet.remove_letter(letter)
        
    else:
        alphabet.remove_letter(letter)
        alphabet.correct_letters.append(letter)

#%%

hidden_word = Word(choose_word())

alphabet = Letters()
hangman = Hanged_Man()

print('welcome to hangman')

#%%

while playing == True:
    
    hangman.__str__()
    show_word(hidden_word, alphabet)
    alphabet.__str__()
    letter_check(hidden_word, alphabet, hangman, player_guess(alphabet))
    win_check(hidden_word, alphabet, hangman)
    
#%%    