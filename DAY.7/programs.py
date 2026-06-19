'''
#queue:(function)
front=0
rear=-1
queue = [None]
size=0
def enqueue(value):
  if size==len(queue):return'queue overflow'
  rear+=1
  size+=1
  queue[rear]=value
def dequeue():
  if size==0:return False
  front+=1
  return True
def peek():
  return queue[front]
def peek():
  return queue[front]
def isFull():
  return size == len(queue)
def isEmpty():
  return size==0
'''
'''
# linked list:
class Node:
  def __init__ (self,data):
    self.data = data
    self.next = None
Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(40)
Node1.data=30
Node1.next=Node2
print(Node1.data)
print(Node2.data)
print(Node3.data)
'''