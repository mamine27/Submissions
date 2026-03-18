# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        def do(node = root):
            
            if node.val < val:
                if not node.right:
                    node.right = TreeNode(val)
                    return
                do(node.right)

            else:
                if not node.left:
                    node.left = TreeNode(val)
                    return
                do(node.left)


        do()
        return root