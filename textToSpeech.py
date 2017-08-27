# Python Program - TEXT-TO-SPEECH Converter
# ***INTERNET CONNECTION IS COMPULSORY

from gtts import gTTS
import os
from string import capwords
language = 'en'
filename = input("Enter your name: ")
input("Hey there! "+capwords(filename)+"\nWelcome to TEXT-TO-SPEECH Converter\nPress any key to continue...")
mytext = input("\nEnter text here => ")

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save(filename+'.mp3')
