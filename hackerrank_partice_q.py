# #  Q1-- Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# # Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line

# if __name__ == "__main__":
#     student_name = [
#         ["Harry", 37.21],
#         ["Berry", 37.21],
#         ["Tina", 37.2],
#         ["Akriti", 41],
#         ["Harsh", 39],
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


# # # Q2 ---  The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

# student = {
#     "aman": [23, 45, 6, 7, 78],
#     "abhay": [
#         34,
#         56,
#         7,
#         7,
#         887,
#     ],
# }

# name = input()
# marks = []
# add = 0

# for i in student[name]:
#     add = add + i
#     marks.append(i)

# count = len(marks)
# avg = add / count
# print(f"{avg:.2f}")


# # Q3 -- You are given a string, and you have to validate whether it's a valid Roman numeral. If it is valid, print True. Otherwise, print False. Try to create a regular expression for a valid Roman numeral.


# # roman_car = ["I","V","X","L","C","D","M"]

# # user = input()

# # for i in roman_car:
# #     if i in user:
# #         print("True")
# #     else:
# #         print("false")

# if __name__ == '__main__':
#     N = int(input())
#     N = []
#     N.insert(0,5)
#     N.insert(1,10)
#     N.insert(0,6)
#     print(N)
#     N.remove(6)
#     N.append(9)
#     N.append(1)
#     N.sort()
#     print(N)
#     N.pop()
#     N.reverse()
#     print(N)


# # Q-4 ----- Consider a list (list = []). You can perform the following commands:
# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.


# if __name__ == '__main__':
#     n = int(input())
#     my_list = []

#     for i in range(n):
#         command = input().split()

#         if command[0] == "insert":
#             my_list.insert(int(command[1]), int(command[2]))

#         elif command[0] == "print":
#             print(my_list)

#         elif command[0] == "remove":
#             my_list.remove(int(command[1]))

#         elif command[0] == "append":
#             my_list.append(int(command[1]))

#         elif command[0] == "sort":
#             my_list.sort()

#         elif command[0] == "pop":
#             my_list.pop()

#         elif command[0] == "reverse":
#             my_list.reverse()
