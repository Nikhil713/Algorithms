import numpy

narr = numpy.array([input().split() for _ in range(int(input().split()[0]))],int)
print(narr.transpose())
print(narr.flatten())