import numpy


arr=input().split()
for _ in range(len(arr)):
    arr[_]=int(arr[_])
array1=numpy.array(arr)
print(numpy.reshape(array1,(3,3)))