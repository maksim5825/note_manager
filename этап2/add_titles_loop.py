sp = []
while len(sp) >= 0:
    title = input("Введите заголовок (или оставьте пустым для завершения)") #заголовок заметки
    if len(title) >= 1 :
        sp.append(title)
    else:
        len(title) < 1
        break
print('заголовок:' , *sp, sep = "\n-" )
