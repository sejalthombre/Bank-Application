balance=0
def check_balance():
    print("total balance :",balance)
def deposit(amt):
    global balance
    balance=balance+amt
    print(amt,"RS.deposits")
def withdraw(amt):
    global balance
    if balance==balance>=amt:
        balance=balance-amt
        print(amt,"RS.withdraw")
    else:
        print("SORRY! insufficient balance")
while True:
    choice=int(input("enter the choice :\n1.deposit\t2.withdraw\n3.check balance\t4.exits"))
    match choice:
        case 1:
            print("deposit cash")
            d_amt=int(input("enter deposit amount"))
            deposit(d_amt)
        case 2:
            print("withdraw cash")
            w_amt=int(input("enter withdraw amount"))
            withdraw(w_amt)
        case 3:
            print("check balance")
            check_balance()
        case 4:
            print("exiting")
            break
        case _:
            print("invalid choice")
