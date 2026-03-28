class ListNode:
    def __init__(self, key=0, next=None):
        self.key = key
        self.next = next


class MyHashSet:
    SIZE = 10000

    def __init__(self):
        self.data = [ListNode() for _ in range(self.SIZE)]

    def offset(self, key: int) -> int:
        return key % self.SIZE

    def add(self, key: int) -> None:
        off = self.offset(key)

        linkedList = self.data[off]
        while linkedList.next:
            if linkedList.next.key == key:
                return
            linkedList = linkedList.next

        linkedList.next = ListNode(key)

    def remove(self, key: int) -> None:
        off = self.offset(key)

        linkedList = self.data[off]
        while linkedList.next:
            if linkedList.next.key == key:
                linkedList.next = linkedList.next.next
                return

            linkedList = linkedList.next

    def contains(self, key: int) -> bool:
        off = self.offset(key)

        linkedList = self.data[off]
        while linkedList.next:
            if linkedList.next.key == key:
                return True

            linkedList = linkedList.next

        return False
