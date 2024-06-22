# a, b, c, d =map(int, input().split())
# count = 0
# arrs = [a, b, c, d]
# arr = sorted(arrs)
# for i in range(3):
#     if arr[i] == arr[i+1]:
#         count += 1
# print(count)

# x = input()
# a = set()
# for i in x:
#     a.add(i)
# if len(a) % 2 == 1:
#     print(("IGNORE HIM!"))
# else:
#     print(("CHAT WITH HER!"))
a, b = map(int, input().split())
count = 0
if a >= b:
    max = a
else:
    max = b
for i in range(0, max + 1):
    for j in range(0, max + 1):
        if (i ** 2 + j) == a and (i + j ** 2) == b:
            count += 1

print(count)