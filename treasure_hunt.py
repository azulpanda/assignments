with file("treasure_map.txt", "r") as text:
	message_1 = ""
	for line in text:
		this_line = ""
		for c in line:
			if c.isdigit():
				this_line += c
		message_1 += line[int(this_line)]
	print message_1


with file("treasure_map.txt", "r") as text:
	message_2 = ""
	split = text.read().split("!@#$%")
	for i in range(len(split)-1):
		message_2 += split[i+1][0]
	print message_2