
#создаём список , где будут храниться все заметки
list_note = []

def note(): #функция где создаем заметки
    from datetime import datetime
    username = input("Введите ваше имя:")  # имя пользователя
    content = input("Введите описание заметки:")  # описание заметки
    status = input("Введите статус заметки:")  # статус заметки
    title = input("Введите заголовок заметки:")  # заголовок заметки
    current_data = datetime.now().date()
    current_data_true = current_data.strftime("%d-%m-%Y")
    issue_date = input("Введите дату дедлайна (в формате день-месяц-год): \n")  # дата истечения заметки
    dedline = datetime.strptime(issue_date, "%d-%m-%Y").date()
    deadline_true = dedline.strftime("%d-%m-%Y")
    note = {                                 #создаем словарь для заметки
        'имя пользователя:': username,
        'заголовок заметки:': title,
        'описание заметки:': content,
        'статус заметки:': status,
        'дата создания заметки:': current_data_true,
        'дедлайн:': deadline_true
    }
    list_note.append(note)  #добавляем заметку в список

def print_note(): # функция для вывода всех заметок
    if not list_note:
        print("Заметок нет)")
        return
    for i, note in enumerate(list_note, 1):
        print(f"\n{i}. имя пользователя: {note['имя пользователя:']}")
        print(f"   заголовок заметки: {note['заголовок заметки:']}")
        print(f"   описание заметки: {note['описание заметки:']}")
        print(f"   статус заметки: {note['статус заметки:']}")
        print(f"   Дата создания: {note['дата создания заметки:']}")
        print(f"   Дедлайн: {note['дедлайн:']}")

def program():
    print("Добро пожаловать в Менеджер заметок! Вы можете добавить новую заметку.")
    while 1 > 0:
        note()  #создаем заметку
        zaproc = input("\nХотите добавить ещё одну заметку? (да/нет): ")
        if zaproc != "да":
            break
    print_note()
program()