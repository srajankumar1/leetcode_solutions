class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        k=(n*(n+1))//2
        return k-sum(nums)