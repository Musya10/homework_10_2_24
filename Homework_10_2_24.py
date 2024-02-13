"""Task2
Користувач вводить з клавіатури кількість метрів.
Залежно від вибору користувача програма переводть метри в милі, дюйми чи ярди"""
m1 = int(input("Enter the lenght in meters: "))
c1 = int(input("Choice what you want to transfer metters to: "
               "Enter 1 in miles. "
               "Enter 2 in inches. "
               "Enter 3 in yards: "))
m2 = m1 / 1609
m3 = m1 * 39.37
m4 = m1 * 1.094
if 0 < c1 < 2:
    print(f"Miles: {m2}")
elif 1 < c1 < 3:
    print(f"Inches: {m3}")
elif 2 < c1 < 4:
    print(f"Yards: {m4}")
else:
    print("Incorrect choice")