class Solution:
    def networkDelayTime(self, times, n, k):
        INF=10**9
        dist=[INF]*(n+1)
        dist[k]=0

        for _ in range(n-1):
            for u,v,w in times:
                if dist[u]!=INF and dist[u]+w<dist[v]:
                    dist[v]=dist[u]+w

        ans=0
        for i in range(1,n+1):
            if dist[i]>ans:
                ans=dist[i]

        if ans==INF:
            return -1
        else:
            return ans