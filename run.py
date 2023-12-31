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
    formatting numbers so that floating points are displayed as integers
    """
    global num_format
    try:
        x = '{:,}'.format(x)
        if x.endswith('.0'):
            num_format = x[:-2]
    except ValueError:
        pass
    return num_format
