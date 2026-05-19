class LinkedList:

    class Node:
        def __init__(self,val):
            self.val = val
            self.next = None
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        idx = 0
        t = self.head
        while idx < index:
            t = t.next
            idx+=1 
        return t.val

    def insertHead(self, val: int) -> None:
        if self.head is None:
            self.head = self.Node(val)
            self.size+=1
            return
        node = self.Node(val)
        node.next = self.head
        self.head = node
        self.size+=1
        

    def insertTail(self, val: int) -> None:
        node = self.Node(val)        
        if self.head:
            t=self.head
            while t.next:
                t = t.next
            t.next = node
        else:
            self.head = node
        self.size+=1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
        if index == 0:
            if self.size == 1:
                self.head = None
            else:
                self.head = self.head.next
            self.size-=1
            return True
        idx = 0
        t = self.head
        while idx < index-1:
            t = t.next
            idx+=1
        t.next = t.next.next
        self.size-=1
        return True


    def getValues(self) -> List[int]:
        ans = []
        t = self.head
        while t:
            ans.append(t.val)
            t = t.next
        return ans        
