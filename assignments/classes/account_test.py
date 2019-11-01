from account import SavingsAccount, DebitAccount

def print_accounts(accounts):
    for account in accounts:
        print(account)

def update_accounts(accounts):
    for account in accounts:
        account.update_balance()

s1 = SavingsAccount(1000)
d1 = DebitAccount(1000)
s2 = SavingsAccount(2000)
d2 = DebitAccount(4000)

accounts = [s1,d1,s2,d2]
print_accounts(accounts)
update_accounts(accounts)

print_accounts(accounts)
update_accounts(accounts)

print_accounts(accounts)
update_accounts(accounts)
