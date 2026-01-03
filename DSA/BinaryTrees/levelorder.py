#     __2__
#    /     \
#   4       3
#  / \     / \
# 0   5   1   6
"""
Level Order traversal (BFS)
"""
from collections import deque 

class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)
    
A = TreeNode(2)
B = TreeNode(4)
C = TreeNode(3)
D = TreeNode(0)
E = TreeNode(5)
F = TreeNode(1)
G = TreeNode(6)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
C.right = G

def level_order(node):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()
        print(node)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)

level_order(A)