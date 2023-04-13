#Calculator
from art.calculator_art import logo
import os

os.system('cls')

#Add
def add(n1, n2):
    return n1 + n2


#Subtract
def subtract(n1, n2):
    return n1 - n2


#Mulitply
def multiply(n1, n2):
    return n1 * n2


#Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


#calculator function
def calculator():
    os.system('cls')
    print(logo)

    operation_list = "(+ - * /)"
    keep_running = True

    num1 = float(input("What´s the first number?: "))

    operation_symbol = input(f"\nPick an operation {operation_list}: ")

    while operation_symbol != "+" and operation_symbol != "-" and operation_symbol != "*" and operation_symbol != "/":
        print("You must enter an operation symbol from the list")
        operation_symbol = input(f"\nPick an operation {operation_list}: ")

    while keep_running:
        num2 = float(input("\nWhat´s the next number?: "))
        calc_function = operations[operation_symbol]
        answer = calc_function(num1, num2)

        print(f"\n{num1} {operation_symbol} {num2} = {answer}")
        operation_symbol = input(f"\nTo continue type another operation {operation_list} or 'any key' to restart: "        )
        num1 = answer
        if operation_symbol != "+" and operation_symbol != "-" and operation_symbol != "*" and operation_symbol != "/":
            calculator()


calculator()
