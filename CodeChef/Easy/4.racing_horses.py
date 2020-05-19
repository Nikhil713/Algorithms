tcase=int(input())
for i in range(tcase):
	num=int(input())
	arr=input().split()
	for i in range(num):
		arr[i]=int(arr[i])
	arr.sort()
	small=arr[1]-arr[0]
	for i in range(num-1):
		if(arr[i+1]-arr[i]<small):
			small=arr[i+1]-arr[i]
	print(small)
