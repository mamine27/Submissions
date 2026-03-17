# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def do(node):
            if not node.next:
                return node
            nxt = do(node.next)
            if node.val < nxt.val:
                return nxt
            else:
                node.next = nxt
                return node

        if not head:
            return head
        return do(head)


        