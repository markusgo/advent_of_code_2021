from collections import Counter
def part_one():
	data = [i[i.index("|")+1:].strip() for i in open("input").readlines()]
	allstr = ""
	for i in data:
		allstr += " "+i
	lens = dict(Counter([len(i) for i in allstr.split()]))
	print(lens[2]+lens[4]+lens[3]+lens[7])
part_one()

def part_two():

	for i in open("input","r"):
		wires = i.strip().split("|")[0].split()
		output = i.strip().split("|")[1].split()
		print(wires,output)
		keys = {}
		for i in wires:
			if len(i)==2:
				keys[1] = i
			elif len(i)==4:
				keys[4] = i
			elif len(i)==3:
				keys[7] = i
			elif len(i)==7:
				keys[8] = i
		print(keys)	

part_two()