# Problem: House Robber III - https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node = root):
            if not node.left and not node.right:
                return [node.val , 0]
            choosme = node.val
            notchooseme = 0
            if node.right:
                choose , notchoose = dfs(node.right)
                choosme += notchoose
                notchooseme += choose
            if node.left:
                choose , notchoose = dfs(node.left)
                choosme += notchoose
                notchooseme += choose

            return [max(choosme, notchooseme) , notchooseme]

        return max(dfs())


        