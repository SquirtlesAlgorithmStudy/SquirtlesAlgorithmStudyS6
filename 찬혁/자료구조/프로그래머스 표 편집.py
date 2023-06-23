#수정해야함

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = self
        self.prev = self

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None
        
    def insertAfter(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head

        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode



def solution(n, k, cmd):
    chart = LinkedList()
    chart.insertAfter('head', 0)
    for i in range(n-1):
        chart.insertAfter(i, i+1)
    
    chart.insertAfter(n-1, 'tail')
    chart.insertAfter(n-1, )
    return answer


n = 8
k = 2
cmd1 = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
cmd2 = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]

print(solution(n, k, cmd1))
print(solution(n, k, cmd2))