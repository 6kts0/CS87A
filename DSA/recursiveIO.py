"""
Traversing Binary Trees
------------------------------
Recursive In Order
LEFT > NODE > RIGHT
"""

#    1
#  2   3
# 4  5  10
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

# Recursive pre order traversal (DFS)
def in_order(node):
    if not node:
      return
    
    in_order(node.left)
    print(node)
    in_order(node.right)

in_order(A)