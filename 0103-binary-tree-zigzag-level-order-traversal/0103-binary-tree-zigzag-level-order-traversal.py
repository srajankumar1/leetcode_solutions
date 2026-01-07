class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        from collections import deque
        q=deque([root])
        res=[]
        ltr=True
        while q:
            size=len(q)
            level=deque()
            for _ in range(size):
                node=q.popleft()
                if ltr:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(list(level))
            ltr=not ltr
        return res