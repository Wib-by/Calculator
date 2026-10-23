### C A L C U L A T O R ###

# Operation Functions

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

# Interface and Operation Chassis

print("Calculator v0\n\n")

while(True):

    first = float(input("Input the first part of operation (FLOAT):\n"))

    operation = {"+", "-", "*", "/"}
    operation_choice = str(input("Input your desired operation ( + - * / ):\n"))

    if operation_choice not in operation:
        print("Are you simple? Let's try again from the beginning.\n\n")
        continue

    second = float(input("Input the second part of operation (FLOAT):\n"))

    if operation_choice == "+":
        print(add(first, second))
    elif operation_choice == "-":
        print(sub(first, second))
    elif operation_choice == "*":
        print(mul(first, second))
    elif operation_choice == "/":
        print(div(first, second))
    else:
        print("I literally don't have any idea how you reached this.")
