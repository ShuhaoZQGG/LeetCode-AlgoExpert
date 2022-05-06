# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = collections.deque([(root, -math.inf, math.inf)])
        while queue:
            node, lower, upper = queue.pop()
            if not node:
                continue
            if node.val <= lower or node.val >= upper:
                return False
            queue.append((node.left, lower, node.val))
            queue.append((node.right, node.val, upper))
        return True