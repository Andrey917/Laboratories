"""
Число Армстронга - це таке натуральне число, яке дорівнює сумі своїх цифр, зведених в ступінь, рівну кількості його
цифр. Знайти всі такі числа від 1 до n, де n вводиться на вимогу з клавіатури.
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


number = int_request('Enter n number > 0: ')

def arm(num):
    num_sum = 0
    x = len(str(num))
    while num:
        num_sum += (num % 10) ** x
        num //= 10
    return num_sum


for num in range(0, number):
    if num == arm(num):
        print(num)