num1 = int(input("Enter first number: "))
num2 = int(input("Enter Second number: "))
operation = int(input("Enter 1 for addition\n"
                      "Enter 2 for Subtraction\n"
                      "Enter 3 for multiplication\n"
                      "Enter 4 for division\n"))


def arithmetic(op):
    switcher = {
         1: "Addition of two numbers is: " + str(num1 + num2),
         2: "Subtraction of two numbers is: " + str(abs(num1 - num2)),
         3: "Multiplication of two numbers is: " + str(num1 * num2),
         4: "Division of two numbers is: " + str(round(num1 / num2, 3))
    }
    print(switcher.get(op, "invalid operation\n"))


arithmetic(operation)




