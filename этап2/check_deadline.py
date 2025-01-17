from datetime import datetime

current_data = datetime.now().date()
print('текущая дата:', current_data.strftime("%d-%m-%Y"))


issue_date = input("Введите дату дедлайна (в формате день-месяц-год): \n")  # дата истечения заметки
dedline = datetime.strptime(issue_date , "%d-%m-%Y").date()



if current_data > dedline:
    period = current_data - dedline
    print("делайн истек {} дня назад".format(period.days))
elif current_data.day == dedline.day and current_data.month == dedline.month and current_data.year == dedline.year:
    print("дедлайн истечет сегодня")
else:
    period = dedline - current_data
    print("делайн истечёт через {} дня".format(period.days))
