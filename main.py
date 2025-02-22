import operator

def main(input: str):
    try:
        a, op, b = input.split()

    except:
        output = "The expression is not valid. Try again or exit."

    else:
        if not (a.isdigit() and b.isdigit()):
            output = "Operands must be integer values. Try again or exit."
        elif not op in "+-*/":
            output = "Operator must be one of this: +, -, * or /. Try again or exit."
        else:
            a_int = int(a)
            b_int = int(b)
            if a_int < 0 or b_int < 0 or a_int > 10 or b_int > 10:
                output = "Operands must be integer values from 1 to 10. Try again or exit."
            else:
                operators = {
                    '+': operator.add,
                    '-': operator.sub,
                    '*': operator.mul,
                    '/': operator.floordiv
                }
                output = str(operators[op](a_int, b_int))
    return output




if __name__ == '__main__':
    greeting = """
Hey! This simple calculator can help you perform some basic arithmetic operations.
Type the expression of integer values from 1 to 10 in this format:
a + b
a - b
a * b
a / b
And then press Enter.
To exit type 'exit'.
    """
    print(greeting)

    user_input = ''
    while user_input != "exit":
        user_input = input("Your expression: ")
        print(main(user_input))
