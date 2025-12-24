from bisect import bisect_left

class Solution:
    def jobScheduling(self,startTime,endTime,profit):
        jobs=sorted(zip(startTime,endTime,profit))
        starts=[s for s,_,_ in jobs]
        n=len(jobs)
        dp=[0]*(n+1)
        for i in range(n-1,-1,-1):
            j=bisect_left(starts,jobs[i][1])
            dp[i]=max(dp[i+1],jobs[i][2]+dp[j])
        return dp[0]