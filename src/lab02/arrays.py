# # 1
# def min_max(lst):
#     mn = 10**10
#     mx = -10**10
#     if lst:
#         for x in lst:
#             if x < mn:
#                 mn = x
#             if x > mx:
#                 mx = x
#         return (mn, mx)
#     else: return 'ValueError'

# print(min_max([3, -1, 5, 5, 0]))
# print(min_max([42]))
# print(min_max([-5, -2, -9]))
# print(min_max([]))
# print(min_max([1.5, 2, 2.0, -3.1]))


# # 2

# def uniqe_sorted(lst):
#     res = list(set(lst))

#     for i in range(len(res)):
#         for j in range(i + 1, len(res)):
#             if res[i] > res[j]:
#                 res[i], res[j] = res[j], res[i]
#     return res

# print(uniqe_sorted([3, 1, 2, 1, 3]))
# print(uniqe_sorted([]))
# print(uniqe_sorted([-1, -1, 0, 2, 2]))
# print(uniqe_sorted([1.0, 1, 2.5, 2.5, 0]))


# 3
def flatten(lst):
    res = []
    for x in lst:
        if type(x) != list and type(x) != tuple:
            return 'TypeError'

        for y in x:
            res.append(y)
    return res

print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))