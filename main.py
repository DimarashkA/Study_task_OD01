def is_palindrome(s):
    # 1. Преобразуем строку в нижний регистр, чтобы сравнение не было чувствительным к регистру.
    s = s.lower()

    # 2. Удаляем все пробелы и неалфавитно-цифровые символы из строки, оставляя только буквы и цифры.
    s = ''.join(char for char in s if char.isalnum())

    # 3. Определяем начало и конец строки.
    left, right = 0, len(s) - 1

    # 4. Пока начало меньше или равно концу
    while left <= right:
        # 4.1. Сравниваем символы на текущих позициях.
        if s[left] != s[right]:
            # Если они не равны, то строка не палиндром.
            return False
        # 4.2. Перемещаем индексы к центру.
        left += 1
        right -= 1

    # 5. Если дошли до этой точки, значит все парные символы равны, и строка - палиндром.
    return True

# Пример использования функции:
example_string = "A man, a plan, a canal, Panama"
print(is_palindrome(example_string))  # Вывод: True

example_string = "A mans, a plans, a canals, Panama"
print(is_palindrome(example_string))  # Вывод: False