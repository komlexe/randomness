#i will not use this program on any ide only sublime text is good because that program looks ugly on any ide

import pyttsx3 #pip install pyttsx3
import random
import os
import sys
import requests
from random_word import RandomWords

r = RandomWords()

#just somthing cool
print('''                           .___                                          
 ____________    ____    __| _/____   _____   ____   ____   ______ ______
 \_  __ \__  \  /    \  / __ |/  _ \ /     \ /    \_/ __ \ /  ___//  ___/
  |  | \// __ \|   |  \/ /_/ (  <_> )  Y Y  \   |  \  ___/ \___ \ \___ \ 
  |__|  (____  /___|  /\____ |\____/|__|_|  /___|  /\___  >____  >____  >
             \/     \/      \/            \/     \/     \/     \/     \/ v1.0 ''')

#the name engine does not have to be engine 
engine = pyttsx3.init()
voices = engine.getProperty('voices')


#the voise index is 1 you can make it 0 if you want voice of a terminator
engine.setProperty('voice', voices[1].id)

#som fancy stuff
def onStart(name):
   print ('starting', name)
   
def onWord(name, location, length):
   print ('word', name, location, length)
   
def onEnd(name, completed):
   print ('finishing', name, completed)
   
engine = pyttsx3.init()
engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)

#it just the speed, you can change the speed with those numbers
engine.setProperty('rate', 125)


#it's not necessary it just a test to the voice
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()


#the name does not have to be speak it's just abviose
def speak(audio):
    engine.say(audio)
    engine.runAndWait()



class jake:
   def __init__(self, error, where_error):
      self.e = error
      self.we = where_error

   def __str__(self):
      print('the error is %s' % self.e)
      return 'the error in the %s' % self.we

   def __repr__(self):
      return 'print this when you got som thing wrong'

def main():
      
   #an empty list that what ever word you save in a file is what you are going to append on it
   a = []


   #just to make the program running with out having to run it every single time
   while True:

       #to get anything from the user
       inp = (input('input sumthing: '))


       #here to append the list from the user to the list
       a.append(inp)


   #to get what the user want
       inp2 = (input('''do you want to speak it(1) or save it(2)
               or do want to play a guessing game(3)
               or di you want to get a random ward(4): '''))


   #here
       if inp2 == '1':
           inp5 = (input('do you want to speak all the list(1) or just the that word(2):'))

           if inp5 == '1':
               speak(a)
               
           elif inp5 == '2':
               speak(inp)
           
       elif inp2 == '2':
           inp3 = (input('whay is the file name: '))

           ope = open(inp3, 'w')
           ope.write(inp)
           ope.close()

       elif inp2 == '3':
           
           #that's why i imported random
           WORDS = ("python", "jumble", "easy", "difficult", "answer",  "xylophone")
           word = random.choice(WORDS)
           correct = word
           jumble = ""
           while word:
               
               position = random.randrange(len(word))
               jumble += word[position]
               word = word[:position] + word[(position + 1):]
               
           print(
           """
                  make a word.
                 (press the enter key at to quit)
                 """
                 )
           print("The word is:", jumble)
           guess = input("what nyou think it is: ")
           while guess != correct and guess != "":
               print("Sorry, that's not it")
               guess = input("Your guess: ")
           if guess == correct:
               print("That's it, you guessed it!\n")
           print("Thanks for guessing")
           

       elif inp2 == '4':
           inp4 = (input('''a single random word(1) or list of Random words(2) \n
                  or Word of the day(3)'''))

           # Return a single random word
           t = r.get_random_word()
           # Return list of Random words
           g = r.get_random_words()
           # Return Word of the day
           h = r.word_of_the_day()

           if inp4 == '1':
              print(t)
           elif inp4 == '2':
              print(g)
           elif inp4 == '3':
              print(h)

main()


