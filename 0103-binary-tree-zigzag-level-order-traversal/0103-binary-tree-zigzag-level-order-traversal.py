from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        ans = []
        if root is None:
            return ans
        queue = deque([root])
        left_to_right = 1


        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if left_to_right == 0:
                level.reverse()

            ans.append(level)
            left_to_right = 1 - left_to_right

        return ans
                

