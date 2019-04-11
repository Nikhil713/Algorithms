
tcase=int(input())
for i in range(tcase):
	count=0
	chef=''
	assistant=''
	jobs=input().split()
	total=int(jobs[0])
	completed_no=int(jobs[1])
	completed=input().split()
	for j in range(completed_no):
		completed[j]=int(completed[j])
	completed.sort()
	for j in range(1,total+1):
		if j not in completed:
			if(count%2==0):
				chef+=str(j)+' '
			else:
				assistant+=str(j)+' '
			count+=1
	print(chef)
	print(assistant)
