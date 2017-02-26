# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 09:00:42 2017

@author: JoseMaria
"""
"""
Suppose we want to model a bank account
with support for deposit and withdraw operations, also we can
change the owner name of the account.
One way to do that is by using python functions
that we know very well.
"""
def make_account():
    return {'balance': 0,'name':''}

def deposit(account, amount):
    account['balance'] += amount
    return account['balance']

def withdraw(account, amount):
    account['balance'] -= amount
    return account['balance']

def change_name(account, nname):
    account['name'] = nname
    return account['name']

a = make_account()
b = make_account()
deposit(a, 100)
change_name(a,"Pepito")
withdraw(a,20)
print(a)

##The same proces but OO

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.name = ""
    ##overloading operators
    def __str__(self):
        return self.name
    def __add__(self, other):
        return self.balance + other
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def change_name(self, nname):
        self.name = nname
        return self.name
    
a = BankAccount()
a.name = "Juanito"
a.deposit(50)
a.withdraw(3)
b = BankAccount()
b.name = "Pepito"
b.balance = 100

print(str(a))

a+100

##Inheritance with a more complex case
class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print('Sorry, minimum balance must be maintained.')
        else:
            BankAccount.withdraw(self, amount)
c = MinimumBalanceAccount(a)
c
c.minimum_balance = 0
c.withdraw(2000)
