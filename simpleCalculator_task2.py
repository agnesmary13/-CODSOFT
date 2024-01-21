def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Cannot divide by zero."
history = []
while True:
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. History\n6. Exit")
    d = int(input("Choose the operation to perform (1, 2, 3, 4, 5, 6): "))

    if d == 6:
        print("Exiting the calculator.")
        break

    if d == 5:
        print("\n--- Calculation History ---")
        for entry in history:
            print(entry)
        print("---------------------------\n")
        continue

    if d in (1, 2, 3, 4):
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

        if d == 1:
            result = add(a, b)
        elif d == 2:
            result = sub(a, b)
        elif d == 3:
            result = multiply(a, b)
        elif d == 4:
            result = division(a, b)

        history.append(f"{a} {'+' if d == 1 else '-' if d == 2 else '*' if d == 3 else '/'} {b} = {result}")
        print("Result:", result)

    else:
        print("Invalid operation. Please choose a valid option.")
