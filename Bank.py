class Bank_Account: 
  def __init__(self):
   self.balance=0
   print("HELLO!!! welcome to the deposit & withdrawal machine")
  def deposit (self):
   amount=float (input("enter amount to be deposited:"))
   self.balance += amount
   print ("/n amount deposited:, amount")
  def withdraw (self):
   amount=float(input("enter amount to be withdrawn:"))
   if self.balance>=amount:
    self.balance-=amount
    print ("/n you withdraw:", amount)
   else:
    print ("/n Insufficient balance")
   def display(self):
    print ("/n net available balance=",self.balance)
s=Bank_Account()
s.deposit()
s.withdraw()
s.diaplay()
  
