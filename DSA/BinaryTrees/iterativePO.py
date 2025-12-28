#     __1__
#    /     \
#   4       0
#  / \     / \
# 6   2   3   5

"""
Iterative Pre Order Traversal
NODE > LEFT > RIGHT
"""

class TreeNode():
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

    def __str__(self):
        return str(self.val)
    

A = TreeNode(1)
B = TreeNode(4)
C = TreeNode(0)
D = TreeNode(6)
E = TreeNode(2)
F = TreeNode(3)
G = TreeNode(5)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
C.right = G

def iter_preorder(node):
    stk = [node]
    
    while stk:
        node = stk.pop()
        if node.left:
            stk.append(node.left)
        if node.right:
            stk.append(node.right)
        print(node)

iter_preorder(A)