numbers=[i.strip() for i in open("input","r")]
nbits = len(numbers[0])
freq = [sum(int(row[i]) for row in numbers) for i in range(nbits)]
gamma = "".join(str(int(i>len(numbers)/2)) for i in freq)
epsilon = "".join( str(int(not int(i))) for i in gamma)

numbers2 = numbers
n=0
while len(numbers2)>1:
	a = sum(int(row[n]) for row in numbers2)
	morecommon=""
	if a>=len(numbers2)/2:
		morecommon="1"
	else:
		morecommon="0"
	new_numbers=[]
	for i in numbers2:
		if i[n]==morecommon:
			new_numbers.append(i)
	numbers2 = new_numbers
	n+=1
co2=int(numbers2[0],2)

numbers2 = numbers
n=0
while len(numbers2)>1:
	a = sum(int(row[n]) for row in numbers2)
	lesscommon = ""
	if a>=len(numbers2)/2:
		lesscommon="0"
	else:
		lesscommon="1"
	new_numbers=[]
	for i in numbers2:
		if i[n]==lesscommon:
			new_numbers.append(i)
	numbers2 = new_numbers
	n+=1
o2=int(numbers2[0],2)
print(co2*o2)
