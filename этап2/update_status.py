status = {1: "выполнено"}  # сделал словарь
print("текущий статус заметки:", status[1])  # вывел текущий статус заметки
while True:
    write_status = int(input("Выберите новый статус заметки:\n 1.выполнено\n 2.не выполнено\n 3.в процессе"))
    print("Ваш выбор:", write_status)  # дал пользователю выбор статуса заметки
    if write_status == 1:  # создал условие при котором в зависимости от выбора меняется статус заметки
        status[1] = "выполнено"
        print("Статус заметки успешно обновлён на: выполнено")
        break
    elif write_status == 2:
        status[1] = "не выполнено"
        print("Статус заметки успешно обновлён на: не выполнено")
        break
    elif write_status == 3:
        status[1] = "в процессе"
        print("Статус заметки успешно обновлён на: в процессе")
        break
    elif write_status != 3 and write_status != 2 and write_status != 1:
        print("такого варианта не существует, попробуйте снова")

print("текущий статус заметки:", status[1])  # проверил выбранный статус

