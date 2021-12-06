from collections import Counter
fish  = Counter([int(i) for i in open("input","r").read().strip().split(",")])
for i in range(1,257):
	newfish=[0,0,0,0,0,0,0,0,0]
	for j in (1,2,3,4,5,6,8):
		newfish[j-1] = fish[j]
	newfish[6] = fish[0]+fish[7]
	newfish[8] = fish[0]
	fish=newfish
print(i,sum(fish))