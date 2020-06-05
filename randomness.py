import pyttsx3 
import random
import os
import datetime
import sys
from random_word import RandomWords

r = RandomWords()

#just somthing cool
print('''


                            
                            
           _____                   ____          
          /\    \                 /:\   \         
         /::\    \               /:::\   \        
        /::::\    \             /:::::|   |        
       /::::::\    \           /::::::|   |        
      /:::/\:::\    \         /:::::::|   |
     /:::/__\:::\    \       /::::/|::|   |        
     \:::\   \:::\    \     /::::/ |::|   |        
 __ __\:::\   \:::\    \   /::::/  |::|___|______  
/::\   \:::\   \:::\    \ /::::/   |::::::::\    \

\:::\   \:::\   \__/____/ \___/___/    /::::/    / 
 \:::\   \:::\    \                   /::::/    /  
  \:::\   \:::\____\                 /::::/    /
   \:::\  /:::/    /                /::::/    /    
    \:::\/:::/    /                /::::/    /       
     \::::::/    /                /::::/    /       
      \::::/    /                 \:::/    /        
       \__/____/                   \_/____/ v1.2 \n \n \n \n \n \n''')

#the name engine does not have to be engine 
engine = pyttsx3.init()
voices = engine.getProperty('voices')


#the voise index is 1 you can make it 0 if you want voice of a terminator
engine.setProperty('voice', voices[1].id)

#som fancy stuff
name = 'SM'

def onStart(name):
   print ('starting SM')
   
def onWord(name, location, length):
   print ('word', 'SM', location, length)
   
def onEnd(name, completed):
   print ('finishing', 'SM', completed)
   
engine = pyttsx3.init()
engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)

#it just the speed, you can change the speed with those numbers
engine.setProperty('rate', 140)

#the volume
engine.setProperty('volume', 0.8)


#it's not necessary it just a test to the voice
sir = (input('what is your name: '))

engine.say('welcom to Randomness' + sir)
engine.runAndWait()


#the name does not have to be speak it's just abviose
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!" + sir)

    elif hour>=12 and hour<18:
        speak("Good Afternoon!" + sir)   

    else:
        speak("Good Evening!" + sir)

    speak("I am SM %s. Mister komplex made me i will try to make you conftebal" % sir)

greet()

def main():
      
   #an empty list that what ever word you save in a file is what you are going to append on it
   a = []


   #just to make the program running with out having to run it every single time
   while True:

       #to get anything from the user
       speak('input sumthing')
       inp = (input('input sumthing: '))


       #here to append the list from the user to the list
       a.append(inp)


   #to get what the user want
       speak('''do you want to speak it press 1, or save it press 2,
        or do you want to play a guessing game press 3,
        or do you want to get a random word press 4 ''')
       inp2 = (input('''do you want to speak it(1) or save it(2)
               or do want to play a guessing game(3)
               or di you want to get a random ward(4): '''))


   #here
       if inp2 == '1':
           speak('do you want to speak all the list press 1 or just the that word press 2')
           inp5 = (input('do you want to speak all the list(1) or just the that word(2):'))
           
           
           
           if inp5 == '1':
               speak(a)
               
           elif inp5 == '2':
               speak(inp)
           
       elif inp2 == '2':
           speak('what is the file name: ')
           inp3 = (input('what is the file name: '))

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

           speak("""
                  make a word.
                 (press the enter key at to quit)
                 """)
           print(
           """
                  make a word.
                 (press the enter key at to quit)
                 """
                 )
           
           
           print("The word is:", jumble)
           guess = input("what you think it is: ")
           while guess != correct and guess != "":

               speak("Sorry, that's not it")              
               print("Sorry, that's not it")

               speak("what you think it is: ")
               guess = input("what you think it is: ")

               
           if guess == correct:

               speak("That's it, you guessed it!")
               print("That's it, you guessed it!\n")

           speak("Thanks for guessing")
           print("Thanks for guessing")

       elif inp2 == '4':
           speak('''a single random word press 1 or list of Random words press 2
                  or Word of the day press 3''')
           
           inp4 = (input('''a single random word(1) or list of Random words(2)
                  or Word of the day(3)'''))

           

           # Return a single random word
           t = r.get_random_word()
           
           # Return list of Random words
           g = r.get_random_words()
           
           # Return Word of the day
           h = r.word_of_the_day()

           if inp4 == '1':
              print(t)
              speak(t)
              
           elif inp4 == '2':
              print(g)
              speak(g)
              
           elif inp4 == '3':
              print(h)
              speak(h)

main()





prnt
