# # 36 reconnaissance
#
# n, d = map(int, input().split())
# arr = list(map(int, input().split()))
# brr = sorted(arr)
# # print(brr)
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
# t = int(input())
#
# while t > 0:
#     a = input()
#     b = input()
#     l = len(a)
#     brr = [i for i in b]
#     arr = [i for i in a]
#     for i in brr:
#         # print(f"i {i} in a {a} is true: {i not in a}")
#
#         if i not in a:
#             l += 1
#             arr.append(i)
#         print("arr")
#         print(arr)
#         print("brr")
#         print(brr)
#     crr = []
#     for i in arr:
#         if i in brr:
#             print("i")
#             print(i)
#
# #     print(a in b)
#     print(l)
#
#
#
#     t -= 1
#

t = int(input())

while t > 0:
    n = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    print(sum(arr))
    print(sum(brr))
    a = (sum(arr))
    b = (sum(brr))
    c = max(a, b)
    d = min(a, b)
    print(c)
    print(d)
    t -= 1



