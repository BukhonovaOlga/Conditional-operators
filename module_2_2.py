from os import times_result

first = input("Введите первое число: ")
second = input("Введите второе число: ")
third = input("Введите третье число: ")

if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
elif first != second and second != third and first != third:
    print(0)


