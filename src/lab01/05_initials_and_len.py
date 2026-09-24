fio = input("ФИО: ")
st = fio.split()
lst = []
cnt = 0
for x in st:
    lst.append(x[0])
    cnt += len(x)
print(f"Инициалы: {''.join(lst)}.")
print(cnt + 2)

