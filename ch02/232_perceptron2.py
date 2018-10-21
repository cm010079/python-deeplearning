# --coding:utf-8
import numpy as np

def AND(x1,x2):
	'''
	w1,w2,theta = 0.5,0.5,0.7
	tmp = x1*w1 + x2*w2

'''
	x=np.array([x1,x2])
	w=np.array([0.5,0.5])
	b=-0.7

	tmp = np.sum(w*x)+b

	if(tmp<=0):
		print(" return 0")
		return 0

	else:
		print(" return 1")
		return 1

def NAND(x1,x2):

	x=np.array([x1,x2])
	w=np.array([-0.5,-0.5])
	b=0.7

	tmp = np.sum(w*x)+b

	if(tmp<=0):
		print(" return 0")
		return 0

	else:
		print(" return 1")
		return 1

def OR(x1,x2):

	x=np.array([x1,x2])
	w=np.array([0.5,0.5])
	b=-0.2

	tmp = np.sum(w*x)+b

	if(tmp<=0):
		print(" return 0")
		return 0

	else:
		print(" return 1")
		return 1

def NOR(x1,x2):
	s1 = NAND(x1,x2)
	s2 = OR(x1,x2)
	y = AND(s1,s2)
	return  y

'''
print("AND 0-0")
AND(0,0)
print("AND 1-0")
AND(1,0)
print("AND 0-1")
AND(0,1)
print("AND 1-1")
AND(1,1)

print("NAND 0-0")
NAND(0,0)
print("NAND 1-0")
NAND(1,0)
print("NAND 0-1")
NAND(0,1)
print("NAND 1-1")
NAND(1,1)

print("OR 0-0")
OR(0,0)
print("OR 1-0")
OR(1,0)
print("OR 0-1")
OR(0,1)
print("OR 1-1")
OR(1,1)
'''
print("NOR 0-0")
NOR(0,0)
print("NOR 1-0")
NOR(1,0)
print("NOR 0-1")
NOR(0,1)
print("NOR 1-1")
NOR(1,1)
