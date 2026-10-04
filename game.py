import random
import sys

attemt = 0
guss_number = random.randint(0,5)

user_guese = int(input("Enter Your Guess Number : "))


while user_guese != guss_number:
    if guss_number>user_guese:
        print("Think Larger")
    else:
        print("Think Lower")
    user_guese = int(input("Enter Your Guess Number : "))

    attemt = attemt + 1
     
print("shi jawab")
print("You took",attemt,"attempt")
print("The System Prediction",guss_number)
        

