class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        idx={v:i for i,v in enumerate(inorder)}
        def build(pl,pr,il,ir):
            if pl>pr:
                return None
            rootVal=preorder[pl]
            root=TreeNode(rootVal)
            k=idx[rootVal]
            leftSize=k-il
            root.left=build(pl+1,pl+leftSize,il,k-1)
            root.right=build(pl+leftSize+1,pr,k+1,ir)
            return root
        return build(0,len(preorder)-1,0,len(inorder)-1)