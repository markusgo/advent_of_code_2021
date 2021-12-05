import numpy as np
data = [i.strip().replace("->","").replace(","," ").split() for i in open("input","r") ]
maxx=0
maxy=0
for i in range(len(data)):
	for j in range(len(data[i])):
		data[i][j] = int(data[i][j])
	if max((data[i][0],data[i][2]))>maxx:
		maxx = max((data[i][0],data[i][2]))
	if max((data[i][1],data[i][3]))>maxy:
		maxy = max((data[i][1],data[i][3]))
print(maxx,maxy)
crosses = np.zeros((maxx+1,maxy+1))
for i in data:
	start = i[0:2]
	end = i[2:4]
	vec=[0,0]
	if start[0]>end[0]:
		vec[0] = -1
	elif start[0]<end[0]:
		vec[0] = 1
	else:
		vec[0] = 0

	if start[1]>end[1]:
		vec[1] = -1
	elif start[1]<end[1]:
		vec[1] = 1
	else:
		vec[1] = 0
	sent=1
	while sent:
		if start[0]==end[0] and start[1]==end[1]:
			sent=0
		crosses[start[0],start[1]]+=1
		start[0]+=vec[0]
		start[1]+=vec[1]

print(np.sum(np.where(crosses>=2,1,0)))