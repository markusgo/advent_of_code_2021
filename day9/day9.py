import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from scipy.ndimage import measurements
def part_one():
	data=np.array([[int(j) for j in i.strip()] for i in open("input","r").readlines()])
	dims = np.shape(data)
	datapad = np.zeros((dims[0]+2,dims[1]+2),dtype=int)+10
	datapad[1:np.shape(datapad)[0]-1,1:np.shape(datapad)[1]-1]=data
	soma=0
	for i in range(1,np.shape(datapad)[0]-1):
		for j in range(1,np.shape(datapad)[1]-1):
			if datapad[i,j]==9:
				continue
			l,r,u,d = (datapad[i,j-1],datapad[i,j+1],datapad[i-1,j],datapad[i+1,j])
			if datapad[i,j]==np.min([datapad[i,j],l,r,u,d]):
				soma+=datapad[i,j]+1
	print(soma)

def part_two():
	data=np.array([[int(j) for j in i.strip()] for i in open("input","r").readlines()])
	dims = np.shape(data)
	datapad = np.zeros((dims[0]+2,dims[1]+2))+9
	datapad[1:np.shape(datapad)[0]-1,1:np.shape(datapad)[1]-1]=data
	data_bin = np.where(datapad==9,0,1)
	lw,num = measurements.label(data_bin)
	area = measurements.sum(data_bin,lw,index=np.arange(lw.max() + 1))
	print(int(np.prod(np.sort(area)[::-1][:3])))

part_one()
part_two()