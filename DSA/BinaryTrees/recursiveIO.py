#     __1__
#    /     \
#   6       3
#  / \     / \
# 5   2   4   0

"""
RECURSIVE IN-ORDER TRAVERSAL (DFS)
LEFT > NODE > RIGHT 
"""



class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
    def __str__(self):
        return str(self.val)
    

A = TreeNode(1)
B = TreeNode(6)
C = TreeNode(3)
D = TreeNode(5)
E = TreeNode(2)
F = TreeNode(4)
G = TreeNode(0)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
C.right = G

def in_order(node):
    if not node:
        return
    
    in_order(node.left)
    print(node)
    in_order(node.right)

 
in_order(A)




