from typing import Optional

from util.list_node import ListNode


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = ListNode(val=-1, next=head)
        list_iter = temp

        while list_iter:
            nxt = list_iter.next

            if nxt and nxt.val == val:
                list_iter.next = list_iter.next.next  # type: ignore
            else:
                list_iter = list_iter.next

        return temp.next
