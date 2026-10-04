#  Q1-- Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line

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


# # Q2 ---  The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

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


# Q3 -- You are given a string, and you have to validate whether it's a valid Roman numeral. If it is valid, print True. Otherwise, print False. Try to create a regular expression for a valid Roman numeral.


# roman_car = ["I","V","X","L","C","D","M"]

# user = input()

# for i in roman_car:
#     if i in user:
#         print("True")
#     else:
#         print("false")