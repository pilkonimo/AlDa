import unittest
import random


class Number:
    def __init__(self, val, l, r):
        self.number = float(val)
        self.left = l
        self.right = r


class Operator:
    def __init__(self, op, l, r):
        self.operator = op
        self.left = l
        self.right = r


def check_infix(infix):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    operators = ['+', '-', '/', '*']
    parenth_counter = 0
    # first element needs to be a number
    if not infix[0] in numbers:
        return False
    # s i)
    if len(infix) > 1:
        if infix[1] in numbers and (infix[1] not in operators and infix[1] != ')'):
            return False
    for i in range(1, len(infix) - 1):
        # i) number needs to be followed by closed parentheses or operator
        if infix[i] in numbers and (infix[i+1] not in operators and infix[i+1] != ')'):
            return False
        # ii) operator needs to be followed by number or open parentheses
        if infix[i] in operators and (infix[i+1] not in numbers and infix[i+1] != '('):
            return False
        # iii) at every point of expression number of closed should never exceed number of open parentheses
        if infix[i] == '(':
            parenth_counter += 1
        if infix[i] == ')':
            parenth_counter -= 1
            if parenth_counter < 0:
                return False
    # last element needs to be number and number of open and closed parentheses needs to be equal
    if infix[len(infix)-1] == ')':
        if parenth_counter > 1:
            return False
        return True
    if infix[len(infix)-1] not in numbers or parenth_counter != 0:
        return False
    return True


def convert_to_postfix(infix):
    stack = []
    postfix = ''
    precedence = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}

    for c in infix:
        if c not in ['+', '-', '/', '*', '(', ')']:
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
        if c not in ['+', '-', '/', '*']:
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


class TestCalculator(unittest.TestCase):
    def test_addition(self):
        operand1 = random.randint(0, 9)
        operand2 = random.randint(0, 9)
        infix = str(operand1) + '+' + str(operand2)
        self.assertEqual(operand1 + operand2, evaluate(parse(infix)))

    def test_subtraction(self):
        operand1 = random.randint(0, 9)
        operand2 = random.randint(0, 9)
        infix = str(operand1) + '-' + str(operand2)
        self.assertEqual(operand1 - operand2, evaluate(parse(infix)))

    def test_multiplication(self):
        operand1 = random.randint(0, 9)
        operand2 = random.randint(0, 9)
        infix = str(operand1) + '*' + str(operand2)
        self.assertEqual(operand1 * operand2, evaluate(parse(infix)))

    def test_division(self):
        operand1 = random.randint(0, 9)
        operand2 = random.randint(1, 9)
        infix = str(operand1) + '/' + str(operand2)
        self.assertEqual(operand1 / operand2, evaluate(parse(infix)))

    def test_operator_precedence(self):
        operand1 = random.randint(0, 9)
        operand2 = random.randint(0, 9)
        operand3 = random.randint(0, 9)
        infix = str(operand1) + '+' + str(operand2) + '*' + str(operand3)
        self.assertEqual(operand1 + operand2 * operand3, evaluate(parse(infix)))
        infix = str(operand1) + '+' + str(operand2) + '/' + str(operand3)
        self.assertEqual(operand1 + operand2 / operand3, evaluate(parse(infix)))
        infix = str(operand1) + '-' + str(operand2) + '*' + str(operand3)
        self.assertEqual(operand1 - operand2 * operand3, evaluate(parse(infix)))
        infix = str(operand1) + '-' + str(operand2) + '/' + str(operand3)
        self.assertEqual(operand1 - operand2 / operand3, evaluate(parse(infix)))

    def test_parentheses(self):
        operand1 = random.randint(0, 9)
        operand2 = random.randint(0, 9)
        operand3 = random.randint(0, 9)
        infix = str(operand1) + '+(' + str(operand2) + '-' + str(operand3) + ')'
        self.assertEqual(operand1 + (operand2 - operand3), evaluate(parse(infix)))
        infix = str(operand1) + '*(' + str(operand2) + '-' + str(operand3) + ')'
        self.assertEqual(operand1 * (operand2 - operand3), evaluate(parse(infix)))
        infix = str(operand1) + '*(' + str(operand2) + '/' + str(operand3) + ')'
        self.assertEqual(operand1 * (operand2 / operand3), evaluate(parse(infix)))

    def test_syntax_check(self):
        with self.assertRaises(SyntaxError):
            parse('4+-3')
        with self.assertRaises(SyntaxError):
            parse('44-3')
        with self.assertRaises(SyntaxError):
            parse('4-3)+4')


if __name__ == '__main__':
    unittest.main()
