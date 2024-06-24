# /a, b, c, d =map(int, input().split())
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
# # lets get our expectations up and in
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

# # 14 counting dragons
# k = int(input())
# l = int(input())
# m = int(input())
# n = int(input())
# d = int(input())
# count = 0
# for i in range(1, d+1):
#     if i % k == 0 or i % l == 0 or i % m == 0 or i % n ==0:
#         count += 1
#
# print(count)

######
# arr = []
# for i in range(n):
#     a = x % 10
#     x = math.floor(x/10)
#     # print(a)
#     arr.append(a)
# #     print(arr)
# arr.reverse()
# # print(arr)

# 15 Lucky Ticket
# n = int(input())
# x = input()
# arr = [int(i) for i in x]
# print(arr)
#
# count1 = 0
# count2 = 0
# for i in range(int(n/2)):
# #     print(arr[i])
#     count1 += arr[i]
# #     print(count1)
# for i in range(int(n/2),n):
# #     print(arr[i])
#     count2 += arr[i]
# #     print(count2)
# flag = True
# for i in arr:
#     if i != 4:
#         if i != 7:
#             flag = False
# #         print(f"flag: {flag}")
# if count1 == count2 and flag:
#     print("YES")
# else:
#     print("NO")

# # 17 Arrival of the General
# x = int(input())
# # x = "100 95 100 100 88"
# arr = list(map(int, input().split()))
# # print(arr.index(min(arr)))
# loi = arr.index(min(arr))
# hii = arr.index(max(arr))
# for i in range(len(arr)):
#     if min(arr) == arr[i]:
#         if i > loi:
#             loi = i
# for i in range(len(arr)):
#     if max(arr) == arr[i]:
#         if i < hii:
#             hii = i
#
# # print(loi)
# # print(hii)
# q = hii - 0
# w = len(arr) - loi - 1
# # print(hii)
# # print(loi)
# sec = q + w
#
# # print(sec)
# if hii > loi:
#     sec -= 1
#     pass
# # if arr[hii] == arr[loi]:
# #     sec -= 1
# # if (hii == 0 and loi == len(arr)):
# #     sec = 0
# print(sec)

# # 17 Amusing Joke
#
# x = input()
# y = input()
# z = input()
# arr = []
# brr = []
# for i in x:
#     arr.append(i)
# # print(arr)
# for i in y:
#     arr.append(i)
# # print(x)
# # print(arr)
#
# for i in z:
#     brr.append(i)
#
# crr = sorted(arr)
# # print(crr)
# drr = sorted(brr)
# flag = len(crr) == len(drr)
# # print(drr)
# # print(brr)
# for i in drr:
#     if i in crr:
#         crr.pop(crr.index(i))
# #         print("asdfshf")
# #         print(crr)
# # print(crr)
# if len(crr) == 0 and flag:
#     print("YES")
# else:
#     print("NO")

# # 18 Presents
#
# n = int(input())
# arr = list(map(int, input().split()))
# # print(arr)
# brr = []
# for i in range(len(arr)):
#     brr.append(0)
# #     print(brr)
# for i in arr:
#     brr[i-1] = arr.index(i) + 1
# #     print(i)
#
# # print(brr)
# ans = ""
# for i in brr:
#     ans += f"{str(i)} "
#
# print(ans.strip())

# # 19 Epic game
# import math
# s, a, n = map(int, input().split())
# flag = 0
# # print(f"{s} {a} {n}")
#
# while n >= 0:

#     # simon part
#     x = math.gcd(s, n)
#     n -= x
#     if n < 0:
#         flag = 1
#         break
#     else:
#         flag = 0
#     # anti simon part
#     y = math.gcd(a, n)
#     n -= y
#     if n < 0:
#         flag = 0
#         break
#     else:
#         flag = 1
#
# print(flag)

# # 20 Tram
#
# t = int(input())
# arr = []
# while t > 0:
#     a, b = map(int, input().split())
#     w =[a, b]
#     arr.append(w)
#
#     # print(w)
#
#     t -= 1
# # print([i[0] for i in arr])
# # print([i[1] for i in arr])
# x = [i[0] for i in arr]
# y = [i[1] for i in arr]
# max_person = []
# to = 0
# for i in range(len(x)):
#     t = t - x[i] + y[i]
#     max_person.append(t)
# #     print(f"t is: {t}")
#     q = y[i] - x[i]
# #     print(q)
# print(max(max_person))
#
# # 01703202018

