from typing import Optional

from util.list_node import ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next  # type: ignore
            fast = fast.next.next

        list_iter = slow
        new = None

        while list_iter:
            nxt = list_iter.next
            list_iter.next = new
            new = list_iter
            list_iter = nxt

        while new:
            if head.val != new.val:  # type: ignore
                return False
            head = head.next  # type: ignore
            new = new.next

        return True
