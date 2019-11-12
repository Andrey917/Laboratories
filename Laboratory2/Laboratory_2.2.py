"""
Дано ціле число N(>0). Якщо воно є ступенем числа 3, то вивести True, якщо ні - вивести False.
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
    while number <= 0:
        number = int(validator(re_integer, prompt))
    return number


N = int_request('Enter number N to check: ')
while N > 2:
    N = N / 3
if N == 1:
    print(True)
else:
    print(False)
