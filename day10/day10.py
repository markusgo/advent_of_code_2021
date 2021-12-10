def irred(a,charlist):
	lenold=1
	lennew=0
	while lenold!=lennew:
		lenold=len(a)
		for j in charlist:
			a=a.replace(j,"")
		lennew=len(a)
	return a

from collections import Counter
lines=[i.strip() for i in open("input","r").readlines()]
toremove=("()","[]","<>","{}")
irredlines=[irred(i,toremove) for i in lines]
incomplete = []
corrupted = []
for i in irredlines:
	count = Counter(i)
	if any(j in count for j in (")","]","}",">")):
		corrupted.append(i)
	else:
		incomplete.append(i)

values={"(":1,"[":2,"{":3,"<":4}
somas=[]
for i in incomplete:
	soma=0
	for j in i[::-1]:
		soma=soma*5+values[j]
	somas.append(soma)

import numpy
print(numpy.median(somas))