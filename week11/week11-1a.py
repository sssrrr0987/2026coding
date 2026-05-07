# week11-1a.py 學習計畫 Binary Tree - DFS P2
# leetcode 872. Leaf-Similar Trees
# 求兩棵樹的葉子順序是否相同
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        a = []
        def helper(root):
            if root.left == None and root.right == None:
                a.append(root.val)
            if root.left: helper(root.left)
            if root.right: helper(root.right)
        helper(root1)
        a, b = [], a
        helper(root2)
        return a == b