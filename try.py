class dog():
	def talk(self):
		print("woof")
	def walk(self):
		print("dog walks")
 
class duck():
	def talk(self):
		print("ducks")
	def walk(self):
		print("move")

def speak(thing):
	thing.talk()
def move(thing):
	thing.walk()

myduck = duck()
move(myduck)

mydog= dog()
speak(mydog)

import this


