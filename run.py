from decimal import Decimal

# Defining global variables.
num1 = 0
num2 = 0
result = 'N/A'
num_format = ''
valid = True
memory = []

# Define an 'operators' list (if modified, the 'user_help()' function needs to be updated).
operators = ['+', '-', '*', '/', '%', 'A', '**', '//']

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
    Define a class to store operations performaed for memory function
    """
    def __init__(self, value1, operator, value2, answer):
        self.value1 = value1
        self.operator = operator
        self.value2 = value2
        self.answer = answer


def past_results():
    global memory, num1
    print('\nPrevious operations:'
          '\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    if len(memory) == 0:
        print('None')

    while len(memory) > 10:
        memory.pop(0)

    for mem in memory:
        print('>', mem.value1, mem.operator, mem.value2, '=', mem.answer)
    print('\nContinue your operation'
          '\nYour first value is ───→', num1)