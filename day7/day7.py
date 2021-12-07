import numpy as np
pos=np.array([int(i) for i in open("input","r").read().strip().split(",")])
mincost = np.min([np.sum(np.abs(pos-i,dtype=int)) for i in range(max(pos))])
print("Part One: ",mincost)
mincost = np.min([np.sum(np.abs(pos-i,dtype=int)*(np.abs(pos-i,dtype=int)+1)//2) for i in range(max(pos))])
print("Part Two: ",mincost)