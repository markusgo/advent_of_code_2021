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
	soma=0
	for i in open("input","r"):
		wires = i.strip().split("|")[0].split()
		output = i.strip().split("|")[1].split()
		res = {}
		wires = [set(x) for x in wires]
		res[1] = [x for x in wires if len(x)==2][0]
		wires.remove(res[1])
		res[4] = [x for x in wires if len(x)==4][0]
		wires.remove(res[4])
		res[7] = [x for x in wires if len(x)==3][0]
		wires.remove(res[7])
		res[8] = [x for x in wires if len(x)==7][0]
		wires.remove(res[8])
		res[9] = [x for x in wires if (len(x)==6 and res[4].issubset(x))][0]
		wires.remove(res[9])
		res[3] = [x for x in wires if (len(x)==5 and res[1].issubset(x))][0]
		wires.remove(res[3])
		res[0] = [x for x in wires if (len(x)==6 and res[7].issubset(x))][0]
		wires.remove(res[0])
		res[6] = [x for x in wires if (len(x)==6)][0]
		wires.remove(res[6])
		res[5] = [x for x in wires if (len(x)==5 and x.issubset(res[9]))][0]
		wires.remove(res[5])
		res[2] = wires[0]
		newdict={}
		for i,j in res.items():
			arr = sorted(list(j))
			newdict["".join([i for i in arr])] = i

		number=""
		for i in output:
			arr = sorted(list(i))
			number+=str(newdict["".join([i for i in arr])])
		soma+=int(number)
	print(soma)
part_two()