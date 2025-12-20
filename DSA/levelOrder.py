"""
Traversing Binary Trees
------------------------------
Level Order Traversal
"""
# Double sided queue
from collections import deque

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

def level_order (node):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()
        print(node)
        if node.left: q.append (node.left)
        if node.right: q.append(node.right)

level_order(A)


    