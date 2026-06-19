'''
class BankAccount:
  def __init__(self,account_holder,balance):
    self.account_holder = account_holder
    self.balance = balance
  def deposit(self,amount):
    self.balance += amount
  def withdraw(self,amount):
    if amount <= self.balance:
      self.balance -= amount
    else:
      print("Insufficient balance")
  def check_balance(self):
    print("balance:",self.balance)
account = BankAccount("Anna",1000)
account.deposit(500)
account.withdraw(200)
account.check_balance()
'''

'''
class car:
  def __init__ (self,brand,colour):
    self.brand = brand
    self.colour = colour
  def start_engine(self):
    print(f'{self.brand} car started')
car = car("toyota","red")
car.start_engine()
   '''

'''
class rectangle:
    def __init__ (self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

r1 = rectangle(5,3)

print(r1.area())
'''

'''
class student:
  def __init__ (self,name,roll_no,branch):
    self.name = name
    self.roll_no = roll_no
    self.branch = branch
  def display(self):
    print(f'name:{self.name}')
    print(f'roll_no:{self.roll_no}')
    print(f'branch:{self.branch}')
s1 = student("anjali","449","ece")
s1.display()
   '''








