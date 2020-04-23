# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode):
        result = []
        if root is None: return result
        current = [root]
        while len(current) != 0:
            val = []
            temp = []
            for i in range(len(current)):
                val.append(current[i].val)
                if current[i].left is not None:
                    temp.append(current[i].left)
                if current[i].right is not None:
                    temp.append(current[i].right)
            result.append( val )
            current = temp
        return result[::-1]

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
r = sol.levelOrderBottom(root)
print(r)