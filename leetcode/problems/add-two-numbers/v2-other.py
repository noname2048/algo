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
        dummy_head = tail = ListNode()
        carry = 0

        while l1 is not None or l2 is not None or carry > 0:
            _sum = (
                (l1.val if l1 is not None else 0)
                + (l2.val if l2 is not None else 0)
                + carry
            )
            carry, digit = divmod(_sum, 10)

            tail.next = ListNode(digit)
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        head = dummy_head.next
        dummy_head.next = None
        return head


n1 = ListNode(2, ListNode(4, ListNode(3)))
n2 = ListNode(5, ListNode(6, ListNode(4)))
p = Solution()
ans = p.addTwoNumbers(n1, n2)
while ans:
    print(ans.val)
    ans = ans.next
