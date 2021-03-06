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
    """Checks if given infix expression is syntactically correct."""
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
    """Converts infix expression into postfix expression of identical meaning."""
    stack = []  # keep operators here
    postfix = ''
    precedence = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}

    for c in infix:
        # numbers can be added to postfix expression immediately otherwise one needs to differentiate
        if c not in ['+', '-', '/', '*', '(', ')']:
            postfix += c
        else:
            # parentheses stay at their position only chars inside need to change order
            if c == '(':
                stack.append(c)
            # pop stack until corresponding open parentheses is found
            elif c == ')':
                operator = stack.pop()
                while not operator == '(':
                    postfix += operator
                    operator = stack.pop()
            # push operator on stack unless operators with higher precedence are already on stack, these can be added
            # to expression because higher ranked operators will always be left and the most left operator is the first
            # to take effect
            else:
                while len(stack) > 0 and precedence[stack[-1]] >= precedence[c]:
                    postfix += stack.pop()
                stack.append(c)

    # at the end add already sorted operators to expression
    while len(stack) > 0:
        postfix += stack.pop()
    return postfix


def parse(s):
    """Parses given infix expression into binary tree/syntax tree and returns root."""
    stack = []
    if not check_infix(s):
        raise SyntaxError('infix expression is incorrect!')
    postfix = convert_to_postfix(s)

    # given a postfix expression you can create the corresponding syntax tree easily using a stack
    # iterating through the postfix expression numbers can be pushed instantly
    for c in postfix:
        if c not in ['+', '-', '/', '*']:
            stack.append(Number(c, None, None))
        # operators need to be applied to last two numbers of expression/stack, that means
        # only operators are inner children which need to have operands as children/leaves
        # the resulting subtree can again be a children for a new operator node, which is why it
        # needs to be pushed to the stack
        else:
            right = stack.pop()
            left = stack.pop()
            stack.append(Operator(c, left, right))
        # at the end only one node should be left - the root node
    return stack.pop()


def operation(op1, operator, op2):
    """Calculates simple arithmetic expression given operator as a string."""
    if operator == '+':
        return op1 + op2
    if operator == '-':
        return op1 - op2
    if operator == '*':
        return op1 * op2
    if operator == '/':
        return op1 / op2


def evaluate(root):
    """Evaluates syntax tree using recursion."""
    # if node is number return it
    if isinstance(root, Number):
        return root.number
    # otherwise gain corresponding number to left and right subtree (recursion)
    operand_l = evaluate(root.left)
    operand_r = evaluate(root.right)
    # and use operation corresponding to current operator node
    return operation(operand_l, root.operator, operand_r)


class TestCalculator(unittest.TestCase):
    """Testclass to test calculator on simple arithmetic expressions and cases with different operator precedences."""
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
