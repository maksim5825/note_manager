username=input("Введите ваше имя:") #имя пользователя
name=f"меня зовут {username}!"
content=input("Введите описание заметки:")          #описание заметки
status=input("Введите статус заметки:") #статус заметки
created_date=input("Введите дату создания заметки") # дата создания заметки
issue_date=input("Введите дату истечения заметки")  # дата истечения заметки
title1=input("Введите заголовок заметки:") #заголовок заметки
title2=input("Введите заголовок заметки :") #заголовок заметки
title3=input("Введите заголовок заметки :") #заголовок заметки
title4=input("Введите заголовок заметки4:") #заголовок заметки
title=[title1 , title2 , title3 , title4]
note_list1={"имя пользователя" : name,
            "описание заметки" : content,
            "статус заметки" : status,
            "дата создания заметки" : created_date,
            "дата истечения заметки" : issue_date,
            "заголовок заметки" : title}
print(note_list1)