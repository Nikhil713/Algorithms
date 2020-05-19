# Question: https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705

tcase=int(input())
for i in range(tcase):
	arr=list(map(int,str(input())))
	b=0
	arr.reverse()
	for j in range(len(arr)):
		if arr[j]==4:
			arr[j]-=1
			b+=10**j
		arr.reverse()
		s=int("".join(map(str,arr)))
	print("Case #",i+1,": ",s," ",b,sep='')
