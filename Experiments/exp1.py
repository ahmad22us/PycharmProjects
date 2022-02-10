# d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
# d_hello = d['k1'][2]['k2'][1]['tough'][2]
# print(d_hello)
##################################################
# a = "pizaz is here"
# b = a.split()
# print(f"b = {b}")
# c = b.reverse()
# print (b)
# print(c)
#################################################
# start = 11
# end = 25
# is_p = True
# for i in range(start, end + 1):
#     for k in range(2, i):
#         if i % k == 0:
#             is_p = False
#             break
#         else:
#             is_p = True
#     if is_p:
#         print(f"i = {i}")
# **************************************************
# def show():
#     for x in range(21, 22, 23):
#         print(x)
#
# show()
# **************************************************
# num = int(input())
#
# for _ in range(num):
#     name = input()
#     evn_str = ''
#     odd_str = ''
#     for i in range(0, len(name)):
#         if i % 2 == 0:
#             evn_str += name[i]
#         else:
#             odd_str += name[i]
#
#     print(f"{evn_str} {odd_str}")
# ***************************************************
# def diagonalDifference(arr):
#     # i = 0
#     # k = 0
#     ar1 = 0
#     # l = 0
#     # m = len(arr) - 1
#     ar2 = 0
#     # for _ in range(len(arr)):
#     #     print(arr[i][k])
#     #     ar1 += arr[i][k]
#     #     i += 1
#     #     k += 1
#     # for _ in range(len(arr)):
#     #     print(arr[l][m])
#     #     ar2 += arr[l][m]
#     #     l += 1
#     #     m -= 1
#     # return abs(ar1 - ar2)
#     n = len(arr)
#     ar1 = sum([arr[x][x] for x in range(n)])
#     ar2 = sum([arr[x][n - 1 - x] for x in range(n)])
#     return abs(ar1 - ar2)
#
#
# n = int(input().strip())
#
# arr = []
#
# for _ in range(n):
#     arr.append(list(map(int, input().rstrip().split())))
#
# result = diagonalDifference(arr)
# print(result)
# ********************************************************
# def miniMaxSum(arr):
#     temp_arr = []
#     t_sum = 0
#     a_sum = 0
#     for i in range(0, len(arr)):
#         t_sum = sum(arr)
#         a_sum = t_sum - arr[i]
#         temp_arr.append(a_sum)
#     print(str(min(temp_arr)) + ' ' + str(max(temp_arr)))
#
# if __name__ == '__main__':
#
#     arr = list(map(int, input().rstrip().split()))
#
#     miniMaxSum(arr)
# *************************************************************
# arr = [1, 2, 5, 6, 6]
# count = 0
# max_val = max(arr)
#
# for ar in arr:
#     if ar == max_val:
#         count += 1
#
# print(count)
# ***********************************************************
# str1 = "helloworld"
# str2 = str1[::-1]
# print(str1[::-1])
# print(str2)
# **********************************************************
# def staircase(n):
#     for i in range(1,n+1):
#         print(' '*(n-i)+'#'*(i))
#
# if __name__ == '__main__':
#     n = int(input().strip())
#
#     staircase(n)
# ************************************

# def kangaroo(x1, v1, x2, v2):
#     if (x1 + v1) == (x2 + v2):
#         return "YES"
#     elif (x2 > x1) and (v2 > v1):
#         return "NO"
#     elif (x2 > x1) and (v2 < v1):
#         return "YES"
#
#
# result = kangaroo(0, 2, 5, 3)
# print(result)
#########################################
# def unpack(p, q, r, s):
#     print(p+q)
#
# a = [1, 2, 3, 4]
# unpack(a, a, a, a)
##############################
# for i in range(1, 5):
#     for j in range(i, 6):
#         print(" ", end=" ")
#     for k in range(1, i):
#         print("*", end=" ")
#     for l in range(0, i):
#         print("*", end=" ")
#     print("\n")
# for i in range(1, 6):
#     for j in range(0, i):
#         print(" ", end=" ")
#     for k in range(i, 5):
#         print("*", end=" ")
#     for l in range(i, 6):
#         print("*", end=" ")
#     print("\n")
###########################################
# numbers = [1, 2, 3]
# #new_list = []
# # for n in numbers:
# #     add_1 = n + 1
# #     new_list.append(add_1)
# new_list = [n+1 for n in numbers]
# print(new_list)
############################################

# def solution(A):
#     small = 1
#     A.sort()
#     for i in range(0, len(A)):
#         if A[i] == small:
#             small += 1
#     return small
#
#
# A = [1, 2, 3]
# print(solution(A))
##########################################
# numbers = [1,2,3,4,5,6,7]
# number_list=[]
#
# for num in numbers:
#     number_list.append(num*2)
# print(number_list)
############################################
# my_list = [25.28, 33.49, 42.18, 63.68, 98.25, 82.53, 66.78, 90.56, 28.41, 8.91, 58.37, 87.67, 35.08, 23.43, 92.01, 90.05, 92.33, 92.68, 52.74, 0.55]
# total = 0
# for index in range(len(my_list)):
#     total += my_list[index]
# print(round(total, 2))
###########################################
# my_string = 'abdullah'
# for i in range(len(my_string)):
#     my_string[i].upper()
# print(my_string)
#
# my_numbers = [5, 4, 3, 1, 9]
# my_numbers.sort()
# print(my_numbers)
############################################
# s = list((23, )*4)
# print(s)
#################################
# def add(a, b):
#     return a + 5, b + 5
#
#
# print(add(3, 2))
###################################
i = 2
for i in range(i < 2):
    i = i + 3
print(i)
