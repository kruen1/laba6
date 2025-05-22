sequence = [3, -5, 2, -8, 7, -1, 4, -6]

first_positive = None
for num in sequence:
    if num > 0:
        first_positive = num
        break

last_negative = None
for num in reversed(sequence):
    if num < 0:
        last_negative = num
        break

print("Исходная последовательность:", sequence)
if first_positive is not None:
    print("Первый положительный элемент:", first_positive)
else:
    print("В последовательности нет положительных элементов")

if last_negative is not None:
    print("Последний отрицательный элемент:", last_negative)
else:
    print("В последовательности нет отрицательных элементов")