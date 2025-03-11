from typing import Optional

from util.list_node import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        new = None
        while cur != None:
            nxt = cur.next
            cur.next = new
            new = cur
            cur = nxt
        return new
