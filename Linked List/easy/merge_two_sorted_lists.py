from typing import Optional

from util.list_node import ListNode


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        temp = ListNode()
        cur = temp

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
                cur = cur.next
            else:
                cur.next = list2
                list2 = list2.next
                cur = cur.next

        while list1:
            cur.next = list1
            list1 = list1.next
            cur = cur.next

        while list2:
            cur.next = list2
            list2 = list2.next
            cur = cur.next

        return temp.next
