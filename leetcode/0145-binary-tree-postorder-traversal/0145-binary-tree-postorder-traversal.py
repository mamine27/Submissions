# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        def do(node = root):
            if not node:
                return
            if node.left:
                do(node.left)
                ans.append(node.left.val)
            if node.right:
                do(node.right)
                ans.append(node.right.val)


        do()
        ans.append(root.val)
        return ans