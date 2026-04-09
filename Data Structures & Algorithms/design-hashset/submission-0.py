class MyHashSet:

    def __init__(self):
        self.size=1000
        self.buckets=[[] for _ in range(self.size)]
        
    def _hashIndex(self, key):
        return key%self.size

    def add(self, key: int) -> None:
        index=self._hashIndex(key)

        if not self.contains(key):
            self.buckets[index].append(key)

    def remove(self, key: int) -> None:
        index=self._hashIndex(key)

        if self.contains(key):
            self.buckets[index].remove(key)

    def contains(self, key: int) -> bool:
        index=self._hashIndex(key)

        return key in self.buckets[index]


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
key=3
obj.add(key)
obj.remove(key)
param_3 = obj.contains(key)