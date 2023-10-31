def add(n1, n2):
    return n1+n2

def multiply(n1, n2):
    return n1*n2

def subtract(n1, n2):
    return n1-n2

def divide(n1, n2):
    return n1/n2

operations = {
    "+": add,
    "*": multiply,
    "-": subtract,
    "/": divide
}

def calculator():
    num1 = int(input("First number: "))

    for operator in operations:
        print(operator)

    end_of_calculation = False
    while not end_of_calculation:

        operator = input("Choose an operator: ")

        num2 = int(input("Next number: "))

        operation_function = operations[operator]
        ans = operation_function(num1, num2)
        print(f"{num1} {operator} {num2} = {ans}")
        

        again = input(f"Continue calculating with {ans}? [y/n/q] ").lower()
        if again == 'y':
            num1 = ans
        elif again == 'n':
            end_of_calculation = True
            calculator()
        elif again == 'q':
            end_of_calculation = True
        else:
            print("Invalid input!")
            end_of_calculation = True

calculator()