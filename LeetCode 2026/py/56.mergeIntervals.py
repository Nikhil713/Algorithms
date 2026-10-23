# Standard Solution: How do I even come with this if I have never seen this before? I guess I need to practice more problems :(.

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda x: x[0])
        resultArr = []
        
        for interval in intervals:
            if not resultArr or interval[0] > resultArr[-1][1]:
                resultArr.append(interval)
            else:
                resultArr[-1][1] = max(resultArr[-1][1], interval[1])
        return resultArr



# My Soltion
# class Solution:
#     def merge(self, intervals: list[list[int]]) -> list[list[int]]:
#         intervals.sort(key = lambda x: x[0])
#         resultArr = []
#         i = 0
#         print(intervals)
#         while i < len(intervals):
#             tempInterval = intervals[i]
#             while i!= len(intervals) - 1 and tempInterval[1] >= intervals[i+1][0]:
#                     i += 1
#                     tempInterval[1] = max(tempInterval[1], intervals[i][1])
#             i += 1
#             resultArr.append(tempInterval)
#             print(i)
#         return resultArr