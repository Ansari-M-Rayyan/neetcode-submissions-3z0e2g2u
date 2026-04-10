class MyHashMap:

    def __init__(self):
        self.size=1000
        self.buckets=[[] for _ in range(self.size)]
    
    def _hashIndex(self ,key):
        return key%self.size
        
    def put(self, key: int, value: int) -> None:
        index=self._hashIndex(key)

        for pair in self.buckets[index]:
            if pair[0]==key:
                pair[1]=value
                return
        self.buckets[index].append([key,value])

    def get(self, key: int) -> int:
        index=self._hashIndex(key)

        for k,v in self.buckets[index]:
            if k==key:
                return v
        return -1

    def remove(self, key: int) -> None:
        index=self._hashIndex(key)

        for i,pair in enumerate(self.buckets[index]):
            if pair[0]==key:
                del self.buckets[index][i]
                return


# Your MyHashMap object will be instantiated and called as such:

obj = MyHashMap()
key=2
value=3
obj.put(key,value)
param_2 = obj.get(key)
obj.remove(key)