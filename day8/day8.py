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
		#wires = set(i.strip().split("|")[0].split())
		output = i.strip().split("|")[1].split()
		res = {}
		wires = [set(x) for x in "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab".split()]
		print(wires)
		res[1] = [x for x in wires if len(x)==2][0]
		res[4] = [x for x in wires if len(x)==4][0]
		res[7] = [x for x in wires if len(x)==3][0]
		res[8] = [x for x in wires if len(x)==7][0]
		res[3] = [x for x in wires if (len(x)==5 and res[7].issubset(x))][0]
		res[9] = [x for x in wires if (len(x)==6 and res[4].issubset(x))][0]
		res[0] = [x for x in wires if (len(x)==6 and not res[3].issubset(x))][0]
		print(res)
		break
part_two()