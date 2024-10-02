number = input("Введите восьмизначное число: ")
if len(number) == 8 and number.isdigit():
    result = sum(int(digit) for digit in number)
    print(f"Сумма цифр числа {number} равна {result}")
else:
    print("Пожалуйста, введите корректное восьмизначное число.")