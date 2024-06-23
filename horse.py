# a, b, c, d =map(int, input().split())
# count = 0
# arrs = [a, b, c, d]
# arr = sorted(arrs)
# for i in range(3):
#     if arr[i] == arr[i+1]:
#         count += 1
# print(count)
import math

# x = input()
# a = set()
# for i in x:
#     a.add(i)
# if len(a) % 2 == 1:
#     print(("IGNORE HIM!"))
# else:
#     print(("CHAT WITH HER!"))
# a, b = map(int, input().split())
# count = 0
# if a >= b:
#     max = a
# else:
#     max = b
# for i in range(0, max + 1):
#     for j in range(0, max + 1):
#         if (i ** 2 + j) == a and (i + j ** 2) == b:
#             count += 1
#
# print(count)

#
# # beaver matrix
# n = int(input())
#
# row, col = (n, n)
# c = 1
# # arr = [[0 for i in range(n)] for j in range(n)]
# arr = []
#
# for i in range(n):
#     w = list(map(int, input().split()))
#     arr.append(w)
# for i in range(n):
#     for j in range(n):
#         if arr[i][j] == 0:
#             # arr[i][j] = int(input())
#             # arr[i][j] = int(input())
#             pass
#
# # adding main diagonal
# x = 0
# midrow = math.floor(n/2)
# m12 = n + n - 1
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             x += arr[i][j]
#
# for i in range(n):
#     for j in range(n):
#         if i == n - 1 - j:
#             x += arr[i][j]
#
# x -= 3 * arr[midrow][midrow]
#
# for i in range(n):
#     for j in range(n):
#         if i == midrow:
#             x += arr[i][j]
#
#
# for i in range(n):
#     for j in range(n):
#         if j == midrow:
#             x += arr[i][j]
#
# print(x)
# # for i in range(n):
# #     for j in range(n):
# #         if i == j:
# #             x += arr[i][j]
# #             print(f' array {arr[i][j]}')
# #             print(f' x {x}')
"""
n = list(map(int, input().split()))
arr = list(map(int, input().split()))
#
c = 0
if arr[n[1]] >= 0:
    for i in arr:
        if i >= arr[n[1]]:
            c += 1
            # print(f"{arr[n[1]]}  i is :{i} and  k is {n[1]} c is {c}")
    print(c)

else:
    print(0)
# """
# t = int(input())
# arr = list(map(int, input().split()))
# # print(arr)
# amazing = 0
# curhi = arr[0]
# curlo = arr[0]
# for i in arr:
#     if i > curhi:
#         amazing += 1
#         curhi = i
#     elif i < curlo:
#         amazing += 1
#         curlo = i
# print(amazing)

#
# def remove_element(arry):
#     flag = False
#     if len(arry) <= 1:
#         flag = True
#     else:
#         if arry[1] - arry[0] <= 1:
#             arry.pop(0)
#             # print(arry)
#         if len(arry) <= 1:
#             flag = True
#
#         else:
#             try:
#                 remove_element(arry)
#                 # print("NO")
#                 if len(arry) == 1:
#                     flag = True
#
#             except:
#                 if len(arry) > 1:
#                     flag = False
#
#     return flag
#
# t = int(input())
#
# while t > 0:
#     n = int(input())
#     arr = list(map(int, input().split()))
#     sorted_arr = sorted(arr)
#     x = remove_element(sorted_arr)
#     if x == True:
#         print("YES")
#     else:
#         print("NO")
#     t -=
#
# import math
# n, k, l, c, d, p, nl, np = map(int,(input().split()))
# max_lime = c * d/ n
# max_no_liquid = (k * l)/(n * nl)
# max_salt = p/(np * n)
# arr = [max_lime, max_no_liquid, max_salt ]
# # print(arr)
# print(math.floor(min(arr)))
# toast = nl + np + 1
# q = n * l

# Contest programming start
# lets get our expectations up and in
# t = int(input())
# while t > 0:
#     x = list(map(int, input().split()))
#     distances = []
#     for i in range(0, 11):
#         a = i - x[0]
#         if a < 0:
#             a *= -1
#         b = i - x[1]
#         if b < 0:
#             b *= -1
#         c = i - x[2]
#         if c < 0:
#             c *= -1
#         aw = [a, b, c]
#         distances.append(aw)
#
#
#     smallest = []
#     for i in distances:
#         z = sum(i)
#         smallest.append(z)
#
#     print(min(smallest))
#     t -= 1

# 14 counting dragons
k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
count = 0
for i in range(1, d+1):
    if i % k == 0 or i % l == 0 or i % m == 0 or i % n ==0:
        count += 1

print(count)