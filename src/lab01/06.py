n = int(input())
lst = []
for i in range(n):
    a = input()
    i, f, v, form = a.split()
    lst.append(form)

o = 0
zo = 0
for x in lst:
    if x == 'True': o += 1
    else: zo += 1
    
print(o, zo)
