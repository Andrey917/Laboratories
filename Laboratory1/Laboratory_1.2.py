"""
Визначити правильність дати, введеної з клавіатури (число - від 1 до 31, місяць - від 1 до 12.  Якщо введені некоректні
дані, то повідомити про це.
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


month = int_request('Enter number of month to check : ')
day = int_request('Enter number of day to check: ')

if month >= 1 and month <= 12:
    print("Месяц существует :", month, "- ый")
if month < 1 or month > 12:
    print("Ошибка. Введён неправильный месяц")
if day >= 1 and day <= 31:
   print("День существует :", day, "- ый")
if day < 1 or day > 31:
    print("Ошибка. Введён неправильный день")


