class Solution:
    def findTargetSumWays(self, nums, target):
        dp={0:1}
        for num in nums:
            nxt={}
            for s,c in dp.items():
                nxt[s+num]=nxt.get(s+num,0)+c
                nxt[s-num]=nxt.get(s-num,0)+c
            dp=nxt
        return dp.get(target,0)