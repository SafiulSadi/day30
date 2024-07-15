# # 36 reconnaissance
#
# n, d = map(int, input().split())
# arr = list(map(int, input().split()))
# brr = sorted(arr)
# # # print(brr)
# # brr.append(-100)
# # print(brr)
# count = 0
# for i in range(len(brr)):
#
#     for j in range(len(brr)):
#         if abs(brr[i] - brr[j]) <= d and i !=j:
#             count += 1
# # for i in range(len(brr)-1):
# #     # if brr[i + 1] != -100:
# #     x = brr[i] - brr[i + 1]
# #     if x < 0:
# #         x *= - 1
# #     if x <= d:
# #         count += 1
# print(count)
#
# z = 1
# r = 2
# # for i in range(1,count+1+1):
# #     z *= i
# #     print(f"inner count: {z}")
# # n_r = 1
# # for i in range(1,count+1-r):
# #     n_r *= i
# #     print(f"inner count n - r: {n_r}")
# # print("ans")
# # print(int(count * 2))
#
# n = int(input())
#
# while n > 0:
#     x, y = map(int, input().split())
#     if y <= -2:
#         print("NO")
#     elif y == -1:
#         print("YES")
#     elif y >= 0:
#        print("YES")
#
#
#     n -= 1
#
# c
# t = int(input())
#
# while t > 0:
#     n = int(input())
#     arr = list(map(int, input().split()))
#     brr = list(map(int, input().split()))
#     print(sum(arr))
#     print(sum(brr))
#     a = (sum(arr))
#     b = (sum(brr))
#     c = max(a, b)
#     d = min(a, b)
#     print(c)
#     print(d)
#     t -= 1
#
#
# b
#
#
# t = int(input())
#
# while t > 0:
#     a = input()
#     b = input()
#     x = []
#     l = len(a)
#     brr = [i for i in b]
#     arr = [i for i in a]
#     crr = []
#     for i in range(len(brr)):
#         # print(f"i {i} in a {a} is true: {i not in a}")
#
#         if brr[i] not in a:
#             l += 1
#             crr.append(i)
#         # print("arr")
#         # print(arr)
#         # print("brr")
#         # print(brr)
#     for i in arr:
#         if i in brr:
#             # print("i")
#             # print(i)
#             pass
#
# #     print(a in b)
#     for i in crr:
#         # print("crri")
#         # print(crr[i])
#         # print("i")
#         # print(i)
#         # print("brr")
#         # print(brr)
#         # brr.pop(i)
#         # print("brr")
#         # print(brr)
#         # i -= 1
#         x = [brr[i] for i in range(len(brr)) if i in crr]
#     #     print("XXX")
#     #     print(x)
#     # print(l)
#     # print("crr")
#     # print(crr)
#     # print("brr")
#     # print(brr)
#     print(len(arr)+len(x))
#
#
#
#     t -= 1
#
# arr = list(map(int, input().split()))
# m = max(arr)
# # print(arr)
# r = 7- m
# # print("r")
# # print(r)
# if r == 6:
#     print(f"1/1")
# elif r == 5:
#     print(f"{r}/6")
# elif r == 4:
#     print(f"2/3")
# elif r == 3:
#     print(f"1/2")
# elif r == 2:
#     print(f"1/3")
# elif r == 1:
#     print(f"1/6")
import math

# # A2oj dinks
# n = int(input())
# arr = list(map(int, input().split()))
#
# x = 0
# for i in arr:
#     x += i/100
# print((x/n)*100)
#
#
# # Lunch Rush
#
# n, k = map(int, input().split())
# arr = []
# while n > 0:
#     x = list(map(int, input().split()))
#     arr.append(x)
#
#
#     n -= 1
# # print(arr)
# fs = []
# for i in arr:
#     if k >= i[1]:
# #         print(i[0])
#         fs.append(i[0])
#     else:
#         f = i[0] - (i[1] - k)
# #         print(f"f: {i[0] - (i[1] - k)}")
#         fs.append(f)
#
# # print(fs)
# print(max(fs))
#
# # 38 watermelon
# x = int(input())
#
# if x < 4:
#     print("NO")
# elif x % 2 == 0:
#     print("YES")
# else:
#     print("NO")
#
#
# # 39 A. Taymyr is calling you
# n, m, z = map(int, input().split())
# count = 0
# arr = [i for i in range(1, z+1) if i % m == 0]
# brr = [i for i in range(1, z+1) if i % n == 0]
#
#
# for i in brr:
#     if i in arr:
#         count += 1
#
# print(count)
#
#
# # 40 Holiday Of Equality
#
# n = int(input())
# arr = list(map(int, input().split()))
# x = max(arr)
# brr = [x - i for i in arr]
# print(sum(brr))
#
# # 41 A. PolandBall and Hypothesis
# n = int(input())
#
#
# def is_prime(a):
#     if a == 1:
#         return True
#     if a == 2:
#         return True
#     if a == 3:
#         return True
#
#     if a >= 3:
#         for i in range(2, a):
#             if a % i == 0:
#                 return False
#         return True
#
#
# # a = is_prime(n)
# # print(a)
# for m in range(1, 1000):
#     x = n * m + 1
#     flag = is_prime(x)
#     if flag:
#         pass
#     else:
#         print(m)
#         break

# # 42 A. New Year and Hurry
# t = 4 * 60
# n, k = map(int, input().split())
# count = 0
# nrr = [i * 5 for i in range(1, n+1)]
# time = t - k
# for i in nrr:
#     if i <= time:
#         count += 1
#         time -= i
#
# print(count)
#
# # 43 A. Bachgold Problem
# import math
# n = int(input())
#
#
# def is_prime(a):
#     if a == 1:
#         return True
#     if a == 2:
#         return True
#     if a == 3:
#         return 3
#     elif a > 3:
#         for i in range(2, math.floor((a+1)/2)):
#             if a % i == 0:
#                 return False
#         return True
#
#
# if n % 2 == 0:
#     arr = [2 for i in range(math.floor(n / 2))]
# else:
#     arr = [2 for i in range(math.floor(n/2)-1)]
#     arr.append(3)
# # print(arr)
# x = ""
# for i in arr:
#     x += f"{i} "
# print(len(arr))
# print(x.strip())
#
# # 44 A. Compote
#
# a = int(input())
# b = int(input())
# c = int(input())
#
#
# arr = [1 for i in range(1, a + 1)]
# brr = [2 for i in range(0, b + 1, 2) if i <= b]
# if sum(brr) > b:
#     brr.pop(-1)
# crr = [4 for i in range(0, c + 1, 4) if i <= c]
# if sum(crr) > c:
#
#     crr.pop(-1)
# # for i in range(0, c + 1, 4):
# #     print(i)
# #     print(i <= c)
# # print(arr)
# # print(brr)
# # print(crr)
# w = [arr, brr, crr]
# x = min(map(len, w))
# # print(x)
# count = 0
# for i in range(x):
#     count += arr[i] + brr[i] + crr[i]
# print(count)


# # 46 Anton and Danik
#
# n = int(input())
# s = input()
# arr = []
# drr = []
# for i in s:
#     if i == "A":
#         arr.append(1)
#     else:
#         drr.append(1)
# if len(arr) > len(drr):
#     print("Anton")
# elif len(drr) > len(arr):
#     print("Danik")
# else:
#     print("Friendship")
#
#
# # 47 A. Buy a Shovel
#
# k, r = map(int, input().split())
# x = k % 10
# count = 0
# prices = []
# for i in range(0, 1000):
#     prices.append(k)
#
# # print(prices)
#
# for i in range(1, 1000):
#     x = sum(prices[:i])
# #     print("XXX")
# #     print(x)
#     count += 1
#     if x % 10 == r or x % 10 == 0:
#
#         break
# print(count)

# # 48 A. Night at the Museum
# a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 't',  's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
# arr = [i.lower() for i in a]
# brr = arr.reverse()
# print(arr)
# x = input()
# xrr = [i for i in x]
# count = 0
# pt = 0
# pt1 = 0
# pt2 = 25
# for i in xrr:
#     if i in arr:
#         distance = min(abs(pt1 - a.index(i)), abs(pt2 - a.index(i)))
#         if
#         print("Count")
#         print(count)
#         pt = arr.index(i)
#         print("pt")
#         print(pt)
#
# print(count)
#

# # 48 A. Night at the Museum
# arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 't',  's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
# brr = [i for i in arr]
# brr.reverse()
# print(brr)
# pointer = 0
# pointer_a = 0
# pointer_b = 0
# x = input()
#
# distance1 = 0
# distance2 = 0
# count = 0
# for i in x:
#     if i in arr:
#
#         distance1 = abs(pointer_a - arr.index(i))
#         print("distance1")
#         print(distance1)
#         pointer_a = arr.index(i)
#         print("pointer a")
#         print(pointer_a)
#     if i in brr:
#         distance2 = abs(pointer_b - brr.index(i))
#         print("distance2")
#         print(distance2)
#         print("pointer n")
#         print(pointer_b)
#
#     count += min(distance1, distance2)
#     print("count")
#     print(count)
# print("total count")
# print(count)


# # 49 A. The New Year: Meeting Friends
#
# arr = list(map(int, input().split()))
# distances = [abs(i- arr[0]) + abs(i- arr[1]) + abs(i- arr[2]) for i in range(0, 101)]
# # print(distances)
# print(min(distances))
#
# # 50 A. One-dimensional Japanese Crossword
#
# n = int(input())
# s = input()
# g = 0
# c = 0
# arr = [i for i in s]
# grr = []
# crr = []
# for i in arr:
#
#     if i == "B":
#         crr.append("B")
#         # print(crr)
#     if len(crr) > 0 and i == "W":
#         grr.append(crr)
#         crr = []
# if len(crr) > 0:
#     grr.append(crr)
#
# # print(grr)
#
# print(len(grr))
# xrr = [len(i) for i in grr]
# abc = ""
# for i in xrr:
#     abc += f"{i} "
#
# print(abc.strip())
#

# # 51 A. Crazy Computer
# t, d = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.append(0)
# xs = []
# count = 0
# for i in range(len(arr)-1):
#     count += 1
#     if abs(arr[i + 1] - arr[i]) > d:
#         # print("count inside")
#         # print(count)
#         xs.append(count)
#         count = 0
# # print(count)
#
# if d >= arr[-2]:
#     print(len(arr)-1)
# else:
#     print(xs[-1])
#
#
# # contest
# # a
# import math
# t = int(input())
# while t > 0:
#     n, k = map(int, input().split())
#     time = 0
#     for i in range(1, n+1):
#         time += k
#
#     time -= k
#     time +=1
#     print(time)
#     t -= 1
#
# b

# brr = sorted(arr)
# coin = 0
# for i in range(len(arr)):
#     x = abs(arr[i] - brr[i])
#     if abs(arr[i] - brr[i]) > 0:
#         coin += x
# import math
# t = int(input())
# while t > 0:
#     n = int(input())
#     arr = list(map(int, input().split()))
#     arr.append(100000)
#     brr = sorted(arr)
#     coin = 0
#     for i in range(len(arr)-1):
#         if arr[i+1] - arr[i] < 0:
#             coin += abs(arr[i+1] - arr[i])
#             print(coin)
    # for i in range(len(arr)):
    #     m = abs(arr[i] - brr[i])
    #     if m < 0:
    #         coin += m

    # print(coin)
    # t -= 1

n = int(input())
xrr = []
while n > 0:
    arr = list(input().split())
    xrr.append(arr)
    n -= 1
# print(xrr)
flag = "NO"
for i in xrr:
    if int(i[1]) > int(i[2]) and int(i[1]) >= 2400:
        flag = "YES"
print(flag)



















