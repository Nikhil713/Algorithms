tcase=int(input())
num1=0
for i in range(tcase):
	no=int(input())
	numbers=input().split()
	num=int(input())
	num1=numbers[num-1]
	numbers.sort(key=int)
	for j in range(no):
		if(numbers[j]==num1):
			print(j+1)
