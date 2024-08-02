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

n = int(input())
arr = [1 for i in range(n)]
brr = [1 for _ in range(n)]
crr = [arr]

for i in range(n-1):
    ar = [1]
    crr.append(ar)
# print(crr)
for i in range(1, n):
    for j in range(1, n):
        x = crr[i-1][j] + crr[i][j-1]
        crr[i].append(x)
# print(crr)
print(crr[-1][-1])
