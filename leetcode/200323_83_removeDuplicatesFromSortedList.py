# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return head
        r = []
        d = ListNode(0)
        p = d
        pre = head.val
        c = False
        while head.next:
            v = head.next.val
            if pre == v: r.append(pre)
            if pre not in r:
                p.next = ListNode(pre)
                p = p.next
            pre = v
            head = head.next
            if head.next is None and v not in r: p.next = ListNode(v)
        return d.next
    
l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)
l.next.next.next.next.next = ListNode(5)
l.next.next.next.next.next.next = ListNode(5)

sol = Solution()
d = sol.deleteDuplicates(l)
print(d.val)