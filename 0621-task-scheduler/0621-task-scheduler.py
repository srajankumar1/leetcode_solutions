class Solution:
    def leastInterval(self, tasks, n):
        freq=[0]*26
        for t in tasks:
            freq[ord(t)-65]+=1
        freq.sort()
        maxf=freq[-1]-1
        idle=maxf*n
        for i in range(24,-1,-1):
            idle-=min(freq[i],maxf)
        return len(tasks)+max(0,idle)