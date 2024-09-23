#Получить строку
#Предобработка строки
#- Привести строку к одному регистру (например, к нижнему), чтобы сравнение было нечувствительно к регистру.
#- Удалить из строки все пробелы и знаки препинания, чтобы учитывать только буквы и цифры.
#Определить длину строки. Найти длину очищенной версии строки.
#Сравнение символов
#-Использовать цикл, чтобы сравнить символы с начала и с конца строки.
#- Перебрать символы до середины строки. Если длина строки четная, то до середины включительно, если нечетная — то до середины, не включая центральный символ.
#- Если символы на соответствующих позициях не совпадают, строка не является палиндромом.
#- Если все проверенные символы совпадают, строка является палиндромом.
# - Вернуть результат (истина или ложь).

import string


def is_palindrome(s):
    # Приводим строку к нижнему регистру
    s = s.lower()

    # Удаляем пробелы и знаки препинания
    s = ''.join(filter(lambda char: char in string.ascii_lowercase + string.digits, s))

    # Определяем длину строки
    length = len(s)

    # Сравниваем символы с начала и с конца
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            return False

    # Если все символы совпадают
    return True
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("Racecar"))
print(is_palindrome("а роза упала на лапу Азора"))
print(is_palindrome("Hello, World!"))