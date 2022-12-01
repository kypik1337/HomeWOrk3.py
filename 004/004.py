summ = ""
peremen = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
while peremen != 0:
    summ = str(peremen % 2) + summ
    peremen //=2
print(summ)