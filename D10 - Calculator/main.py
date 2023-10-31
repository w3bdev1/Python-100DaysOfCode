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

num1 = int(input("First number: "))

for operator in operations:
    print(operator)

operator = input("Choose one of the above operators: ")

num2 = int(input("Second number: "))

operation_function = operations[operator]
ans = operation_function(num1, num2)

print(f"{num1} {operator} {num2} = {ans}")

operator = input("Choose one of the above operators: ")

num3 = int(input("Third number: "))

operation_function = operations[operator]
new_ans = operation_function(ans, num3)

print(f"{ans} {operator} {num3} = {new_ans}")