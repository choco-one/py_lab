#!/usr/bin/python     


number = input("Input Number : ")
number = int(number)

sum=0

for i in range(number):
	num = input()
	num = int(num)
	sum = sum + num;

average = sum / float(number) 

print('Average : %.2f '%(average))
