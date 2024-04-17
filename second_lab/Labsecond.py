def power(san, darege):
    if darege == 0: #показатель степени
        return 1
    else:
        return san * power(san, darege - 1)

san = int(input("Введите основание (целое число): "))
darege = int(input("Введите показатель степени (целое число): "))

result = power(san, darege)
print(f'{san} в степени {darege} равно {result}')
