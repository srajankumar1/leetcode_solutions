class Solution(object):
    def permute(self, nums):
        res = []
        used = [False]*len(nums)
        curr = []

        def backtrack():
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    curr.append(nums[i])
                    backtrack()
                    curr.pop()
                    used[i] = False

        backtrack()
        return res