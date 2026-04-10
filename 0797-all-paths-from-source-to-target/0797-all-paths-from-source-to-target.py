class Solution:
    def allPathsSourceTarget(self, graph):
        res=[]
        n=len(graph)
        def dfs(node,path):
            if node==n-1:
                res.append(path)
                return
            for nei in graph[node]:
                dfs(nei,path+[nei])
        dfs(0,[0])
        return res