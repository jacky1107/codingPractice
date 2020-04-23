# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        res = 0
        temp1 = ""
        temp2 = ""
        while True:
            if l1 is not None: temp1 += str(l1.val)
            if l2 is not None: temp2 += str(l2.val)
            if l1 is None and l2 is None: break
            if l1 is not None: l1 = l1.next
            if l2 is not None: l2 = l2.next
            
        temp1 = temp1[::-1]
        temp2 = temp2[::-1]
        res = str(int(temp1) + int(temp2))[::-1]
        r = ListNode(int(res[0]))
        temp = r
        for i in range(1, len(res)):
            temp.next = ListNode(int(res[i]))
            temp = temp.next
        return r


l1 = ListNode(1)
l1.next = ListNode(8)
l1.next.next = ListNode(3)

l2 = ListNode(0)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

sol = Solution()
r = sol.addTwoNumbers(l1, l2)
# r = 381 + 460 = 841
# r = 1 -> 4 -> 8
