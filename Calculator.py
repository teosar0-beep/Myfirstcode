def calculator():
    print("Простой калькулятор")
    print("Операции: +  -  *  /")

    while True:
        expr = input("Введите выражение (или 'q' для выхода): ")

        if expr.lower() == "q":
            print("Выход из калькулятора.")
            break

        try:
            result = eval(expr)   # вычисляет строку как выражение
            print("Результат:", result)
        except Exception as e:
            print("Ошибка:", e)


if __name__ == "__main__":
    calculator()
