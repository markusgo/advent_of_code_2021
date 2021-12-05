import numpy as np

f = open("input","r").readlines()
numbers = np.array(f[0].strip().split(",")).astype(int)
nlines = len(f)
cards = []
n=2
while n<nlines:
	card = np.zeros((5,5))
	mark = np.zeros((5,5))
	for i in range(0,5):
		a=[int(j) for j in f[n+i].split()]
		card[i]=a
	cards.append(card)
	n+=6

called=0
winner = 0
markwinner = 0
ncalled=0

senti = True
n=1
won = np.zeros(len(cards))
while senti and n<len(numbers):
	called = numbers[0:n]
	for i in range(len(cards)):
		if won[i]:
			continue
		mark = np.isin(cards[i],called).astype(int)
		sumrows=np.sum(mark,axis=0)
		sumcols=np.sum(mark,axis=1)
		if (5 in sumcols) or (5 in sumrows):
			won[i] = 1
		if np.sum(won)==len(cards):
			winner=i
			ncalled=called[-1]
			markwinner = mark
			senti=False
			break
	print(np.sum(won))
	n+=1

print(winner)
print(cards[winner])
print(markwinner)
print(np.sum(cards[winner]*np.abs(markwinner-1))*ncalled)