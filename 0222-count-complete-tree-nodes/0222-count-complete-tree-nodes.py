class Solution:
    def countNodes(self, root):
        def height(node):
            h=0
            while node:
                h+=1
                node=node.left
            return h
        if not root:
            return 0
        lh=height(root.left)
        rh=height(root.right)
        if lh==rh:
            return (1<<lh)+self.countNodes(root.right)
        else:
            return (1<<rh)+self.countNodes(root.left)