class Solution:
    def average(self, salary: List[int]) -> float:
        return mean(sorted(salary)[1:-1])