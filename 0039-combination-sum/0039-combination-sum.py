class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        def backtrack(i, curr, total):
            if total == target:
                res.append(list(curr))
                return
            if i >= len(candidates) or total > target:
                return
            curr.append(candidates[i])
            backtrack(i, curr, total + candidates[i])
            curr.pop()
            backtrack(i + 1, curr, total)
        backtrack(0, [], 0)
        return res