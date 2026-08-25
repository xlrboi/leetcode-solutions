# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if root is None:
            return res

        st1 = []
        st2 = []

        st1.append(root)

        while len(st1) != 0:
            root = st1.pop()
            st2.append(root)

            if root.left is not None:
                st1.append(root.left)

            if root.right is not None:
                st1.append(root.right)

        while len(st2) != 0:
            res.append(st2.pop().val)

        return res        