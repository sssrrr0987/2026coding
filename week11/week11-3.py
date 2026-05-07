# week11-3.py 學習計畫 Binary Search Tree - BST P1
# leetcode 700. Search in a Binary Search Tree
# 在BST中找到目標節點
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def helper(root, val):
            if root == None:return None
            if val < root.val:#比現在小往左走
                return helper(root.left, val)
            if val > root.val:#比現在大往右走
                return helper(root.right, val)
            if val == root.val:#相等是答案
                return root
        return helper(root, val)
