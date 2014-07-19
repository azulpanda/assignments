#-*- coding:UTF-8 -*-
import random

def win(str):
	print "컴퓨터는 "+str+"를 냈다!"
	print
	print "니가 이겼다."
	print

def draw(str):
	print "컴퓨터는 "+str+"를 냈다!"
	print
	print "승부가 나지 않았다..."
	print

def lose(str):
	print "컴퓨터는 "+str+"를 냈다!"
	print
	print "컴퓨터가 승리했다!"
	print

cont=True

while cont:
	me = 0
	com = random.randint(1,3)
	value = raw_input("가위 바위 보!:")
	ask = False
	if value == "가위":
		if com==1:
			draw("가위")
		elif com==2:
			lose("바위")
		else:
			win("보")
		ask = True
	elif value == "바위":
		if com==1:
			win("가위")
		elif com==2:
			draw("바위")
		else:
			lose("보")
		ask = True
	elif value == "보":
		if com==1:
			lose("가위")
		elif com==2:
			win("바위")
		else:
			draw("보")
		ask = True
	else:
		print
		print "가위, 바위, 보 중 하나를 입력하세요"
		print
	while ask:
		print
		next = raw_input("한판 더?(예/아니오):")
		if next == "예":
			print
			break
		elif next == "아니오":
			print
			print "포기한 너는 루저"
			cont = False
			break
		else: 
			print
			print "예, 아니오 중 하나를 입력하세요"