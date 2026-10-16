# print(num)


# # count = 0
# n = len(num)
# i = n -1
# # while i <= n-1:
# #     if num[::-i]%2 == 0:
# #         count += 1
# #     i +=1

# # print(count)

# # while i>=0:
# #     print(num[i],end=" ")
# #     i = i -1

# # add = 0
# # for index,nums in enumerate(num):
# #     if nums%2 == 0:
# #         add = nums + add

# #         print(f'Your Index numbers for {index}')

# # print(add)


# largest = num[0]

# for i in num:
#     if i > largest:
#         largest = i

# print(f'the largest element in list is {largest}')


# print(max(num))


# # target = int(input("enter your target number"))

# def does_taget_exist(num,target):
#     for i in num:
#         if i == target:
#             return True


#     return False

# print(does_taget_exist(num,123))
# num = [5,7,4,56,78,456,344,3,2,3]

# def avg_return(num):
#     n = len(num)
#     add = 0

#     for i in num:
#         add = add +i
#     return add/n


# print(avg_return(num))

# nums1 = [2,3,4,5,6]
# nums2 = [2,3,4,5,6]


# def return_new_list(nums1,nums2):
#     nums3 = []
#     n = len(nums1)
#     for i in range(0,n):
#         t = nums1[i]+nums2[i]
#         nums3.append(t)
#     return nums3


# print(return_new_list(nums1,nums2))


# new_list = [i * i for i in range(1, 11) if i%2 == 1]

# new_list = [i for i in range(1,21) if i%2 == 0 and i%5 == 0]
# print(new_list)

# from 1 to hundred make a list of only prime number

# print(prime_number)


# def is_prime(num):
#     factors = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             factors += 1

#     if factors == 2:
#         return True
#     return False


# prime_number = [i for i in range(1,101) if is_prime(i) == True]
# print(prime_number)

# new_list = [i*i for i in range(1,21) if i%2 ==1]
# print(new_list)

# list_1 = [23,45,45,78,76,89,54]

# new_list = [i for i in list_1 if i > 75]

# print(new_list)


# --------------------#nested list--------------------------
# matrix represnt in list as a 2d list


# 3*3

#matrix = [[2, 3, 4], [3, 4, 5], [3, 4, 5]]  # 0  # 1  # 2

# print(matrix[1][1])

# #65*75

# for i in range(0,3):
#     for j in range(0,3) print(matrix[i][j],end=" ")
#     print(


# r = len(matrix)
# c = len(matrix[0])
# for i in range(0, r):
#     for j in range(0, c):
#         if i >= j:
#             print(matrix[i][j], end=" ")
#         else:
#             print("*",end=" ")
#     print()
# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line
# if __name__ == '__main__':
#     student_name = [
#         ['Harry', 37.21],
#         ['Berry', 37.21],
#         ['Tina', 37.2],
#         ['Akriti', 41],
#         ['Harsh', 39]
#     ]

#     grades = []

#     for i in range(len(student_name)):
#         grades.append(student_name[i][1])

#     # Remove duplicates and sort
#     grades = sorted(set(grades))

#     second_lowest = grades[1]

#     name = []

#     for i in range(len(student_name)):
#         if student_name[i][1] == second_lowest:
#             name.append(student_name[i][0])

#     name.sort()

#     for i in name:
#         print(i)


# name = {
#     "ap":[2,3]
# }
# print(name["ap"][0])   



# subject1 = int(input("enter your 1st subject name :- "))
# subject2 = int(input("enter your 2nd subject name :- "))
# subject3 = int(input("enter your 3rd subject name :- "))
# total = subject1+subject2+subject3
# avg = total/3

# print(f"Your Total marks is {total}\nYour avg is {avg:.2F}")


# age = int(input("Enter Your age = "))

# if age >= 18:
#     print("you can vote")
    
# # print("you cannot vote")


# num = int(input("Enter your Number = "))

# if num == 0:
#     print(f"{num} is Zero")
# elif num < 0:
#     print(f"{num} is negative")
# elif num > 0:
#     print(f"{num} is positive")

# a = int(input("Enter Your a number = "))
# b = int(input("Enter Your b number = "))

# if a == b :
#     print("Both Are equal")
# elif a > b:
#     print(a)
    
# else:
#     print(b)

year = int(input("Enter Your Year  = "))

if (year%4 == 0 and year%100 != 0)or (year % 400 == 0) :
    print(f"{year} is a leap year") 
    
else:
    print("Not a Leap Year")
    