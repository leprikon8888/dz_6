"""Task 3
Напишіть скрипт, який обчислює суму всіх кодів символів рядка."""
string = input("input strig: ")
res = 0
for i in string:
    res += ord(i)
print(res)