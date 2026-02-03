class Solution:
    def findMinHeightTrees(self, n, edges):
        if n==1:
            return [0]
        adj=[[] for _ in range(n)]
        deg=[0]*n
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            deg[u]+=1
            deg[v]+=1
        leaves=[]
        for i in range(n):
            if deg[i]==1:
                leaves.append(i)
        rem=n
        while rem>2:
            rem-=len(leaves)
            new=[]
            for u in leaves:
                for v in adj[u]:
                    deg[v]-=1
                    if deg[v]==1:
                        new.append(v)
            leaves=new
        return leaves