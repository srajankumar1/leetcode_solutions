class Solution:
    def countArrangement(self, n):
        used=[False]*(n+1)
        def dfs(pos):
            if pos>n:
                return 1
            res=0
            for i in range(1,n+1):
                if not used[i] and (i%pos==0 or pos%i==0):
                    used[i]=True
                    res+=dfs(pos+1)
                    used[i]=False
            return res
        return dfs(1)