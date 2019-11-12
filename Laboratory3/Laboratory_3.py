"""
Вставити пробіл перед останніми 2-мя символами в слова, що мають мінімальну (задану) довжину.
"""
import re
re_integer = re.compile("^[-+]{0,1}\d+$")


def validator(pattern, promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text


def int_request(prompt):
    number = int(validator(re_integer, prompt))
    while number < 3:
        number = int(validator(re_integer, prompt))
    return number
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////


text = input('Введите текст:\n')
words = text.split()
counter = 0

lim = int_request('Insert minimum length of unchangeable words : ')

for word in words:
    if lim > len(word) > 2:
        word = word[:-2] + ' ' + word[-2:]
        print(word, end=' ')
    elif len(word) < 3 and len(word) != 0:
        print(word, end=' ')
    else:
        print(word, end=' ')
