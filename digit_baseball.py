#-*- coding:UTF-8 -*-
import os
from random import randint

def check_num(number):
	a = number[0]
	b = number[1]
	c = number[2]
	d = number[3]
	return not (a==b or a==c or a==d or b==c or b==d or c==d)

def get_num():
	num = 0
	while True:
		mid = randint(1000,9999)
		if check_num(str(mid)):
			num = mid
			break
	return num

def compare(x, y):
	strike = 0
	ball = 0
	for i in range(len(x)):
		if x[i] in y:
			if i == y.index(x[i]):
				strike+=1
			else:
				ball+=1
	return [strike, ball]

log = []
game = 0
log.extend(["Game Start!", "", ""])
print "Game Start!"
print

while True:
	game+=1
	print
	print "Game", game
	print
	guess = 0
	com = str(get_num())
	print com
	log.extend(["Game %d" % game, "", "Answer: "+com, ""])
	while True:
		guess += 1
		while True:
			player = raw_input("Guess %d - Insert a 4 digit number (all digits must be different):" % guess)
			if player.isdigit():
				if int(player)>=1000 and int(player)<=9999:
					if check_num(player):
						break
					else:
						print "I said, all digits must be different"
				else:
					print "I said, insert a 4 digit number"
			else: 
				print "I said, insert a number"
		log.extend(["Guess #%s: %s" % (guess, player)])
		score = compare(com, player)
		if score[0]==4:
			log.extend(["", "You hit the number!", "You guessed %d times!" % guess, ""])
			print
			print "You hit the number!"
			print "You guessed %d times!" % guess
			print
			break
		else:
			log.extend(["Result: %dS %dB" % (score[0], score[1]), ""])
			print "%dS %dB" % (score[0], score[1])
			print
	log.extend([""])
	while True:
		cont = raw_input("New Game? (yes/no):")
		if cont.lower()=="yes" or cont.lower()=="no":
			break
		else:
			print "Insert 'yes' or 'no':"
	if cont.lower()=="no":
		break

while True:
	export = raw_input("Do you want to export your game log? (yes/no):")
	if export.lower()=="yes" or export.lower()=="no":
		break
	else:
		print "Insert 'yes' or 'no':"

log.extend(["", "Game Over!"])
print 
print "Game Over!"

if export.lower()=="yes":
	if not os.path.exists("game_log"):
   		os.makedirs("game_log")
	with open("game_log/baseball_log.txt", "w") as text:
		for i in range(len(log)):
			text.write(log[i]+"\n")
