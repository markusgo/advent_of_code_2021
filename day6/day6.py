import numpy as np
from collections import Counter
fish  = [int(i) for i in open("input","r").read().strip().split(",")]
count = Counter(fish)

#for i in range(1,80):
for i in range(1,257):
	dcount=np.zeros(9,dtype=int)
	for j in (1,2,3,4,5,6,8):
		dcount[j-1] = count[j]
	dcount[6] = count[0]+count[7]
	dcount[8] = count[0]
	count=dcount
	print(i,np.sum(count))