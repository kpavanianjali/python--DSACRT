'''
stack = []
stack.append(5)
stack.append(6)
print(stack)      # o/p:[5,6]
stack.pop()
print(stack)      # o/p:[5]
stack.append(7)
stack.append(4)
print('stack',stack)  #o/p:[5,7,4]
print(stack[-1])      #o/p" 4  
print(len(stack)==0)
'''
'''
stack = [5,3,8,2,9]
l=len(stack)
t=8
for i in range(l):
    if stack.pop() == t:
        print("found")
        break
'''
'''  
class student:
  def __init__ (self,name,age):
    self.name=name
    self.age=age
  def display(self,name,age):
    print("name",self.name)
    print("age",age)
student1 = student("alice",20)
student1.display("sai",22)
'''
'''
class dog:
  def __init__ (self,slepping,eating,barking):
    self.slepping = slepping
    self.eating = eating
    self.barking = barking
  def display(self):
    print("dog is",self.slepping)
    print("dog is",self.eating)
    print("dog is",self.barking)
dog1 = dog("slepping","eating","barking")
dog1.display()
'''