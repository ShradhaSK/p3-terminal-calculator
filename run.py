# FIX FORMATTING FUNCTION.

# Define global variables.
num1 = 0
num2 = 0
result = 'N/A'
num_format = ''
valid = True
memory = []
# Define an 'operators' list (if modified, update the 'user_help()' function).
operators = ['+', '-', '*', '/', '%', 'A', '**', '//']


# Define a 'value-formatting' function (display '.0' floats as integers).
def format_num(x):
    """
    formatting numbers so that '.0' floating point numbers are displayed as integers
    """
    global num_format
    try:
        x = '{:,}'.format(x)
        if x.endswith('.0'):
            num_format = x[:-2]
    except ValueError:
        pass
    return num_format


class Operations:
    """
    A class to store operations performed for memory function
    """
    def __init__(self, value1, operator, value2, answer):
        self.value1 = value1
        self.operator = operator
        self.value2 = value2
        self.answer = answer



def past_results():
    """
    Function to list previous 10 operations
    """
    global memory, num1
    print('\nPrevious operations:'
          '\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    if len(memory) == 0:
        print('None')
    while len(memory) > 10:
        memory.pop(0)
    for m in memory:
        print('>', m.value1, m.operator, m.value2, '=', m.answer)
    print('\nContinue your operation'
          '\nYour first value is ───→', num1)


def num_validation(num):
    """
    Function to check if the user entered number is other than whole number or decimal
    """
    global valid
    number = ''
    while valid:
        try:
            number = float(input(num + ': '))
            break
        except ValueError:
            print('\nInvalid input (numbers and decimal points only).')
    return number



def operator_validation():
    """
    Validate user entered operator
    """
    op = input('\nOperator: ').upper()
    while op not in operators or op.isspace():
        if op == 'H':
            user_help()
            op = input('\nOperator: ').upper()
        elif op == 'M':
            past_results()
            op = input('\nOperator: ').upper()
        elif op == 'R':
            print('\nYour calculation has been reseted.\n')
            calculate()
        else:
            print('\n► Invalid operator, try again.\n')
            op = input('Operator: ').upper()
    return op


def operation_to_perform(op):
    """
    operation to perform based on user input of operator
    """
    global num1, num2, result, memory
    while op in operators:
        try:
            if op == '+':  # ADDITION
                result = float(num1) + float(num2)
                break
            elif op == '-':  # SUBTRACTION
                result = float(num1) - float(num2)
                break
            elif op == '*':  # MULTIPLICATION
                result = float(num1) * float(num2)
                break
            elif op == '/':  # DIVISION
                result = float(num1) / float(num2)
                break
            elif op == '**':  # POWER
                result = float(num1) ** float(num2)
                break
            elif op == '//':  # ROOT
                result = float(num1) ** (1 / float(num2))
                break
            elif op == 'A':  # AVERAGE
                result = (float(num1) + float(num2)) / 2
                break
            elif op == '%':  # PERCENTAGE
                result = float(num1) * float(num2) / 100
                break
        except ArithmeticError as error:
            print('\nError:', error)
            break
    # Add the operation to the 'memory' list.
    operation = Operations(num1, op, num2, result)
    memory.append(operation)
    # Format and display result.
    print('\n──→ Result:', result, '\n'
          '\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')



def calculate():
    """calculate the result based on
    the user entered numbers and arithmetic operato
    r - main program LOOP"""
    global num1, num2, valid
    while valid:
        num1 = num_validation('\nFirst value')
        operator = operator_validation()
        num2 = num_validation('\nSecond value')
        operation_to_perform(operator)


# Define "user_help" function.
def user_help():
    global num1
    print('\nList of possible operators and their uses:'
          '\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾'
          '\n- Use [ M ] to display a list of the last 10 operations.'
          '\n- Use [ R ] to reset your calculation.'
          '\n- Use [ + ] for Addition - [Value #1] plus [Value #2].'
          '\n- Use [ - ] for Subtraction - [Value #1] minus [Value #2].'
          '\n- Use [ * ] for Multiplication - [Value #1] by [Value #2].'
          '\n- Use [ / ] for Division - [Value #1] divided by [Value #2].'
          '\n- Use [ % ] for Percentage - [Value #1] percentage of [Value #2].'
          '\n- Use [ A ] for Average - Average of [Value #1] and [Value #2].'
          '\n- Use [ ** ] for Power operation - [Value #1] raised by the power of [Value #2].'
          '\n- Use [ // ] for Root operation - [Value #1] rooted by the value of [Value #2].'
          '\n\nContinue your operation'
          '\nYour first value is ───→',  num1)


""" 
START OF PROGRAM EXECUTION 
"""

# Welcome user and introduce the 'help' operator.
print('\n         ╔═══════════════════════════════╗'
      '\n         ║ Welcome to Terminal Calculator║'
      '\n         ╚═══════════════════════════════╝'
      '\n\n► If you need help with available operators and their'
      '\n    uses, enter \'H\' when the operator is requested.'
      '\n\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')

# Execute 'calculate' LOOP.
calculate()