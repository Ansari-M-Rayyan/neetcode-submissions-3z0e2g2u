class MyHashSet:

    def __init__(self):
        self.size=[]
    
    def add(self, key: int) -> None:

        if not self.contains(key):
            self.size.append(key)

    def remove(self, key: int) -> None:

        if self.contains(key):
            self.size.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.size


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
key=3
obj.add(key)
obj.remove(key)
param_3 = obj.contains(key)