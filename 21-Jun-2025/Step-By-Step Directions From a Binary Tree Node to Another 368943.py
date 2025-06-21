# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

class TreeNode:
    def __init__(self, val=0, left=None, right=None ,up=None):
        self.val = val
        self.left = left
        self.right = right
        self.up = up

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        qu = deque([(root,TreeNode())])
        vis = set()
        st = None
        en = None
        while qu:

            for _ in range(len(qu)):

                cur, par = qu.popleft()

                if cur.val == startValue:
                    st = cur
                if cur.val == destValue:
                    en = cur

                cur.up = par
                if cur.right and cur.right.val not in vis:
                    qu.append((cur.right,cur))
                    vis.add(cur.right.val)
                if cur.left and cur.left.val not in vis:
                    qu.append((cur.left , cur))
                    vis.add(cur.left.val)

        qu = deque([st])
        vis = set()
        def mk():return [0,0]
        how = defaultdict(mk)
        while qu:

            for _ in range(len(qu)):

                cur = qu.popleft()
                if cur.right and cur.right.val not in vis:
                    qu.append((cur.right))
                    how[cur.right.val][0] = "R"
                    how[cur.right.val][1] = cur.val
                    vis.add(cur.right.val)
                if cur.left and cur.left.val not in vis:
                    qu.append((cur.left))
                    vis.add(cur.left.val)
                    how[cur.left.val][0] = "L"
                    how[cur.left.val][1] = cur.val
                
                if cur.up and cur.up.val not in vis:
                    qu.append((cur.up))
                    vis.add(cur.up.val)
                    how[cur.up.val][0] = "U"
                    how[cur.up.val][1] = cur.val

        how[startValue] = ["",-1]

        ans = []
      
        while how[destValue][1] != -1:
            ans.append(how[destValue][0])
            destValue = how[destValue][1]


        return "".join(ans[::-1])



        

