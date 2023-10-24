"""Task 5
Вводиться з клавіатури користувачем текст. Знайти в ньому найдовше слово та вивести його на екран.
"""
import string
txt = input("input text: ")
for item in string.punctuation:
    if item in txt:
        txt = txt.replace(item, " ")
txt = txt.split()
res = []
for i in txt:
    if len(i) > len(res):
        res = i
print(res)
