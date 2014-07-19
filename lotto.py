import random

box = range(1,46)
lotto = []

for i in range(6):
	num = random.randint(0,44-i)
	lotto.append(box.pop(num))

lotto.sort()
print lotto
