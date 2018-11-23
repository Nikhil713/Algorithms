tcase=int(input())
for i in range(tcase):
	no=int(input())
	numbers=input().split()
	for j in range(no):
		numbers[j]=int(numbers[j])
	num=int(input())
	for j in range(1,no+1):
		num=numbers[num]
	numbers.sort()
	for j in range(1,no+1):
		if numbers[j]==num:
			print(j)

