class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        self.balance -=amount
    def __str__(self):
        return '(%s %d)' %(self.name,self.balance)

bank1 = BankAccount('권혁주',10000)
bank1.deposit(2000)
print(bank1.__str__())
bank1.withdraw(4000)
print(bank1.__str__())