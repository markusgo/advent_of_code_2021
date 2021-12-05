import numpy as np
data = np.array([[int(j) for j in (i.strip().replace("->","").replace(","," ").split())] for i in open("input","r")])
maxx = np.max([np.max(data[:,0]),np.max(data[:,2])])
maxy = np.max([np.max(data[:,1]),np.max(data[:,2])])
print(maxx,maxy)
crosses = np.zeros((maxx+1,maxy+1))
for i in data:
	start = np.array(i[0:2])
	end = np.array(i[2:4])
	vec=np.sign(end-start)
	
	#Comment out for Part 2
	if np.prod(vec):
		continue
	#----------------------
	sent=1
	while sent:
		if start[0]==end[0] and start[1]==end[1]:
			sent=0
		crosses[start[0],start[1]]+=1
		start+=vec
print(np.sum(np.where(crosses>=2,1,0)))