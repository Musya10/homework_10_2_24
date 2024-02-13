"""Task1
Користувач вводить три цифри з клавіатури. Залежно від вибору користувача програма виводить
на екран максимум з трьох, мінімум іх трьох або середноарифметичне трьох чисел"""

n1 = int(input("Enter first digit number"))
n2 = int(input("Enter second digit number"))
n3 = int(input("Enter third digit number"))

c1 = int(input("Choice what you want "
               "Enter 1 Maximum of three numbers. "
               "Enter 2 Minimum of three numbers. "
               "Enter 3 Arithmetic mean of thee numbers: "))

if 0 < c1 < 2:
    print(f"Maximum: {max(n1, n2, n3)}")
elif 1 < c1 < 3:
    print(f"Minimum: {min(n1, n2, n3)}")
elif 2 < c1 < 4:
    print(f"Arifmetic mean: {(n1 + n2 + n3) / 3}")
else:
    print("Incorrect choice")