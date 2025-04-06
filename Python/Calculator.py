def add(x,y):
    return x + y
def minus(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    if y == 0:
        return "Error! You can't return x / divide by zero"
    return x / y

def calc():
    print("Select operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    op = input()
    if op > "4":
        print("Wrong Selection")
        calc()

    print("Enter 1st number")
    num1 = int(input())
    print("Enter 2nd number")
    num2 = int(input())


    if op == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")

    elif op == '2':
        print(f"{num1} - {num2} = {minus(num1, num2)}")

    elif op == '3':
        print(f"{num1} * {num2} = {mul(num1, num2)}")

    elif op == '4':
        print(f"{num1} / {num2} = {div(num1, num2)}")


calc()