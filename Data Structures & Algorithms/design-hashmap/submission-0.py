class MyHashMap:

    def __init__(self):
        self.size=dict()
    
    def _hashIndex(self, key):
        return key in self.size

    def put(self, key: int, value: int) -> None:
        self.size[key]=value

    def get(self, key: int) -> int:
        if self._hashIndex(key):
            val=self.size[key]
            return val
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.size:
            del self.size[key]


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
key=1
value=1
obj.put(key,value)
param_2 = obj.get(key)
obj.remove(key)