class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        from collections import deque
        q=deque([root])
        res=[]
        while q:
            size=len(q)
            level=[]
            for _ in range(size):
                node=q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res