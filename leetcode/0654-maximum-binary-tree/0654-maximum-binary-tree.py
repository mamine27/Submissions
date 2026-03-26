# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        

        def find(l , r):
            if l > r:
                return None
            if l == r:
                return TreeNode(nums[l])
            mx = -inf
            ps = -1
            for i in range(l , r+1):
                if nums[i] > mx:
                    ps = i
                mx = max(mx , nums[i])

            node = TreeNode(mx)


            lft = find(l , ps-1)
            rt = find(ps+1 , r)

            node.right = rt
            node.left = lft

            return node


        return find(0,len(nums)-1)