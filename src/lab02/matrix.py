# # 1
# def transpose(mat):
#     if mat == []:
#         return []
    
#     k = len(mat[0])
#     for x in mat:
#         if len(x) != k:
#             return 'ValueError'

#     res = []
#     for i in range(k):
#         r = []
#         for j in range(len(mat)):
#             r.append(mat[j][i])
#         res.append(r)
#     return res

# print(transpose([[1, 2, 3]]))
# print(transpose([[1], [2], [3]]))
# print(transpose([[1, 2], [3, 4]]))
# print(transpose([]))
# print(transpose([[1, 2], [3]]))


# # 2
# def row_sums(mat):
#     if mat == []:
#         return []
    
#     k = len(mat[0])
#     for x in mat:
#         if len(x) != k:
#             return 'ValueError'

#     res = []
#     for x in mat:
#         res.append(sum(x))
#     return res

# print(row_sums([[1, 2, 3], [4, 5, 6]]))
# print(row_sums([[-1, 1], [10, -10]]))
# print(row_sums([[0, 0], [0, 0]]))
# print(row_sums([[1, 2], [3]]))

# 3
def col_sums(mat):

    k = len(mat[0])
    for x in mat:
        if len(x) != k:
            return 'ValueError'

    res = []
    for i in range(k):
        t = 0
        for j in range(len(mat)):
            t += mat[j][i]
        res.append(t)
    return res


print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))

