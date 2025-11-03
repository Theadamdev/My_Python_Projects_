#this is my first beginner project in python
def show_balance(balance):
    print("***********************************")
    print(f"  Your balance is ${balance:.2f}  ")
    print("***********************************")

def deposit():
    print("************************************")
    amount = float(input("  How much do you want to deposit?  "))
    print("************************************")
    if amount <= 0:
        print("****************************************")
        print("  You cannot deposit a negative amount  ")
        print("****************************************")
        return 0
    else :
        return amount

def withdraw(balance):
    print("**************************************")
    amount = float(input("How much do you want to withdraw? "))
    print("**************************************")
    if amount > balance:
        print("********************************")
        print("  You do not have enough money  ")
        print("********************************")
        return 0
    elif amount <= 0:
        print("*****************************************")
        print("  You cannot withdraw a negative amount  ")
        print("*****************************************")
        return 0
    else :
        return amount

def main():
    balance = 0
    is_running = True
    while is_running:
        print("*******************")
        print("  Banking program  ")
        print("*******************")
        print("1.Show balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("*******************")

        choice = input("Enter your choice(1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("*******************")
            print("  Invalid choice   ")
            print("*******************")

    print("Thank you for using our banking program")

if __name__ == "__main__":
    main()

