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
#
# # 21 112A - Petya and Strings
#
# a = input().lower()
# b = input().lower()
#
# arr = [i for i in a]
# brr = [i for i in b]
# # print(arr)
# # print(brr)
#
# flag = 0
# for i in range(len(arr)):
# #     print(brr[i] < arr[i])
#     if arr[i] < brr[i]:
#         flag = -1
# #         print(flag)
#         break
#     elif brr[i] < arr[i]:
#         flag = 1
# #         print(flag)
#         break
#     else:
#         continue
# print(flag)

# # 22 Nearly Lucky Number
# n = input()
#
# # arr = list(map(int, n.split()))
# arr = [int(i) for i in n]
# # print(len(n))
# # print(arr)
# count = 0
# flag = True
# for i in arr:
#     if i == 7 or i == 4:
#         # flag = True
#         count += 1
#     #         print(flag)
#     else:
#         flag = False
#         #         print(flag)
# if count == 7 or count == 4:
#     print("YES")
# else:
#     print("NO")
#
# # 23 Blackjack
#
# x = int(input())
# # x = 12
# arr = [1,1,1,1, 2,2,2,2, 3,3,3,3, 4,4,4,4, 5,5,5,5, 6,6,6,6, 7,7,7,7, 8,8,8,8, 9,9,9,9, 10,10,10,10, 10,10,10,10, 10,10,10, 10,10,10,10, 11,11,11,11]
# req = x - 10
# count = 0
# for i in arr:
#     if req == i:
#         count += 1
# # print(arr)
# # print(len(arr))
# print(count)
#

#
# # 24 Chips
#
# n, c = map(int, input().split())
# arr = [i+1 for i in range(n)]
#
#
# # print(arr)
#
#
# def reducer(arry, chip):
#     brr = []
#     for i in arry:
#         if i > chip:
#             print(chip)
#             return
#         else:
#             chip -= i
#             # brr.append(chip)
#             # print(brr)
#             # print(f"chip: {chip}")
#         if chip == 0:
#             print(0)
#             return
#     if chip > 0:
#         reducer(arry, chip)
#     # else:
#     #     return brr
#
#
# if n == 1:
#     print(0)
# else:
#     reducer(arr, c)

# # 25 Panoramix's Prediction
#
# import math
# n, m = map(int, input().split())
#
#
# # check prime:
# def check_prime(number):
#     if number == 2:
#         return True
#     elif number % 2 == 0:
#         return False
#     else:
#         for i in range(3, math.floor(number/2) + 1):
#             if number % i == 0:
#                 # print(number % i)
#                 return False
#         return True
#
# flag = check_prime(m)
# green_flag = True
# for i in range(n + 1, m):
#     a = check_prime(i)
# #     print(a)
#     if a:
#         green_flag = False
#         break
# # print(flag)
# # print(green_flag)
# if flag and green_flag:
#     print("YES")
# else:
#     print("NO")

# 26 Way Too Long Words
#
# t = int(input())
# arr = []
# while t > 0:
#     word = input()
#     if len(word) > 10:
#         a = word[0]
#         z = word[len(word)-1]
#         x = len(word) - 2
#         word = f"{a}{x}{z}"
#         print(word)
#         # arr.append(word)
#     else:
#         # arr.append(word)
#         print(word)
#
#     t -= 1
#
# # print(arr)
#

# # 27 Ultra-Fast Mathematician
# a = input()
# b = input()
# c = ""
# for i in range(len(a)):
#     if a[i] != b[i]:
#         c += "1"
#     else:
#         c += "0"
# print(c)

# # 28 Word
# word = input()
# w = word.lower()
# count = 0
# for i in range(len(word)):
#     if word[i] < w[i]:
#         # print(f"w[i]: {w[i]} word[i]{word[i]} and {w[i] < word[i]}")
#         count += 1
# #         print(count)
#     else:
#         count -= 1
# #         print(count)
# if count > 0:
#     print(word.upper())
# else:
#     print(word.lower())

#
# # 29 Domino piling
# import math
# n, m = map(int, input().split())
#
# dom = 0
# if n <= 1 and m <= 1:
#     dom = 0
# elif n < 1 or m < 1:
#     dom = 0
# elif n >= 2 and m == 1:
#     x = math.floor(n/2)
#     dom = x
# elif m >= 2 and n == 1:
#     x = math.floor(m/2)
#     dom = x
# elif n >= 2 and m >= 2:
#     if n % 2 == 0:
#         if m % 2 == 0:
#             dom = int(n/2) * m
#         else:
#             dom = (math.floor(n/2) * m)
#             # print("hello")
#             # print(math.floor(n/2))
#             # print(math.floor(n/2) * m - 1)
#             # print(m - 1)
#             # print(math.floor(m/2))
#     elif n % 2 ==1:
#
#         if m % 2 == 0:
#             dom = int(m/2) * n
#         else:
#             dom = (math.floor(n/2) * m) + math.floor(m/2)
#             # print("here")
#             # print(math.floor(n/2))
#             # print(m)
#             # print(math.floor(m/2))
#             # print(math.floor(n/2))
#
#     # elif m % 2 == 0:
#     #     if n % 2 == 0:
#     #         dom = int(m / 2) * n
#     #     else:
#     #         dom = (int(m / 2) * (n - 1)) + math.floor(n / 2)
#
# print(dom)

# # 30 Sleuth
# v = ['A', 'E', 'I', 'O', 'U', 'Y']
# arr = [i.lower() for i in v]
# # print(arr)
# arr += v
# # print(arr)
# a = input().strip()
# # print(a)
# x = a.strip("?").strip()[-1]
# flag = "NO"
# if x in arr:
#     flag = "YES"
# print(flag)

#
# Contest#
# t = int(input())
#
# while t > 0:
#     a, b = map(int, input().split())
#     x, y = map(int, input().split())
#
#     if a > b:
#         if x > y:
#             print("YES")
#         else:
#             print("NO")
#     elif b > a:
#         if y > x:
#             print("YES")
#         else:
#             print("NO")
#
#     t -= 1
#
#
# #B
# import math
# t = int(input())
#
#
# def rec(a, b, c):
#     pass
#
#
# while t > 0:
#     x, y, k = map(int, input().split())
#     # print(f"{x} Y {y} K {k}")
#     if y == 2:
#         if k == 1:
#             x = x + 1
#         else:
#             x = 1
#     else:
#
#         while k > 0:
# #             print(f"before x+=1: {x}")
#             x += 1
# #             print(f"x+=1: {x}")
#             while x % y == 0:
#                 x /= y
# #                 print(f"x /= y: {x}")
# #             print(k)
#             k -= 1
#     # print(f"ans : {math.floor(x)}")
#     print(math.floor(x))
#     t -= 1
# #
# t = int(input())
# def rec(arr, count, current):
#     for i in brr:
#         current += i
#         if (current >= l and current <= r) or current == l or current == r:
#             count += 1
#             current = 0
#             print("count")
#             print(count)
#             print("current")
#             print(current)
#     if len(arr):
#
#
#     print(brr)
#     print(count)
#
#
# while t > 0:
#
#     n, l, r = map(int, input().split())
#     arr = list(map(int, input().split()))
#     brr = [i for i in arr if i <= r]
#     count = 0
#     current = 0
#     print("Brr")
#
#     t -= 1

# # 31 Triangular Number
# import math
# n = int(input())
# arr = [math.floor(i * (i + 1) / 2) for i in range(1, n)]
# # print(arr)
# if n == 1:
#     print("YES")
# elif n > 1:
#     if n in arr:
#         print("YES")
#     else:
#         print("NO")
#
# # 32 Translation
# s = input()
# t = input()
# flag = "YES"
# if len(s) == len(t):
#
#     arr = [i for i in s]
#     # print(arr)
#     brr = [i for i in t]
# #     print(brr)
#     list.reverse(brr)
# #     print(brr)
#     for i in range(len(arr)):
#         if arr[i] != brr[i]:
#             flag = "NO"
# else:
#     flag = "NO"
#
# print(flag)
#
# # 33 Army
# n = int(input())
# arr = list(map(int, input().split()))
# # print("arr")
# # print(arr)
# brr = list(map(int, input().split()))
# # print("brr")
# # print(brr)
# brr = [i - 1 for i in brr]
# # print("brr")
# # print(brr)
# a = brr[0]
# b = brr[1]
# years = 0
#
# if a == b-1:
#     years += arr[a]
# #     print("Here: arr[b-1]")
# #     print(arr[b-1])
# elif a < b-1:
# #     print("arr[a] < arr[b-1]")
# #     print(arr[a] < arr[b-1])
# #     print("arr[b-1]")
# #     print(arr[b-1])
#     while a <= b - 1:
#         years += arr[a]
#         a += 1
# #         # print(years)
# print(years)
#
# # 34 Reconnaissance 2
# n = int(input())
# arr = list(map(int, input().split()))
# # print(arr)
# brr = [i for i in arr]
# brr.append(arr[0])
# # print(brr)
# heights = []
# for i in range(len(arr)):
#     distance = brr[i] - brr[i + 1]
#     if distance < 0:
#         distance *= -1
#     heights.append(distance)
#
# # print(heights)
# # print("heights")
# # print(min(heights))
# # print("min(heights)")
# # print(heights.index(min(heights)) + 1)
# w = heights.index(min(heights)) + 1
#
# if w > n:
#     w = 1
#     b = 2
# else:
#     w = heights.index(min(heights)) + 1
#     b = w + 1
#     if b > n:
#         b = 1
# if n != 2:
#     print(f"{w} {b}")
# else:
#     print("1 2")
#




