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










