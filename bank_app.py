#bank app 6/10/24
'''has ths following features 
open new account , show account , deposit amount ,withdraw amount , exit '''
import random

print('Welcome to the bank')
print("1.Open New account\n2.Show Account\n3.Deposit amount\n4.Withdraw amount\n5.Exit")
accounts = {}#This is the place where we store accno.
def open_acc(accounts):#
    name = str(input('enter your name:'))
    age = int(input('enter your age:'))
    account_number = random.randint(10000000,99999999)
    accounts[account_number] = {'name': name, 'age': age, 'balance': 0}
    print('This is your new account',account_number)

def show_acc(accounts):
    account_number = int(input('enter your Account number'))
    if account_number in accounts:
        account = accounts[account_number]
        print(f"Account Number: {account_number}\nName: {account['name']}\nAge: {account['age']}\nBalance: {account['balance']}")
    else:
        print("Account not found.")

def deposit_amount(accounts):
    account_number = int(input("Enter your account number: "))
    amount = float(input("Enter amount to deposit: "))
    if account_number in accounts:
        accounts[account_number]['balance'] += amount
        print(f"Successfully deposited {amount}. New balance: {accounts[account_number]['balance']}")
    else:
        print("Account not found.")

def withdraw_amount(accounts):
    account_number = int(input("Enter your account number: "))
    amount = float(input("Enter amount to Withdraw: "))
    if account_number in accounts:
        if accounts[account_number]['balance'] >= amount:
            accounts[account_number]['balance'] -= amount
        else:
            print("Insufficient funds.")
        print(f"Successfully deposited {amount}. New balance: {accounts[account_number]['balance']}")
    else:
        print("Account not found.")

while True:
    a = int(input('Enter your choice: '))
    
    if a == 1:
        open_acc(accounts)
    elif a== 2:
        show_acc(accounts)
    elif a == 3:
        deposit_amount(accounts)
    elif a == 4:
        withdraw_amount(accounts)
    elif a == 5:
        print('Thanks, see you again!')
    else:
        print("Invalid choice. Please select a number between 1 and 5.")







        '''Error i faced 
        
        1) Spelling mistake like used D in place d which led to a Name error
        2) used a >= 5 , so the code ends after choosing single function , so later i went to chat gpt and documentation and fixed it
          by using while True 
        3) at first i didn't create a empty dictionary like "accounts = {}" but forgot to create it 
        lead to a Nameerror 

        Documentation and chat gpt gave me a over look and reminded me some basic mistakes i have did



          '''