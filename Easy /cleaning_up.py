
tcase=int(input())
to_be_done=[]
for i in range(tcase):
	k=0
	jobs=input().split()
	total=int(jobs[0])
	uncompleted=int(jobs[1])
	completed=input().split()
	for j in range(total-uncompleted):
		completed[j]=int(completed[j])
	completed.sort()
	for j in range(1,total+1):
		if j not in completed:
			to_be_done[k]=j
			print(to_be_done[j])
			k+=1
#	for j in range(len(to_be_done)):
#		print(to_be_done[j],end=' ')
#		j+=1
#	for j in range(1,len(to_be_done)):
#		print(to_be_done[j],end=' ')
#		j+=1
