# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они
# сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество
# журавликов, а Катя сделала в два раза больше журавликов, чем
# Петя и Сережа вместе? Пример:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

S = int(input('Введите количество сделанных журавликов: '))

a = S // 6
b = S % 6

print(f"Петя сделал {a} журавлика")
print(f"Серёжа сделал {a} журавлика")
print(f"Катя сделала {a*4} журавлика")
if b != 0:
    print(f"Кто-то сделал еще {b} журавлика")
