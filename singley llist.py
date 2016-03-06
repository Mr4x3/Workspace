class Node:
    def __init__(self,value):
        self.value=value
        self.next=None






a=Node(1)
b=Node(2)
c=Node(3)
a.next=b
b.next=c

def reverse(node):
    current=node
    while current.next != None:
        thirdnext=current.next.next
        current.next.next=current
        current=thirdnext
        
reverse(a)
