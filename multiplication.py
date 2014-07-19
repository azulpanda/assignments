for i in range(1,10):
	line = []
	for j in range(2,10):
		line.append(str(j)+"*"+str(i)+"="+str(i*j))
	print "\t".join(line)