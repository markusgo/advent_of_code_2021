fish = [int(i) for i in open("input","r").read().strip().split(",")]
day=0
while day<80:
	day+=1
	toadd = 0
	for j in range(len(fish)):
		fish[j] = fish[j]-1
		if fish[j]==0:
			toadd+=1
			fish[j]=7
	fish.append([9 for i in range(toadd)])
print(len(fish))