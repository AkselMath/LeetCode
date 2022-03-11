class ListNode(object):
    def __init__(self, val=0, key=None, next=None, previous=None):
        self.val = val
        self.key = key
        self.previous = previous
        self.next = next

class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.head = ListNode()
        self.node = self.head
        self.filling_cache = 0

    def get(self, key):
        if key in self.cache:
            if self.cache[key].next != None:
                v = self.cache[key].val

                prev = self.cache[key].previous
                self.cache[key].previous.next = self.cache[key].next
                self.cache[key].next.previous = prev

                del self.cache[key]

                self.node.next = ListNode(v, key)
                self.node.next.previous = self.node
                self.node = self.node.next
                self.cache[key] = self.node

            return self.cache[key].val
        else:
            return -1

    def put(self, key, value):
        if self.filling_cache < self.capacity or key in self.cache:
            if key in self.cache:
                if self.cache[key].next != None:
                    prev = self.cache[key].previous
                    self.cache[key].previous.next = self.cache[key].next
                    self.cache[key].next.previous = prev

                    del self.cache[key]

                    self.node.next = ListNode(value, key)
                    self.node.next.previous = self.node
                    self.node = self.node.next

                    self.cache[key] = self.node
                else:
                    self.cache[key].val = value
            else:
                self.node.next = ListNode(value, key)
                self.node.next.previous = self.node
                self.node = self.node.next
                self.cache[key] = self.node
                self.filling_cache += 1

        else:
            del self.cache[self.head.next.key]
            if self.head.next.next != None:
                self.head.next = self.head.next.next
                self.head.next.previous = self.head

                self.node.next = ListNode(value, key)
                self.node.next.previous = self.node
                self.node = self.node.next
                self.cache[key] = self.node
            else:
                self.head.next = ListNode(value, key)
                self.head.next.previous = self.head
                self.node = self.head.next
                self.cache[key] = self.node
        return self.head.next