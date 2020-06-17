# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root, depth=0) -> int:
        if root: depth += 1
        else: return depth
        return max(self.maxDepth(root.left, depth=depth), self.maxDepth(root.right, depth=depth))
      

p = TreeNode(3)

p.left = TreeNode(9)
p.left.left = TreeNode(None)
p.left.right = TreeNode(None)

p.right = TreeNode(20)
p.right.left = TreeNode(15)
p.right.right = TreeNode(7)
p.right.right.right = TreeNode(0)

sol = Solution()
result = sol.maxDepth(p)
print(result)