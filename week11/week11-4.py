# week11-4.py 學習計畫 Binary Search Tree - BST P2
# leetcode 450. Delete Node in a BST
# 刪除某節點,後始結構繼續符合BST,找該節點左邊節點最右 或是 右邊節點最左 當繼承者

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findRightest(root):#找最右邊
            if root.right:#右邊還有繼續走
                return findRightest(root.right)
            return root
        
        if root == None:return root
        if root.val == key:
            if root.left:#找左節點最右
                now = findRightest(root.left)#找到繼承者
                root.val = now.val#繼承
                root.left = self.deleteNode(root.left, now.val)#把繼承者的舊位置也調成BST格式
                return root
            else:
                return root.right
        root.left = self.deleteNode(root.left, key)#往左找
        root.right = self.deleteNode(root.right, key)#往右找
        return root