import numpy as np

def part_one():
	gridlin = np.array([int(i) for i in open("input").read().replace("\n","")])
	gridpad = np.zeros((12,12))-1
	gridpad[1:11,1:11] = np.reshape(gridlin,(10,10))
	day = 0
	totflashed=0
	while day<100000:
		if np.sum(gridpad[1:11,1:11])==0:
			break
		gridpad = np.where(gridpad>=0,gridpad+1,gridpad).astype(int)
		flashed=np.zeros((12,12),dtype=int)
		while True:
			sumold=np.sum(np.where(gridpad>9))
			for i in range(1,11):
				for j in range(1,11):
					if gridpad[i,j]>=10 and flashed[i,j]==0:
						gridpad[i-1:i+2,j-1:j+2] += np.where(gridpad[i-1:i+2,j-1:j+2]!=-1,1,0)
						flashed[i,j]=1
			sumnew=np.sum(np.where(gridpad>9))
			print(gridpad)
			if sumold==sumnew:
				break
		gridpad = np.where(gridpad>9,0,gridpad)
		nflashed = np.sum(flashed)
		totflashed+=nflashed
		day+=1
		print("after day ",day,": ",nflashed," flashed")
		print("------------------------")
		print(gridpad)
	print(totflashed)

part_one()
