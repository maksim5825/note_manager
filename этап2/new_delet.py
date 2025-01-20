print("Добро пожаловать в Менеджер заметок! Вы можете добавить новую заметку.")
list = []
while 1 > 0:
    username=input("Введите ваше имя:") #имя пользователя
    content=input("Введите описание заметки:")          #описание заметки
    status=input("Введите статус заметки:") #статус заметки
    created_date=input("Введите дату создания заметки (в формате день-месяц-год):") # дата создания заметки
    issue_date=input("Введите дедлайн (в формате день-месяц-год):")  # дата дедлайна
    title=input("Введите заголовок заметки:") #заголовок заметки
    zaproc = input("Хотите добавить ещё одну заметку? (да/нет):")
    note_list = {"имя пользователя": username,
                 "описание заметки": content,
                 "статус заметки": status,
                 "дата создания заметки": created_date,
                 "дата истечения заметки": issue_date,
                 "заголовок заметки": title}
    if zaproc == "да":
        for i in range(1,11):
            list[0:11] ={"имя пользователя": username,
                 "описание заметки": content,
                 "статус заметки": status,
                 "дата создания заметки": created_date,
                 "дата истечения заметки": issue_date,
                 "заголовок заметки": title}
            print(list[2])
        list.append(note_list)
        continue
    else:
        for i in note_list :
            print(i,note_list[i])
        list.append(note_list)

    break
