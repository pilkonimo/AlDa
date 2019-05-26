class Number:
    def __init__(self, val, l, r):
        self.number = int(val)
        self.left = l
        self.right = r


class Operator:
    def __init__(self, op, l, r):
        self.operator = op
        self.left = l
        self.right = r


def check_infix(infix):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    operators = ['+', '-', ':', '*']
    paranth_counter = 0
    # first element needs to be a number
    if not infix[0] in numbers:
        return False
    for i in range(1, len(infix) - 1):
        if infix[i] in numbers and (infix[i+1] not in operators and infix[i+1] != ')'):
            return False
        if infix[i] in operators and (infix[i+1] not in numbers and infix[i+1] != '('):
            return False
        if infix[i] == '(':
            paranth_counter += 1
        if infix[i] == ')':
            paranth_counter -= 1
            if paranth_counter < 0:
                return False
    # last element needs to be number and number of open and closed parentheses needs to be equal
    if infix[len(infix)-1] not in numbers or paranth_counter != 0:
        return False
    return True

def convert_to_postfix(infix):
    stack = []
    postfix = ''
    precedence = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}

    for c in infix:
        if c not in ['+', '-', ':', '*', '(', ')']:
            postfix += c
        else:
            if c == '(':
                stack.append(c)
            elif c == ')':
                operator = stack.pop()
                while not operator == '(':
                    postfix += operator
                    operator = stack.pop()
            else:
                while len(stack) > 0 and precedence[stack[-1]] >= precedence[c]:
                    postfix += stack.pop()
                stack.append(c)

    while len(stack) > 0:
        postfix += stack.pop()
    return postfix


def parse(s):
    stack = []
    if not check_infix(s):
        raise SyntaxError('infix expression is incorrect!')
    postfix = convert_to_postfix(s)

    for c in postfix:
        if c not in ['+', '-', ':', '*']:
            stack.append(Number(c, None, None))
        else:
            right = stack.pop()
            left = stack.pop()
            stack.append(Operator(c, left, right))
    return stack.pop()


def operation(op1, operator, op2):
    if operator == '+':
        return op1 + op2
    if operator == '-':
        return op1 - op2
    if operator == '*':
        return op1 * op2
    if operator == '/':
        return op1 / op2


def evaluate(root):
    if isinstance(root, Number):
        return root.number
    operand_l = evaluate(root.left)
    operand_r = evaluate(root.right)
    return operation(operand_l, root.operator, operand_r)

