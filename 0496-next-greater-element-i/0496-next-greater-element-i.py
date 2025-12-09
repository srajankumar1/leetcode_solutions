class Solution:
    def nextGreaterElement(self, nums1, nums2):
        next_greater = {}
        stack = []

        for x in nums2:
            while stack and x > stack[-1]:
                val = stack.pop()
                next_greater[val] = x
            stack.append(x)

        while stack:
            val = stack.pop()
            next_greater[val] = -1

        result = []
        for x in nums1:
            result.append(next_greater[x])
        return result