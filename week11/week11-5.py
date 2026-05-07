# week11-5.py 學習計畫 Binary Tree - BFS P1
# leetcode 199. Binary Tree Right Side View
# 由上至下,輸出每層最右的值
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def helper(root, level):
            if root == None: return 
            if len(ans) <= level:#看這層數走過沒
                ans.append(root.val)#沒走過就增加list
            else:
                ans[level] = root.val#走過就從index改值
            
            helper(root.left, level+1)
            helper(root.right, level+1)

        helper(root, 0)
        return ans
        