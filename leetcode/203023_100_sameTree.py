# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q: return False
        if q is None and p: return False
        if p is None and q is None: return True
        if p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

def generateNode(*args):
    t = TreeNode(args[0])
    p = t
    for i, arg in enumerate(args[1:]):
        i += 1
        if i % 2 == 1: p.left = TreeNode(arg)
        else:
            p.right = TreeNode(arg)
            p = p.left
    return t        

p = generateNode(1,2,3,4)
q = generateNode(2,2,3,4)

sol = Solution()
result = sol.isSameTree(p, q)
print(result)