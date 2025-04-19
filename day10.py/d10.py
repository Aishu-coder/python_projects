from d10art import calculator_logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division
}


def calculator():
    print(calculator_logo)
    num1 = float(input("what is the first number?: "))
    for operation in operators:
        print(operation)

    continue_game = False 
    while not continue_game:
        operation_symbol = input("pick one of the operation :")
        num2 = float(input("what is the next number? :"))
        function = operators[operation_symbol]
        result = function(num1, num2)
        print(f"{num1}{operation_symbol}{num2}={result}")
        ask_to_continue = input(
            "Type 'y' to continue calculating or type 'n' to exit or 'Y' to create a new claculation :").lower()
        if ask_to_continue == 'n':
            continue_game = True
        elif ask_to_continue == 'y':
            num1 = result
        elif ask_to_continue == 'Y':
            calculator()


calculator()
