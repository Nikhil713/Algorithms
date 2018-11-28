tcase=int(input())
num1=0
for i in range(tcase):
	no=int(input())
	numbers=input().split()
	for j in range(no):
		numbers[j]=int(numbers[j])
	num=int(input())
	for j in range(no):
		if(j==num):
			num1=numbers[num-1]
	numbers.sort()
	print(num1)
	for j in range(no):
		if(numbers[j]==num1):
			print(j+1)
