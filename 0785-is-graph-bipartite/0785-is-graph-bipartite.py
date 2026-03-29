class Solution:
    def isBipartite(self, graph):
        n=len(graph)
        color=[0]*n
        for i in range(n):
            if color[i]!=0:
                continue
            stack=[i]
            color[i]=1
            while stack:
                node=stack.pop()
                for nei in graph[node]:
                    if color[nei]==0:
                        color[nei]=-color[node]
                        stack.append(nei)
                    elif color[nei]==color[node]:
                        return False
        return True