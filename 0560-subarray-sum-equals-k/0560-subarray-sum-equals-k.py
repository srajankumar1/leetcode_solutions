class Solution:
    def subarraySum(self, nums, k):
        count=0
        prefix=0
        seen={0:1}
        for n in nums:
            prefix+=n
            need=prefix-k
            if need in seen:
                count+=seen[need]
            seen[prefix]=seen.get(prefix,0)+1
        return count