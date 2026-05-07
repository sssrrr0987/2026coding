# week11-2.py 學習計畫 Binary Tree - DFS P6
# leetcode 236. Lowest Common Ancestor of a Binary Tree
# 求p q兩值的最小祖先是誰
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        a = []
        def helper(root):
            count = 0#目前節點下有幾個p或q
            if root == None:return 0
            if root == p or root == q:#目前是q或p
                count += 1
            count += helper(root.left)#往左找
            count += helper(root.right)#往右找
            if count == 2:a.append(root)#p q 都有了存起來這個節點
            return count
        helper(root)
        return a[0]#回傳第一次找到的,就是最短