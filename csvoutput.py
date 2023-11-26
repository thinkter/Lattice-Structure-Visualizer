import csv

_A = []
with open('data.csv', 'r') as csvfile:
	# Create a CSV reader object
    reader = csv.reader(csvfile)


    for row in reader:
    	k =[]
    	for i in row:
    		l = int(i)
    		k.append(l)
    	f = tuple(k)	
    	_A.append(f)

a = tuple(_A)

v = []
e = []
f = []
_pos = []


k = len(a)
for i in range (0,8):
    v.append(a[i])
    _pos.append(a[i])
for i in range (8 , 20):
    e.append(a[i])
for i in range (20,27):
    f.append(a[i])
    _pos.append(a[i])


vert = tuple(v)
edge = tuple(e)
face = tuple(f)

pos = tuple(_pos)
#print(vert)
#print(edge)
#print(face)
#radius = p[28]

#print(pos)



