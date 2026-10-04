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


#--------------------#nested list--------------------------
 #matrix represnt in list as a 2d list








