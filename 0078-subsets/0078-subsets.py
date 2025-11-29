class Solution(object):
    def subsets(self, nums):
        res = []
        curr = []

        def backtrack(i):
            if i == len(nums):
                res.append(curr[:])
                return
            curr.append(nums[i])
            backtrack(i+1)
            curr.pop()
            backtrack(i+1)

        backtrack(0)
        return res