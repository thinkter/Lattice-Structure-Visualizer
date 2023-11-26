import csvoutput as c

#print(c.a)
p = c.a
v = []
e = []
f = []
_pos = []


k = len(p)
for i in range (0,8):
    v.append(p[i])
    _pos.append(p[i])
for i in range (8 , 20):
    e.append(p[i])
for i in range (20,26):
    f.append(p[i])
    _pos.append(p[i])


vert = tuple(v)
edge = tuple(e)
face = tuple(f)

pos = tuple(_pos)
print(vert)
print(edge)
print(face)
#radius = p[28]

print(pos)


