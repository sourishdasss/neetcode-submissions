class LRUCache:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.left = self.Node(0, 0)
        self.right = self.Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv
        node.next = None
        node.prev = None

    # we only insert into rightmost positon
    def insert(self, node):
        prv, nxt = self.right.prev, self.right
        prv.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prv

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # remove the node and insert into right
            self.remove(node)
            self.insert(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            # remove the node and insert into right
            self.remove(node)
            self.insert(node)
        else:
            node = self.Node(key, value)
            print(node)
            self.cache[key] = node
            self.insert(node)

            if len(self.cache.keys()) > self.capacity:
                # remove from left
                removal = self.left.next
                self.remove(removal)
                del self.cache[removal.key]





