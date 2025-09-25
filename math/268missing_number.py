from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sum_nums=sum(nums)
        sum_full=(n*(n+1))//2
        return sum_full-sum_nums

print(Solution().missingNumber([1,2,4,0]))