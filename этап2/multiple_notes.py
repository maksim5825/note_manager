create_note = input("Добро пожаловать в Менеджер заметок! Вы можете добавить новую заметку.\n"
                    "(для продолжения нажмите 'enter')")
from datetime import datetime
def personal():
    username = input("Введите ваше имя:")  # имя пользователя
    name = print(f"меня зовут {username}!")
    content = input("Введите описание заметки:")
def status():
    status_new = {1: "выполнено"}  # сделал словарь
    print("текущий статус заметки:", status_new[1])  # вывел текущий статус заметки
    write_status = int(input("Выберите новый статус заметки:\n 1.выполнено\n 2.не выполнено\n 3.в процессе"))
    print("Ваш выбор:", write_status)  # дал пользователю выбор статуса заметки
    if write_status == 1:  # создал условие при котором в зависимости от выбора меняется статус заметки
        status_new[1] = "выполнено"
        print("Статус заметки успешно обновлён на: выполнено")
    elif write_status == 2:
        status_new[1] = "не выполнено"
        print("Статус заметки успешно обновлён на: не выполнено")
    elif write_status == 3:
        status_new[1] = "в процессе"
        print("Статус заметки успешно обновлён на: в процессе")
def data():
    current_data = datetime.now().date()
    print('текущая дата:', current_data.strftime("%d-%m-%Y"))
    issue_date = input("Введите дату дедлайна (в формате день-месяц-год): \n")  # дата истечения заметки
    dedline = datetime.strptime(issue_date, "%d-%m-%Y").date()
    if current_data > dedline:
        period = current_data - dedline
        print("делайн истек {} дня назад".format(period.days))
    elif current_data.day == dedline.day and current_data.month == dedline.month and current_data.year == dedline.year:
        print("дедлайн истечет сегодня")
    else:
        period = dedline - current_data
        print("делайн истечёт через {} дня".format(period.days))
def titles():
    sp_title = []
    while len(sp_title) >= 0:
        title = input(
            "Введите заголовок (или оставьте пустым для завершения)")  # здесь пользователь вводит свои заголовки
        if len(title) >= 1:  # добавили условие при котором ,если кол-во индексов слова больше 1 ,слово будет доб-ся в список
            sp_title.append(title)
        elif len(
                title) < 1:  # иначе , если кол-во символов меньше 1 т.е. пустой ввод, программа завершиться и выведет нам список
            break
personal()
# status()
# data()
# titles()


# list={} #это словарь где будут хранится все заметки
# for i  in range(1,50):
#     list[f"заметка №{str(i)}"] = input()