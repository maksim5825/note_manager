#задание1

# x = -2
# if x > 0 :
#     y = "y = sin^2x"
# else:
#     y = "y = 1-2sin(x^2)"
# print(y)

#задание2
# x = 2
# y = 3
# if y < 0 or x < 0 :
#     print("точка не попадает в указанные области ")
# elif y > 0 and x < 4 :
#     print("точка попадает в обасть 1")
# elif y > 0 and x > 4 :
#     print("точка попадает в область 2")
# else:
#     print("точка не попадает в указанные области")

#задание3
# x = 2
# y = 3
# if x > y :
#     print("х больше чем у")
# else:
#     print("у больше чем х")

#задание4
# x = 2
# y = 3
# if x > y :
#     print(f"{x} максимальное число")
# else:
#     print(f"{y} максимальное число")

#задание5
# m = 42
# n =2
# if m%n == 0 :
#     s = m//n
#     print(s)
# else:
#     print("m на n нацело не делится")

#задание6
# m = 42
# n =2
# if m%n == 0 :
#     s = m//n
#     print("n является делителем m")
# else:
#     print("n не является делителем m")

#задание7
# m =16
# if m%2 == 0:
#     print("число m четное")
# elif m%2 != 0:
#     print("число m не четное")
# if m%10 == 7:
#     print("число m оканчивается  цифрой 7")
# else:
#     print("число m не оканчивается  цифрой 7")

#задание8
# m = 88
# if m//10 == m%10:
#     print("1 и 2 число одинаковы")
# elif m//10 > m%10:
#     print("1 число больше 2")
# elif m//10 < m%10:
#     print("1 число меньше 2")

#задание9
# m = 48
# a = m//10
# b = m%10
# c = (a**3 + b**3)*4
# if m**2 == c:
#     print("ответ положительный")
# else:
#     print("ответ отрицательный")

#задание10
# m = 56
# a = m//10
# b = m%10
# if a+b > 10:
#     print("сумма цифр числа двузначная")
# else:
#     print("сумма цифр не двузначная ")
# if a+b > m:
#     print("сумма цифр больше числа ")
# else:
#     print("сумма цифр меньше числа ")

#задание11
# m =18
# a = 6
# c = m//10
# b = m%10
# z = c+b
# if m%3 == 0:
#     print("число m кратно 3")
# elif m%3 != 0:
#     print("число m не кратно 3")
# if z%a ==0:
#     print("число m кратно a")
# elif z%a !=0:
#     print("число m не кратно a")

#задание11
# m =185
# a1 = m//100
# b2 = (m%100)//10
# c3 = m%10
# if a1 > c3:
#     print("первая цифра большее третий ")
# else:
#     print("первая цифра меньше третий  ")
# if a1 > b2:
#     print("первая цифра большее второй ")
# else:
#     print("первая цифра меньше второй  ")
# if b2 > c3:
#     print("вторая цифра большее третий ")
# else:
#     print("вторая цифра меньше третий  ")

#задание12
# m =185
# a1 = m//100
# b2 = (m%100)//10
# c3 = m%10
# if a1*3 + b2*3 + c3*3 == m*2:
#     print("YES")
# else:
#     print("NO")

#задание13
# m = 550
# p = 29
# a = m//100
# b = (m%100)//10
# c = m%10
# if a+b+c > 10:
#     print("сумма цифр числа двузначная")
# else:
#     print("сумма цифр не двузначная ")
# if a*b*c > 99:
#     print("произведение цифр числа трехзначное")
# else:
#     print("произведение цифр числа не трехзначное ")
# if a*b*c > p:
#     print("произведение цифр числа больше числа Р")
# else:
#     print("произведение цифр числа меньше числа Р ")
# if (a+b+c)%5 == 0:
#     print(" сумма цифр числа кратна 5")
# else:
#     print("произведение цифр числа не кратна 5 ")

#задание14
# m = 124
# a = m//100
# b = (m%100)//10
# c = m%10
# if a == b and b ==c :
#     print("все цифры одинаковы")
# elif a == b or b ==c :
#     print("есть одинаковые цифры")
# else:
#     print("одинаковых цифр нет")

#задание15
# m = 1212
# a = m//1000
# b = (m//100)%10
# c = (m//10)%10
# d = m%10
# g = 32
# if a+b == c+d:
#     print("сумма первых и последних цифр равна")
# else:
#     print("сумма первых и последних цифр не равна")
# if (a+b+c+d)%3 == 0:
#     print("сумма  цифр кратна 3")
# else:
#     print("сумма  цифр не кратна 3")
# if (a*b*c*d)%4 == 0:
#     print("произведение цифр кратна 4")
# else:
#     print("произведение цифр не кратна 4")
# if (a*b*c*d)%g == 0:
#     print("произведение цифр кратна g")
# else:
#     print("произведение цифр не кратна g")

#задание16
# n = 27
# b = n%10
# if b%2 == 0:
#     print("число заканчивается четной цифрой")
# else:
#     print("число заканчивается нечетной цифрой")

#задание17
# n=9 #минута
# cikl = n%5
# if cikl <= 3 :
#     print("горит зеленый")
# elif cikl >3 and cikl <= 5 :
#     print("горит красный")

#задание18
# m = int(input("введите число:"))
# if m >= -5 and m <= 3 :
#     print("число входит в промежуток(-5:3)")
# else:
#     print("число не входит в промежуток(-5:3)")

#задание18
# m = float(input("введите число:"))
# if m >= -2.4 and m <= 5.7:
#     fm = m**2
#     print(fm)
# else:
#     print("fm = 4")

#задание19
# a = 2
# b = 3
# c =4
# if a < b < c :
#     print("неравенство выполняется")
# else:
#     print("неравенство не выполняется")
# if b > a > c :
#     print("неравенство выполняется")
# else:
#     print("неравенство не выполняется")

#задание20
# a = 15
# b = 16
# if a%b == 0 or b%a == 0:
#     print("Да, одно из чисел является делителем другого")
# else:
#     print("Нет, ни одно из чисел не является делителем другого")

# сделал не все задания , они почти одинаковые , проверьте пожалуйста то что есть
