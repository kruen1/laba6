def count_elements(A, C):
    count = 0
    for element in A:
        if len(element) > 1 and element.startswith(C) and element.endswith(C):
            count += 1
    return count

# Пример использования
A = ["apple", "banana", "cat", "cucumber", "car", "C++", "cc", "hello"]
C = "c"

result = count_elements(A, C)
print(f"Количество элементов, которые содержат более одного символа и при этом начинаются и оканчиваются символом С -> {result}")