#
# # # KeyError
# # a_dictionary = {"key":"value"}
# # value = a_dictionary["non_existant_key"]
#
# # # IndexError
# # fruit_list = ["Apple", "Banana", "Pear"]
# # fruit_list[3]
#
# # # TypeError
# # a = "abc"
# # print(a + 5)
#
# # FileNotFound
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["snadf"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"that key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
# print("error")
# # the problem that needs to be solved are iftar problem and perfect permutation.
# # need to look more into the buet exam for the chance to study there and mainly getting the hall facilities.
#
#
# #
# height = float(input("Height: "))
# weight = int(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters.")
#
# bmi = weight / height ** 2
# print(bmi)
# this is after the quota war
# n = int(input())
# arr = [1, 2, 3, 4, 5]
# # count = 0
#
# if n % 5 == 0:
#     count += n//5
# else:
#     count += n//5 + 1
# print(int(count))
#
#

# this is imoirtamt


# c, n, w = map(int, input().split())
# cost = 0
# crr = []
# for i in range(1, w+1):
#     cost += c*i
#     crr.append(cost)
#
# ans = cost - n
# if ans < 0:
#     print(0)
# else:
#     print(cost-n)
# w = input()
# x = input()
#
# srr = set()
# xrr = [i.lower() for i in x]
# for i in xrr:
#     srr.add(i)
# if len(srr) == 26:
#     print("YES")
# else:
#     print("NO")
#
# n, m = map(int, input().split())
# a = 1
# arr = [i for i in range(1, n+1) if i % 3 == 0]
# print(arr)
# for i in range(0, n):
#     for j in range(0, m):
#         if (i % 2 == 0):
#             print(f"#",end=" ")
#         else:
#             if j == 0:
#                 if i in arr:
#                     print("#", end=" ")
#                 else:
#                     print("-", end=" ")
#             elif j == m - 1 and a == 1 and i not in arr:
#                 print("#", end=" ")
#             else:
#                 print(f"-", end=" ")
#     if a == 0:
#         a = 1
#     else:
#         a = 0
#     print()
#     print(i in arr)

#
# # n, m = map(int, input().split())
# n, m = map(int, input().split())
# row = ""
# lrow = "#"
# rrow = ""
# for i in range(m):
#     row += "#"
# for i in range(m-1):
#     lrow += "."
#     rrow += "."
# rrow += "#"
# flag = True
#
# for i in range(n):
#     if i % 2 == 0:
#         print(row)
#     elif i % 2 != 0:
#         if flag:
#             print(rrow)
#             flag = False
#         else:
#             print(lrow)
#             flag = True
#

# n = int(input())
# arr = [1 for i in range(n)]
# brr = [1 for _ in range(n)]
# crr = [arr]
#
# for i in range(n-1):
#     ar = [1]
#     crr.append(ar)
# # print(crr)
# for i in range(1, n):
#     for j in range(1, n):
#         x = crr[i-1][j] + crr[i][j-1]
#         crr[i].append(x)
# # print(crr)
# print(crr[-1][-1])
# xrr = input().split(", ")
# if xrr[0] == "{}":
#     print(0)
# else:
#     # print(xrr)
#     start = xrr[0]
#     end = xrr[-1]
#     xrr[0] = start[1]
#     xrr[-1] = end[-2]
# #     print(start[1])
# #     print(end[-2])
# #     print(xrr)
#     srr = set()
#     for i in xrr:
#         srr.add(i)
#     print(len(srr))
# def minus(x):
#
#     return 5 - int(x)
#
#
# n, k = map(int, input().split())
# arr = list(map(minus, input().split()))
# brr = [i-k for i in arr]
# count = 0
# for i in brr:
#     if i >= 0:
#         count += 1
# print(count//3)
#
# xrr = list(map(int, input().split()))
# s = input()
# arr = [int(i) for i in s]
# brr = []
# for i in arr:
#     z = xrr[i-1]
#     brr.append(z)
# print(sum(brr))
#
# n = int(input())
# arr = list(map(int, input().split()))
# u = 0
# c = 0
# p = 0
# for i in arr:
#     if i > 0:
#         p += i
#     else:
#         c += 1
#         if p > 0:
#             p -= 1
#         else:
#             u += 1
# print(u)
# x = 4//2
# y = 5 ** 3
# name = "samiul islam"
# srr = set()
# arr = [i+"abc" for i in name if i == "s" or i == "m"]
# for i in arr:
#     srr.add(i)
# print(srr)
# print(arr)
# for i in range(0, x):
#     print(i)
# print(f"This is a number: {x}")
# print(y)
#
# def bst(brr, start, end, x):
#     mid = (start + end)//2
#     if start > end:
#         print(-1)
#         return -1
#     if brr[mid] == x:
#         print(mid)
#         return mid
#     elif brr[mid] > x:
#         end = mid - 1
#         bst(brr, start, end, x)
#
#     elif brr[mid] < x:
#         start = mid + 1
#         bst(brr, start, end, x)

#
# # Binary search implementation
# arr = [1, 2, 4, 6, 8, 9, 10, 15, 28, 36]
#
# left = 0
# right = len(arr)
# ans = 36

# print(bst(brr=arr, start=left, end=right, x=ans))
#
# print()

# implementation of bubble sort
#
#
# def bubble_sort(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - i - 1):
#             if array[j] > array[j + 1]:
#                 temp = array[j]
#                 array[j] = array[j + 1]
#                 array[j + 1] = temp
#     return array
#
#
# arr = [5, 6, 1, 7, 50, 17, 20, 64, 23]
# print(arr)
# print(bubble_sort(array=arr))

#
# s, d = 0, 0
# n = int(input())
# arr = list(map(int, input().split()))
# player = [0, 0]
# i = 0
# while len(arr) > 0:
#
#     mx = max(arr[0], arr[-1])
#     # print(arr)
#     if mx == arr[0]:
#         player[i] += mx
#         arr.pop(0)
#         i += 1
#         i %= 2
#     elif mx == arr[-1]:
#         player[i] += mx
#         arr.pop(-1)
#         i += 1
#         i %= 2
#
# print(f"{player[0]} {player[1]}")

#
# arr = []
# for i in range(5):
#     n = list(map(int, input().split()))
#     arr.append(n)
# index_i = 0
# index_j = 0
# # print(arr)
# for i in range(len(arr)):
#     for j in range(5):
#         if arr[i][j] == 1:
#             index_i = i
#             index_j = j
#             break
# # print(index_i)
# # print(index_j)
# move1 = abs(index_i - 2) + abs(index_j - 2)
# print(move1)

#
# nb = input()
# n = input()
# arr = [i for i in n]
# # print(arr)
# count = 0
# cur = arr[0]
#
# for i in range(len(arr)-1):
#     prev = arr[i]
#     next = arr[i+1]
# #     print(cur)
# #     print(next)
# #     print(prev)
#     if cur != next:
#         cur = next
#     elif cur == next:
#         count += 1
#
#
# print(count)

#
# n = int(input())
# arr = []
# ans = 0
# for i in range(n):
#     x = input()
#     for i in x:
#         if i == "+":
#             ans += 1
#             break
#
#             # print("+")
#         elif i == "-":
#             ans -= 1
#             break
#             # print("-")
#
# print(ans)
#
# n = input()
# arr = [i for i in n]
#
# arr[0] = arr[0].upper()
# s = ""
# for i in arr:
#     s += i
# print(s)
# arr = list(map(int, input().split("+")))
# brr = sorted(arr)
# ans = f"{brr[0]}"
# for i in range(1, len(brr)):
#     ans += f"+{brr[i]}"
# print(ans)
#
# w1, h1, w2, h2 = map(int, input().split())
# low = w1 + 2 * h1 + 2
# hi = w2 + 2 * h2 + 2
# total = hi + low
# # print(low)
# # print(hi)
# if w1 != w2:
#     total += abs(w1 - w2)
# print(total)
#
#
# n = int(input())
# if n == 0:
#     print(0)
# elif n == 2:
#     print(2)
# else:
#     print(1)

# n = int(input())
# arr = []
# pos = 0
# neg = 0
# while n > 0:
#     x = list(map(int, input().split()))
#     arr.append(x)
#     n -= 1
# for i in range(len(arr)):
#     if arr[i][0] <= 0:
#         neg += 1
#     else:
#         pos += 1
# if pos > 1 and neg > 1:
#     print("NO")
# else:
#     print("YES")
# #
# a, b = map(int, input().split())
# count = 0
# while not (a > b):
#     a *= 3
#     b *= 2
#     count += 1
# # print(count)
# diction = {
#     "Tetrahedron": 4,
#     "Cube": 6,
#     "Octahedron": 8,
#     "Dodecahedron": 12,
#     "Icosahedron": 20
# }
# n = int(input())
# side = 0
# while n > 0:
#     x = input()
#     side += diction[x]
#     n -= 1
# # print(diction["Octahedron"])
# print(side)
#
# n, k = map(int, input().split())
# 
# div = n // k
# rem = n % k
# if(div % 2 == 1):
#     print("YES")
# else:
#     print("NO")
#
# x = input()
# x = x.lower()
# jest = {"1", "a", "e", "i", "o", "u", "3", "5", "7", "9"}
# arr = [i for i in x if i in jest]
# print(len(arr))
#
# t = int(input())
#
# while t > 0:
#     n = int(input())
#     s = input()
#     arr = [i for i in s]
#     ans = ""
#     if arr[n - 1] == "1":
#         for i in range(n):
#             ans += "1"
#     else:
#         for i in range(n):
#             ans += "0"
#     print(ans)
#     t -= 1

#
# t = int(input())
#
# while t > 0:
#     n = int(input())
#     if n % 2 == 0:
#         print("YES")
#     else:
#         print("NO")
#
#     t -= 1
# arr = list(map(int, input().split()))
# m = max(arr)
# arr.pop(arr.index(max(arr)))
# # print(arr)
# brr = []
# for i in range(len(arr)):
#     x = m - arr[i]
#     brr.append(x)
# ans = ""
# for i in brr:
#     ans += f" {i}"
# print(ans.strip())
# #
# s = input()
# arr = [i for i in s if i == "a"]
# brr = [i for i in s if i != "a"]
# # print(arr)
# if len(arr) > len(brr):
#     print(len(s))
# else:
#     print(len(arr) * 2 - 1)
#
# y = input()
# year = int(y) + 1
# year = str(year)
# # print(year)
# arr = {i for i in year}
# while len(arr) != 4:
#     year = int(year) + 1
#     year = str(year)
#     arr = {int(i) for i in year}
# print(year)
# arr = list(map(int, input().split()))
# # print(arr)
# m = min(arr[0], arr[2], arr[3])
# arr[0] = arr[0] - m
# arr[2] = arr[2] - m
# arr[3] = arr[3] - m
# n = min(arr[0], arr[1])
# print(m * 256 + n * 32)
#
# t = int(input())
#
# while t > 0:
#     n = int(input())
#     x = input()
#     count = 0
#     arr = [i for i in x]
#     a = arr.count("A")
#     b = arr.count("B")
#     c = arr.count("C")
#     d = arr.count("D")
#     if a <= n:
#         count += a
#     else:
#         count += n
#     if b <= n:
#         count += b
#     else:
#         count += n
#     if c <= n:
#         count += c
#     else:
#         count += n
#     if d <= n:
#         count += d
#     else:
#         count += n
#
#     print(count)
#     t -= 1
# #
# import math
# from typing import List
#
# t = int(input())
#
# while t > 0:
#     n, k = map(int, input().split())
#     count = 0
#     arr: list[int] = list(map(int, input().split()))
#     x = max(arr)
#     brr = [i + 4 for i in arr]
#     y = max(brr)
#     for i in range(len(arr)):
#         while x % arr[i] != 0:
#             x += 1
#     for i in range(len(brr)):
#         while y % brr[i] != 0:
#             y += 1
#     print(x)
#     print(y)
#     print("lcm")
#     print(math.lcm(x, y))
#     t -= 1


def swap(a, b):
    temp = a
    a = b
    b = a


t = int(input())

while t > 0:
    n = int(input())
    arr = list(map(int, input().split()))
    brr = []
    for i in range(0, len(arr)):
        if arr[i] % 2 == 0:
            brr.append(arr[i])
    for i in range(0, len(arr)):
        if arr[i] % 2 == 1:
            brr.append(arr[i])
    ans = f"{brr[0]} "
    for i in range(1, len(brr)):
        ans += f" {brr[i]}"
    print(ans)
    t -= 1


