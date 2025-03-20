def div(a, b):
    if b == 0:
        print("Error: Cannot divide by zero")
        return None
    return a / b

def exp(a, b):
    return a ** b

def rem(a, b):
    if b == 0:
        print("Error: Cannot divide by zero")
        return None
    return a % b

def sum_range(a, b):
    if a > b:
        print("Error: Second number must be greater")
        return None
    total = 0
    for i in range(a, b+1):
        total += i
    return total

while True:
    print("\nOperations:")
    print("D - Divide")
    print("E - Exponent")
    print("R - Remainder")
    print("F - Summation")
    print("Q - Quit")

    c = input("Enter choice: ").upper()

    if c == 'Q':
        print("Bye!")
        break

    if c in ['D', 'E', 'R', 'F']:
        try:
            x = int(input("Enter first number: "))
            y = int(input("Enter second number: "))

            if c == 'D':
                res = div(x, y)
            elif c == 'E':
                res = exp(x, y)
            elif c == 'R':
                res = rem(x, y)
            elif c == 'F':
                res = sum_range(x, y)

            if res is not None:
                print("Result:", res)
        except:
            print("Invalid input")
    else:
        print("Invalid choice, try again")
