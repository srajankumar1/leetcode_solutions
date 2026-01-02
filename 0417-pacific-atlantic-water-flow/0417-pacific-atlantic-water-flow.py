class Solution:
    def pacificAtlantic(self, heights):
        if not heights:
            return []
        m,n=len(heights),len(heights[0])
        pacific=[[False]*n for _ in range(m)]
        atlantic=[[False]*n for _ in range(m)]
        def dfs(r,c,vis):
            vis[r][c]=True
            for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr,nc=r+dr,c+dc
                if 0<=nr<m and 0<=nc<n and not vis[nr][nc] and heights[nr][nc]>=heights[r][c]:
                    dfs(nr,nc,vis)
        for i in range(m):
            dfs(i,0,pacific)
            dfs(i,n-1,atlantic)
        for j in range(n):
            dfs(0,j,pacific)
            dfs(m-1,j,atlantic)
        res=[]
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i,j])
        return res