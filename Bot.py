import nltk	
nltk.download('words')
import spacy
import Token
from sapling import SaplingClient
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from PIL import ImageTk
import PIL.Image
import tkinter as tk
from tkinter import *
import os

Mode = False



def Launch():
	global Mode
	Words = Answer.get(1.0, tk.END+"-1c")

	MoreWords = word_tokenize(Words)
	MW = nltk.pos_tag(MoreWords)

	# print(MW)
	# add using append() so that it keeps going you put the stuff
	# in the parenthisis
	ideaBlock = []
	Subject = None
	found = False
	VerbSec = False
	ObjRed = False
	VerbID = -1
	ObjID = -1
	ShortVerb = None
	# print(MW)
	OneScentenceMode = Mode
	print(OneScentenceMode)
	for i in range(len(MW)):

		if('NNP' in MW[i] and found==False):
			Subject = MoreWords[i]
			if(i+1<len(MW) and 'NNP' in MW[i+1]):
				Wee = Subject +" "+MoreWords[i+1]
				Subject = Wee
			found = True

		if(OneScentenceMode==False):
			if(('VBN' in MW[i] or 'VBZ' in MW[i] or 'VB' in MW[i] or 'VBD' in MW[i]) and VerbSec == False):
				# print("happeing")
				VerbSec = True;
				ObjRed = True
				VerbID = i
				# print(MoreWords[verbID])
				# print(verbID)
			if((('NNP' in MW[i]) or ('NN' in MW[i])) and ObjRed and found == True):
				VerbSec = False
				num = i-VerbID+1
				subBlock = []
				j = VerbID
				while(j<VerbID+num):
					subBlock.append(MoreWords[j])
					j = j+1
				ideaBlock.append(subBlock)
				ObjRed = False
				VerbSec = False;
		else:

			if(('VBN' in MW[i] or 'VBZ' in MW[i] or 'VB' in MW[i] or 'VBD' in MW[i]) and VerbSec == False):
				VerbSec = True;
				ObjRed = True
				ShortVerb = MoreWords[i]
				while(i+1<len(MW) and ('VBN' in MW[i+1] or 'VBZ' in MW[i+1] or 'VB' in MW[i+1] or 'VBD' in MW[i+1]) and VerbSec == False):
					VerbSec = True;
					ObjRed = True
					ShortVerb = ShortVerb+" "+MoreWords[i+1]
					i = i+1
			if((('NNP' in MW[i]) or ('NN' in MW[i])) and ObjRed and found == True):
				VerbSec = False
				subBlock = []
				j = VerbID
				subBlock.append(ShortVerb)
				subBlock.append(MoreWords[i])
				ideaBlock.append(subBlock)
				ObjRed = False
				VerbSec = False;

	BadGrammar = Subject;

	for x in range(len(ideaBlock)):
		for y in range(len(ideaBlock[x])):
			BadGrammar = BadGrammar +" "+ideaBlock[x][y]
		BadGrammar = BadGrammar+","

	# The Justice Department has joined the Pentagon in an urgent effort to determine how secret military documents on the war in Ukraine made their way onto multiple social media sites.


	# API_KEY = '9S7GNI3SBVYMOZYSRVX4WEVX4UHOD3GN'
	# client = SaplingClient(api_key=API_KEY)
	# edits = client.edits(BadGrammar, session_id='old_session')
	# nullList = []
	# backUp = True;
	# while((edits!= nullList) and backUp):
	# 	edits = client.edits(BadGrammar, session_id='old_session')
	# 	start = int(edits[0]['start'])
	# 	end = int(edits[0]['end'])
	# 	rep = edits[0]['replacement']
	# 	leftScentence = BadGrammar[0:start]
	# 	RightScentence = BadGrammar[end: len(BadGrammar)-1]
	# 	BadGrammar = leftScentence + rep + RightScentence
	# 	print("")
	# 	print(BadGrammar)
	# 	if(edits!= nullList):
	# 		backUp = False

	print("=======SUMMARY=======")
	print(BadGrammar)
	Answer2.delete(1.0, "end")
	Answer2.insert("end", BadGrammar)








def ChangeMode():
		global root
		global good
		global Mode
		global panel
		global panel2
		if(Mode==False):
			Mode = True
			good = Label(root, text="bD;Dr")
			good.grid(row=2,column=2)
			root['background']='#000000'
			panel['background'] = '#000000'
			panel2.grid(row = 1, column =0, pady=0)	
			panel2.pack_forget()


		else:
			Mode = False
			panel.grid(row = 1, column =0, pady=0)	
			good = Label(root, text="tl;Dr")
			good.grid(row=2,column=2)
			panel['background'] = "#2e5182"

			root['background']='#2e5182'

#python Desktop\Bot.py

#u can take the latest verb, put commas between everything, and 
# just grammaticly check everything
# this looks pretty goo though. And put an and at the aend. This looks
# solid, I'll have to test it a couple more time though, that all. 
# you'll get to rest soon, dont worry man.


# you need to find a way to cut out some details and
# squeeze it down to the important detials
# its like that thingpython Desktop\Bot.py you do when you describe to a child
# you keep the language simple and easy to understand
#Consistentlyy Wrong
# what if you get the subject, verb, noun, a few other things
# and then make them gramaticly correct?
# you put them together of course, subject verb object
# gonna kill the OG mean lol but Its worth a shot i guess

# i dont really think that this is possilbe honestly. I'd rather
# fail trying to make an awsome project than sumbit a bad
# /boring on and lose anyways. 
# If I asked chatGPT to summerize text for me, I'd still 
# think its kinda insane if it did it propperly
# just try to make something that works to a 50% degree
# something that barley works. Thats it.







# look for chunks of words that mean other words
# declare the goal of a chuck of words is and change it
# just make the engine bro, thats it. If I do that
# Ill be able to put the 3 month AI langauge calling
# to a end. You give the engine a chunk of words and 
# it tells you what the goal of those words are
#Machine Learning? yes! Do I know how to do that?
# No! but hey, thats alright!

#I'll give it like 100 words to pick from, a basic huerstic algo
# from there I'll reward it for making good guesses and 
# punish it for bad guesses

#one verb, one noun, 50 each, or 80 /20


#There have to be a finite number of factors that make one
# word being more likely than another


# question morality
# Prove innocence

# if the words are more uncertain it's question, and
# if it has a question mark it'd most likely be that

#prove would be harder words

#ML requires us to feed data to the machine, but also give it
# an algorithim so that it can become more accurate
# in the future
# What if each scentence I throw at the machine will have
# the word's rankings declared manually by me. It'll have
# 5 spectrums and those spectrums are going to be
# altered if my bot comes up with wierd answers.


#Ill feed data by giving it a giant array of scentences
#Certain wordws will already be defined on five criteria
# but unseen words will be define on the two words surrounding
# if it isn't contained
# Ill turn each of the scentences into arrays with the nlmk
# thing
# The word will then be stored in a hash map, which the 
# ML can access anytime it wants. It'll use the word as a key
# and the stats will be in the objects that come after
# from there.
# Before I code I'm going to run through this idea
# with a few tests




#I think if you had alot of these, like 20, and you
# stacked them ontop of one another, then I think you could
# a close to reality description in two words


#1: Formality
#2: Identification
#3: Agression
#4: Sympathy
#5: Passiveness (usually) 
#6: Retrospectiveness
#7: technological
#8: Money related
#9: Compliment
#10: Neutrality
#11: Joy
#12: Seriousness ( words like so very, extremity)
#13: Explanatory






root= tk.Tk()
root.geometry("1000x500")

root['background']='#2e5182'

Answer = Text(root, height = 7, width = 80)
Answer2 = Text(root, height = 7, width = 80)

img = PIL.Image.open("C:\\Users\\froze\\Desktop\\Tl;dr\\BlueDer.jpg")
Background = img.resize((500,250), PIL.Image.ANTIALIAS)
miga = ImageTk.PhotoImage(Background)
panel = Label(root, i = miga)
panel['background']='#2e5182'
panel.grid(row = 1, column =0, pady=0)

Answer.grid(row = 0, column =0, pady=0)
Answer2.grid(row = 2, column =0, pady=0)
Launch = Button(root, text="Launch", command=Launch)
ChangeMode = Button(root, text="ChangeMode", command=ChangeMode)
Launch.grid(row=0,column=2)
ChangeMode.grid(row=1,column=2)
good = Label(root, text="Tl;Dr")
good.grid(row=2,column=2)


img2 = PIL.Image.open("C:\\Users\\froze\\Desktop\\Tl;dr\\RedDer.png")
Background2 = img2.resize((500,250), PIL.Image.ANTIALIAS)
miga2 = ImageTk.PhotoImage(Background)
panel2 = Label(root, i = miga2)
panel2['background']='#8c0f0f'


root.mainloop()