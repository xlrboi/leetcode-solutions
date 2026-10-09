# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if root is None:
            return True 
        p = root.left
        q = root.right

        def isSameTree(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False

            r1 = isSameTree(p.left, q.right)
            r2 = isSameTree(p.right, q.left)

            if (r1 == True) and (r2 == True):
                return True

            return False

        return isSameTree(p, q)
