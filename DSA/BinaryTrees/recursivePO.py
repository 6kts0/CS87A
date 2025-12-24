
#                    __________________14____________________
#                   /                                        \
#         _________12_______                         _________15________
#        /                  \                       /                   \
#    ___13___              __18__              ____3___               ___25__
#   /        \            /      \            /        \             /       \
#  11        _0         _9        19        _23        _30         _5         10
"""
RECURSIVE PRE ORDER TRAVERSAL (DFS)
NODE > LEFT > RIGHT
"""

# Initialize tree node class and 
class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        return
    
    def __str__(self):
        return str(self.val)

# Define branch nodes
A = TreeNode(14)
B = TreeNode(12)
C = TreeNode(15)
D = TreeNode(13)
E = TreeNode(18)
F = TreeNode(3)
G = TreeNode(25)
H = TreeNode(11)
I = TreeNode(0)
J = TreeNode(9)
K = TreeNode(19)
L = TreeNode(23)
M = TreeNode(30)
N = TreeNode(5)
O = TreeNode(10)

# Define branches
A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
C.right = G
D.left = H
D.right = I
E.left = J
E.right = K
F.left = L
F.right = M
G.left = N
G.right = O

# Pre ordered traversal function
def pre_order(node):
        
    if not node:
        return
    
    print(f"\nRoot: {node}")
    print(f"Subnode left: {node.left}")
    print(f"Subnode right: {node.right}")
    print('=' * 19)
    pre_order(node.left)
    pre_order(node.right)
    

pre_order(A)
