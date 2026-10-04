#email = campusx@gmail.com
#pass = 1234


print("----------------Login Ceredential ----------------------------")
username = input("Enter Your Username: ")
if "@" in username:
    password = input("Enter Your Password: ")

    if username == 'campusx@gmail.com' and password == '1234':
        print("Welcome!!")

    elif username == 'campusx@gmail.com' and password != '1234':
        print("Incorrect pasword")
        password = input("Enter Correct paswword")

        if password == '1234':
            print("You Got it!!")

        else:
            print("Fir se Galat bo raha hai!!")

    else:
        print("incorrect Login!!")
    
else:
    print("Email galat bol raha hai sale  ")




