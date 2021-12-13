def fold(data,axis,n):
	if axis=="x":
		return list(set([tuple([2*n-i[0],i[1]]) if i[0]>n else tuple(i) for i in data[:902]]))
	else:
		return list(set([tuple([i[0],2*n-i[1]]) if i[1]>n else tuple(i) for i in data[:902]]))

data = open("input","r").readlines()
points = [tuple([int(j) for j in i.strip().split(",")]) for i in data[:902]]
instructions = [i.replace("fold along","").strip().split("=") for i in data[903:]]
print(instructions)
for i in instructions:
	print(i)
	newpoints = fold(points,i[0],int(i[1]))
	points=newpoints
import numpy as np
import matplotlib.pyplot as plt
coords = np.array([list(i) for i in points])
mat=np.zeros((100,100))
for i in coords:
	mat[i[0],i[1]] = 1

plt.imshow(mat[:50,:50])
plt.show()