class MyHashSet:

    def __init__(self):
        self.data = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.data.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            del self.data[self.data.index(key)]

    def contains(self, key: int) -> bool:
        return key in self.data
