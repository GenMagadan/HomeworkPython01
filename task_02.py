# Найдите сумму цифр трехзначного числа. Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# Вариант 1
# a = int(input('Введите трехзначное число: '))

# if a > 99 and a < 1000:
#     sum = int(a // 100 + (a // 10) % 10 + a % 10)
#     print(f"{a} -> {a // 100} + {(a // 10) % 10} + {a % 10} = {sum}")
#    #  можно обойтись одной строчкой, но получается слишком массивно
# else:
#     print('Вы ввели не трехзначное число')

# Вариант 2
a = input('Введите трехзначное число: ')

if len(a) == 3:
    sum = int(a[0]) + int(a[1]) + int(a[2])
    print(f"{a} -> {int(a[0])} + {int(a[1])} + {int(a[2])} = {sum}")
  #  можно обойтись одной строчкой, но получается слишком массивно
else:
    print('Вы ввели не трехзначное число')