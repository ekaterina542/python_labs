st = input('in:')

ind1 = 0
ind2 = 0
for i in range(len(st)):
    if st[i] in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        ind1 = i
        break

for y in range(len(st)):
    if st[y] in '01234567890':
        ind2 = y + 1
        break

shag = ind2 - ind1

s = ''

for n in range(ind1, len(st), shag):
    if st[n] != '.':
        s += st[n]
    else:
        s += '.'
        break

print(s)

