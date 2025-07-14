# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        qu = deque([root])
        if not root:
            return []
        ans = [root.val]
        while qu:
            for _ in range(len(qu)):
                cur = qu.popleft()
                if cur.left:
                    qu.append(cur.left)
                if cur.right:
                    qu.append(cur.right)
            if qu:
                ans.append(qu[-1].val)

        return ans
                 