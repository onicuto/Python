def ch(x):
    try:
        x = float(x)
        return True
    except ValueError:
        return False


a = input("Введите первое число:")
if not ch(a):
    print("Необходимо ввести число.")
    exit(1)
else:
    a = float(a)

b = input("Введите второе число:")
if not ch(b):
    print("Необходимо ввести число.")
    exit(1)
else:
    b = float(b)

print("""Выберите операцию 
       1. -
       2. +
       3. /
       4. *
       5. **""")
c = int(input())
if c == 1:
    print(
        f"{int(a) if a.is_integer() else a}",
        " - ",
        f"{int(b) if b.is_integer() else b}",
        " = ",
        a - b,
    )
elif c == 2:
    print(
        f"{int(a) if a.is_integer() else a}",
        " + ",
        f"{int(b) if b.is_integer() else b}",
        " = ",
        a + b,
    )
elif c == 3:
    if b == 0:
        print("На ноль делить нельзя")
    else:
        print(
            f"{int(a) if a.is_integer() else a}",
            " / ",
            f"{int(b) if b.is_integer() else b}",
            " = ",
            a / b,
        )
elif c == 4:
    print(
        f"{int(a) if a.is_integer() else a}",
        " * ",
        f"{int(b) if b.is_integer() else b}",
        " = ",
        a * b,
    )
elif c == 5:
    print(
        f"{int(a) if a.is_integer() else a}",
        " ** ",
        f"{int(b) if b.is_integer() else b}",
        " = ",
        a**b,
    )
