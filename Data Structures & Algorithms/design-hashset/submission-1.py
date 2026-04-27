class MyHashSet:

    def __init__(self):
        self.set_a = set()

    def add(self, key: int) -> None:
        self.set_a.add(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.set_a.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.set_a


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)