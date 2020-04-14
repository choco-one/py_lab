#!/usr/bin/python

num = int(input('Input Num : '))

def fibonacci(num):
	if num < 2:
		return num
	else:
		return fibonacci(num-1)+fibonacci(num-2)

for i in range(1,num+1):
	print(fibonacci(i),end=' ')

print(' ')
print('F%d ='%(num),end=' ')
print(fibonacci(num))
