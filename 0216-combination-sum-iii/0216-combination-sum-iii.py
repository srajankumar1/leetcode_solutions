class Solution:
    def combinationSum3(self, k, n):
        res=[]
        def dfs(start,remain,path):
            if len(path)==k and remain==0:
                res.append(path[:])
                return
            if len(path)>k or remain<0:
                return
            for i in range(start,10):
                path.append(i)
                dfs(i+1,remain-i,path)
                path.pop()
        dfs(1,n,[])
        return res