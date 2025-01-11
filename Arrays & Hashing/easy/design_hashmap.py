class MyHashMap:

    def __init__(self):
        self.arr = []

    def put(self, key: int, value: int) -> None:
        for idx in range(len(self.arr)):
            k, v = self.arr[idx]
            if k == key:
                self.arr[idx] = (k, value)
                break
        else:
            self.arr.append((key, value))

    def get(self, key: int) -> int:
        for idx in range(len(self.arr)):
            k, v = self.arr[idx]
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        for idx in range(len(self.arr)):
            k, v = self.arr[idx]
            if k == key:
                self.arr[idx] = (k, -1)
                return
