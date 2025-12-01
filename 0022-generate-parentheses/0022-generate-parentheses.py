class Solution(object):
    def generateParenthesis(self, n):
        res = []
        def backtrack(openP, closeP, curr):
            if len(curr) == 2 * n:
                res.append(curr)
                return
            if openP < n:
                backtrack(openP + 1, closeP, curr + "(")
            if closeP < openP:
                backtrack(openP, closeP + 1, curr + ")")
        backtrack(0, 0, "")
        return res