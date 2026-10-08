
def format_record(rec):

    if not isinstance(rec, tuple) or len(rec) != 3:
        return "неверный ввод: ожидается кортеж из 3 элементов"



    fio = rec[0].strip()
    group = rec[1].strip()
    gpa = rec[2]

    if not isinstance(fio, str):
        return "неверный ввод ФИО"
    if fio == '':
        return "ФИО не может быть пустым"
    if not isinstance(group, str):
        return "неверный ввод группы"
    if group == '':
        return "группа не может быть пустой"
    if not isinstance(gpa, (int, float)) or not (0.0 <= gpa <= 5.0):
        return "неверный ввод GPA"
    if gpa == '':
        return "GPA не может быть пустым"

    fio_parts = fio.split()
    if len(fio_parts) < 2:
        return "ФИО должно содержать как минимум фамилию и имя"

    initials = ""
    for name in fio_parts[1:]:
        initials += name[0].upper() + "."

    fio_result = surname = fio_parts[0][0].upper() + fio_parts[0][1:].lower() + " " + initials

    return f"{fio_result}, гр. {group}, GPA {gpa:.2f}"


print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
print(format_record(("Петров", "IKBO-12", 5.0)))
print(format_record(("", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр", "", 5.0)))
print(format_record(("Петров Пётр", "IKBO-12", 35.0)))
