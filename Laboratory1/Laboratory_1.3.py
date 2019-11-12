"""
Обчислення функції, в залежності від введеного значення х
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
    return number


x = int_request('Insert x to operate : ')
Function1 = (-3*x+9)            # if x>3
Function2 = (x**3/(x**2+8))     # if x<=3
if x > 3:
   print(Function1)
else:
   print(Function2)
