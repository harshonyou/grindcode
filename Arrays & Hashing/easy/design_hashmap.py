class ListNode:
    def __init__(self, key=0, val=0, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:
    SIZE = 10000

    def __init__(self):
        self.data = [ListNode() for _ in range(self.SIZE)]

    def offset(self, key: int) -> int:
        return key % self.SIZE

    def put(self, key: int, value: int) -> None:
        off = self.offset(key)

        linkedList = self.data[off]
        while linkedList.next:
            if linkedList.next.key == key:
                linkedList.next.val = value
                return

            linkedList = linkedList.next

        linkedList.next = ListNode(key, value)

    def get(self, key: int) -> int:
        off = self.offset(key)

        linkedList = self.data[off]
        while linkedList.next:
            if linkedList.next.key == key:
                return linkedList.next.val

            linkedList = linkedList.next

        return -1

    def remove(self, key: int) -> None:
        off = self.offset(key)

        linkedList = self.data[off]
        while linkedList.next:
            if linkedList.next.key == key:
                linkedList.next = linkedList.next.next
                return

            linkedList = linkedList.next
