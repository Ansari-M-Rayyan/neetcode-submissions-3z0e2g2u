class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key -> Node mapping

        # Left = Least Recently Used (LRU)
        # Right = Most Recently Used (MRU)
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    # Helper: Node ko linked list se remove karna (O(1))
    def _remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # Helper: Node ko right side (MRU) par insert karna (O(1))
    def _insert(self, node: Node) -> None:
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Since ye access ho gaya, isko MRU position par shift karo
            self._remove(node)
            self._insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Agar key already hai, purane node ko hatao
            self._remove(self.cache[key])
        
        # Naya node banao aur MRU par dalo
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._insert(new_node)

        # Agar capacity exceed ho gayi, LRU element ko evict karo
        if len(self.cache) > self.cap:
            lru = self.left.next  # left dummy node ke bagal wala node LRU hota hai
            self._remove(lru)
            del self.cache[lru.key]

# Implement an LRU cache using a hash map and a doubly linked list.
# The hash map gives O(1) access to nodes, while the linked list maintains
# usage order, with the left side as LRU and the right side as MRU.
# On get/put, move the accessed node to MRU; if capacity is exceeded, remove
# the LRU node.
# Time: O(1) per operation, Space: O(capacity)