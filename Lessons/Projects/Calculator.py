print("Введите первое число:")
a = float(input())
print("Введите второе число:")
b = float(input())
print("""Выберите операцию 
       1. -
       2. +
       3. /
       4. *
       5. **""")
c = int(input())
if c == 1:
    print(a, " - ", b, " = ", a - b)
elif c == 2:
    print(a, " + ", b, " = ", a + b)
elif c == 3:
    print(a, " / ", b, " = ", a / b)
elif c == 4:
    print(a, " * ", b, " = ", a * b)
elif c == 5:
    print(a, " ** ", b, " = ", a**b)
