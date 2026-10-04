print(
    "-----------------------------------------------------------------------------------------"
)
print("---------------------------ATM MACHINE---------------------------------------")

balance = 0
pin = 1979
attemt = 0
while True:
    print(
        "What you want to do\n",
        "1 - withdraw\n"
        "2 - balance enquery\n"
        "3 - deposit\n"
        "4 - bas time pass!!!\n",
    )
    print(
        "-----------------------------------------------------------------------------------"
    )
    user = int(input("Enter your choice: "))
    print(
        "-----------------------------------------------------------------------------------"
    )

    if user == 1:
        print(
            "-----------------------------------------------------------------------------------"
        )
        withdraw_amount = int(input("Enter Your amount: "))
        print(
            "-----------------------------------------------------------------------------------"
        )
        if balance >= withdraw_amount:
            pin_enter = int(input("enter your account pin"))
            print(
                "-----------------------------------------------------------------------------------"
            )
            while pin_enter != pin:
                if pin_enter == pin:
                    print("Pin is corect and withrwall in progress")
                    balance = balance - withdraw_amount
                    print(f"withraww sucess full and your reaming balance is{balance}")

                else:
                    print("incorrect pin")
                    pin_enter = int(input("enter correct pin "))
                    attemt += 1
                    if attemt > 3:
                        print("max attempt")
        else:
            print("insufficent ammount")

    elif user == 2:
        print(f"your account balance is {balance}")

    elif user == 3:
        print(f"Your cuurent banlace in account {balance}")
        deposit_amount = int(input("enter ammountbalance deposit"))

        balance = deposit_amount + balance
        print(f"Your Updated banlace in account {balance}")

    elif user == 4:
        print("bas time paas krne aaya tha gawar")
        break
    else:
        print("enter correct choice your choie s=is incorrect")
