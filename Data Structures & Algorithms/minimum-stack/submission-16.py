class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.mini = float('inf')

class MinStack:

    def __init__(self):
        self.head = Node(-1)
        

    def push(self, val: int) -> None:
        node = Node(val)
        t1 = self.head.next
        if t1:
            if val < t1.mini:
                node.mini = val
            else:
                node.mini = t1.mini
            node.next = t1
            self.head.next = node
        else:
            self.head.next = node
            node.mini = node.val
        

    def pop(self) -> None:
        node = self.head.next
        self.head.next = node.next

    def top(self) -> int:
        return self.head.next.val
        

    def getMin(self) -> int:
        return self.head.next.mini
