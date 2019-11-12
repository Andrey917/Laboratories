"""
Знайти суму
"""""
import re

re_integer = re.compile("^[-+]{0,1}\d+$")

def validator(pattern, promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text


def int_request(prompt):
    number = int(validator(re_integer, prompt))
    return number


n = int_request()
x = int_request()
i = 1
result = 0
while i != n + 1:
    res = (x + i) ** 2
    result = result + res
    i += 1
print(result)
