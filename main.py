"""
1 уровень:
1) Паша очень любит кататься на общественном транспорте,
а получая билет, сразу проверяет, счастливый ли ему попался.
Билет считается счастливым, если сумма первых трех цифр совпадает с
суммой последних трех цифр номера билета.
Программа должна выводить “Счастливый” или “Обычный”.  (Решить с помощью индексов строк, то есть без математики)
2) Дана последовательность символов. Проверить, является ли она палиндромом (слово или текст, одинаково читающееся в обоих направлениях)
3) Написать функцию проверки email (представьте, что для своего сайта эту функцию пишете. Сделать проверки, которые считаете нужными, а я буду пробовать сломать)
4) Определить количество слов в строке.
Вводится строка, состоящая из слов, разделенных пробелами.
Требуется посчитать количество слов в ней.

2 уровень:
1) Определить сложность пароля (сделать функцию как на обычных сайтах. То есть проверять большие буквы, символы, цифры И так далее. Подсказка: ascii)
2) Необходимо написать программу, которая сможет посчитать повторяющиеся символы и вывести сокращенную строку, пример:
Вход: s = 'aaaabbcaa'
Выход: 'a4b2c1a2'
3) На основании предоставленного отрывка текста определить 3 наиболее часто встречаемых символа в нем.
Пробелы нужно игнорировать (не учитывать при подсчете).
Для выведения результатов вычислений требуется написать функцию top3(st).
Итог работы функции представить в виде строки: «символ – количество раз, символ – количество раз…».
4) Дмитрий считает, что когда текст пишут в скобках (как вот тут, например), его читать не нужно.
Вот и надумал он существенно укоротить время чтения, написав функцию, которая будет удалять все, что расположено внутри скобок.

УРОВЕНЬ ПСиИииХ : (https://media3.giphy.com/media/1guRIRKAgaEOneVda2Q/giphy.gif?cid=ecf05e4776fhaulj9ulwy8eyhtbnbnh3757ndyj30s0yula9&rid=giphy.gif&ct=g)
1) Взять из сообщения ниже (там html код таблицы с CoinGecko (https://www.coingecko.com/ru) ~5.5к строк)
2) засунуть этот код в переменную (просто скопировать и засунуть в переменную с помощью тройных кавычек)
3) Вывести все названия криптовалют, которые есть в этом коде (по сути первая страница coingecko - топ 100)
P.S. - не пытайтесь читать код coingecko. Откройте консоль разработчика и найдите закономерности
Подсказка: возле каждого названия криптовалюты есть классы "py-0 coin-name cg-sticky-col cg-sticky-third-col px-0" ориентируйтесь на них, когда будете парсить
"""
import string
import re

from pipe import where
from itertools import groupby
from coingecko_html import html


#region Level 3.
# Выполнение уровня 3 взято из старого решения.
def start_level3():
    coin_names = list()
    selector = 'py-0 coin-name cg-sticky-col cg-sticky-third-col px-0'
    for s in list(html.split('\n')):
        if selector in s:
            re_string = re.search(r'data-sort="\w+"', s)
            if re_string:
                coin_names.append(re_string.group(0))

    for coin in coin_names:
        print(coin[11:-1])

    print(len(coin_names))
#endregion


#region Level 2.
def strip_brackets_text(text: str) -> str:
    new_str: str = text
    left_index: int = new_str.index('(')
    right_index: int = new_str.index(')')
    del_string: str = ''
    for c in range(left_index, right_index + 1):
        del_string += new_str[c]
    new_str = new_str.replace(del_string, '')

    return new_str


def top3(text: str) -> dict:
    chars_count: dict = {}
    for s in text.strip():
        for c in s:
            if c in chars_count:
                chars_count[c] += 1
            else:
                chars_count[c] = 1

    counts = list(x for x in chars_count.values())
    counts = sorted(counts)
    top3_counts = counts[-3:]

    top3_chars: dict = {}
    for i in top3_counts:
        top3_chars[
            list(chars_count.keys())
            [
                list(chars_count.values()).index(i)
            ]
        ] = i

    return top3_chars


def short_string(text: str) -> str:
    new_string: str = ''
    for key, group in groupby(text):
        new_string += f'{key}{len(list(group))}'

    return new_string


def check_password(pwd: str) -> int:
    protection_checker = {
        'lowercase': False,
        'uppercase': False,
        'digits': False,
        'special_symbols': False
    }
    for c in pwd:
        if c in string.ascii_lowercase:
            protection_checker['lowercase'] = True
        if c in string.ascii_uppercase:
            protection_checker['uppercase'] = True
        if c in string.digits:
            protection_checker['digits'] = True
        if c in string.punctuation:
            protection_checker['special_symbols'] = True

    return sum(protection_checker.values() | where (lambda x: x == True))


def start_level2():
    password: str = input('Enter the password: ')
    result: int = check_password(password)
    match result:
        case 0:
            print(f'Password {password} doesn\'t protected!')
        case 1:
            print(f'Password {password} protected so simple')
        case 2:
            print(f'Password {password} has easy protection')
        case 3:
            print(f'Password {password} has good protection')
        case 4:
            print(f'Password {password} has perfect protection!')

    text: str = input('Enter string: ')
    print(f'Short string for {text} is {short_string(text)}')

    text = input('Enter the text: ')
    print(f'There are top-3 chars in the text: {top3(text)}')

    text = input('Enter the text with brackets: ')
    print(f'Text without brackets string is: {strip_brackets_text(text)}')

#endregion


#region Level 1.
def count_words(text: str) -> int:
    return len(text.lower().split())


def check_email(email: str) -> bool:
    return '@gmail.com' in email


def check_palindrome(word: str) -> bool:
    reverse_word: str = word[-1::-1]
    for i in range(len(word)):
        if word[i] != reverse_word[i]:
            return False

    return True


def check_bill(bill: str) -> bool:
    left_part: list = []
    right_part: list = []
    for i in range(0, 3):
        left_part.append(int(bill[i]))
    for i in range(3, 6):
        right_part.append(int(bill[i]))

    return sum(left_part) == sum(right_part)


def start_level1():
    bill: str = input('Enter 6 digits for bill: ')
    if check_bill(bill):
        print(f'{bill} is LUCKY!')
    else:
        print(f'{bill} is not lucky =(')

    word: str = input('Enter the word: ')
    if check_palindrome(word):
        print(f'{word} is palindrome!')
    else:
        print(f'{word} is not palindrome =(')

    text: str = input('Enter the text separated by space: ')
    count = count_words(text)
    print(f'There is {count} words in the text')

    email: str = input('Enter e-mail: ')
    if check_email(email):
        print(f'{email} is valid!')
    else:
        print(f'{email} is not valid =(')
#endregion


def main():
    # Uncomment to start specify level.
    # start_level1()
    # start_level2()
    start_level3()


if __name__ == '__main__':
    main()