from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        l3 = ListNode()
        l1Ref = l1
        l2Ref = l2
        l3Ref = l3

        remain = 0
        while l1Ref or l2Ref:
            # 1. calc sum
            if l1Ref:
                l3Ref.val += l1Ref.val
                l1Ref = l1Ref.next

            if l2Ref:
                l3Ref.val += l2Ref.val
                l2Ref = l2Ref.next

            # 2. calc remain
            if l3Ref.val >= 10:
                remain = l3Ref.val // 10
                l3Ref.val = l3Ref.val % 10

            # 3. prepare next
            if remain > 0 or l1Ref or l2Ref:
                l3Ref.next = ListNode(remain)
                remain = 0
                l3Ref = l3Ref.next

        return l3


n1 = ListNode(2, ListNode(4, ListNode(3)))
n2 = ListNode(5, ListNode(6, ListNode(4)))
p = Solution()
ans = p.addTwoNumbers(n1, n2)
while ans:
    print(ans.val)
    ans = ans.next
