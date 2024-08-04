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

def bst(brr, start, end, x):
    mid = (start + end)//2
    if start > end:
        print(-1)
        return -1
    if brr[mid] == x:
        print(mid)
        return mid
    elif brr[mid] > x:
        end = mid - 1
        bst(brr, start, end, x)

    elif brr[mid] < x:
        start = mid + 1
        bst(brr, start, end, x)

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







