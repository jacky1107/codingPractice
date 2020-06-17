class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        if not l1 and not l2: return l1
        if l1 and l2 is None: return l1
        if l2 and l1 is None: return l2
        if l1.val < l2.val: dummy = ListNode(l1.val)
        else: dummy = ListNode(l2.val)
        p = dummy
        while l1 or l2:
            if l1 and l2 is None:
                p.next = ListNode(l1.val)
                l1 = l1.next
            elif l2 and l1 is None:
                p.next = ListNode(l2.val)
                l2 = l2.next
            else:
                if l1.val <= l2.val:
                    p.next = ListNode(l1.val)
                    l1 = l1.next
                elif l2.val < l1.val:
                    p.next = ListNode(l2.val)
                    l2 = l2.next
            p = p.next
        return dummy.next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(2)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

sol = Solution()
r = sol.mergeTwoLists(l1, l2)
print(r)