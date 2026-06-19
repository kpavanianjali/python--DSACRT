"""#functions of linked list:
class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
class single_linkedList:
    def __init__ (self):
        self.head=None
        self.tail=None
        self.size=0



#insert at start functon:
def insertAtStart(self,value):
    newNode=Node(value)
    if self.head is None:
        self.head=newNode
        return
    newNode.next=self.head
    self.head=newNode
    return head 


#insertAtEnd function:
def insertAtEnd(self,value):
    newNode=node(value)
    if self.head is None:
        self.head=self.tail=newNode
        self.size+=1
        return
    self.tail.next=newNode
    self.tail=newNode
    return head


#inserAtEnd using without tail:
def inserAtEnd(self,value):
    newNode=Node(value)
    if self.head is None:
        self.head=newNode
        self.size+=1
        return
    current=self.head
    while current:
        current=current.next
    self.size+=1
    current.next=newNode
    return head


#deleteAtStart:
def deleteAtStart(self):
    if self.head is None:
        return -1
    if self.head.next is None:
        self.head=None
        return
    temp=self.head
    self.head=self.head.next
    temp.next=None
    self.size -1
    return self.head


#deleteFromEnd:
def deleteFromEnd(self):
    if self.head is None:
        return -1
    if self.head.next is None:
        self.head=None
        return
    current=self.head
    while current.next.head:
        current=current.next
    current.next=None
    self.size -1
    return delete


#display function:
def display(self):
    current=self.head
    while current:
        print(current.data)
        current=current.next


#deleteAtIndex:
def deleteAtIndex(self,index):
    if self.head is None:
        return -1
    if index==0:
        deleteAtStart()
        return
    if index==self.size-1:
        deleteFromEnd()
        return
    current=self.head
    for i in range(index-1):
        current=current
    temp=current.next     
    current.next=temp.next
    temp.next=None
    return temp
"""


current=head
prev=None
while current:
    next=current.next
    current.next=prev
    prev=current
    current=next
return prev