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
