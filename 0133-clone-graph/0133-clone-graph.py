class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        mp={}
        def dfs(n):
            if n in mp:
                return mp[n]
            copy=Node(n.val)
            mp[n]=copy
            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)