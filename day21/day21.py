p1pos=6
p2pos=1
p1res=0
p2res=0
diceval=0
n=0
while True:
	dice=[(diceval+i)%100+1 for i in range(0,3)]
	p1pos=p1pos+sum(dice)%10
	p1pos-=10*(p1pos>10)
	print("p1: ",sum(dice),p1pos)
	p1res+=p1pos 
	diceval=dice[2]
	n+=3
	if p1res>=1000:
		break
	dice=[(diceval+i)%100+1 for i in range(0,3)]
	p2pos=p2pos+sum(dice)%10
	p2pos-=10*(p2pos>10)
	p2res+=p2pos
	print("p2: ",sum(dice),p2pos)
	n+=3
	diceval=dice[2]
	if p2res>=1000:
		break

print(min(p1res,p2res)*n)