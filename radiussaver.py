def read(Tfile):
	f = open(Tfile, 'r')
	k = f.readline()
	f.seek(0)
	j = float(k)

	return j 

def save(Tfile , radius):
	f = open(Tfile , 'w')
	f.write(str(radius))
	f.close()