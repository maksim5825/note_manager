username=input("Введите ваше имя:") #имя пользователя
print(f"меня зовут {username}!")

title=input("Введите заголовок заметки:") #заголовок заметки
title2=input("Введите заголовок заметки 2:") #заголовок заметки 2
title3=input("Введите заголовок заметки 3:") #заголовок заметки 3
title4=input("Введите заголовок заметки 4:") #заголовок заметки 4
string=[title , title2 , title3 , title4]
print(string)

content=input("Введите описание заметки:")          #описание заметки
content2=input("Введите описание заметки 2:")          #описание заметки2
content3=input("Введите описание заметки 3:")          #описание заметки3
content4=input("Введите описание заметки 4:")          #описание заметки4
content_string=[content , content2 , content3 , content4]
print(content_string)

status=input("Введите статус заметки:") #статус заметки
status2=input("Введите статус заметки 2:") #статус заметки 2
status3=input("Введите статус заметки 3:") #статус заметки 3
status4=input("Введите статус заметки 4:") #статус заметки 4
status_string=[status , status2 , status3 , status4]
print(status_string)

created_date=input("Введите дату создания заметки") # дата создания заметки
created_date2=input("Введите дату создания заметки 2") # дата создания заметки2
created_date3=input("Введите дату создания заметки 3") # дата создания заметки3
created_date4=input("Введите дату создания заметки 4") # дата создания заметки4
created_date_spring=[created_date , created_date2 , created_date3 , created_date4]
print(f"дата создания заметки: {created_date_spring[0:6]}")

issue_date=input("Введите дату истечения заметки")  # дата истечения заметки
issue_date2=input("Введите дату истечения заметки 2")  # дата истечения заметки 2
issue_date3=input("Введите дату истечения заметки 3")  # дата истечения заметки3
issue_date4=input("Введите дату истечения заметки 4")  # дата истечения заметки4
issue_date_spring=[issue_date , issue_date2 , issue_date3 , issue_date4]
print(f"дата истечения заметки: {issue_date_spring[0:6]}")
