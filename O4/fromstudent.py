class Stack:
    def __init__(self):
        self.__elements = []


    def isEmpty(self):
        return len(self.__elements) == 0

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.__elements[len(self.__elements) - 1]


    def push(self, value):
        self.__elements.append(value)


    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.__elements.pop()

    def getSize(self):
        return len(self.__elements)


def main():
    expression = input("Enter an expression: ").strip()
    try:
        print(expression, "=", evaluateExpression(expression))
    except:
        print("Wrong expression: ", expression)


def insertBlanks(exp):
    res = ""
    for i in exp:
        if i in [')', '(', '+', '-', '*', '%', '^']:
            res += " " + i + " "
        else:
            res += i
    return res


def preceedence(c):
    if c == '^':
        return 1
    if c in ['/', '*', '%']:
        return 2
    if c in ['+', '-']:
        return 3

def evaluateExpression(expression):
    operandStack = Stack()
    operatorStack = Stack()
    expression = insertBlanks(expression)
    expression = expression.split()
    res = []

    for i in expression:

        if i not in [')', '(', '+', '-', '*', '%', '^']:
            res.append(i)

        elif i == '(':
            operatorStack.push(i)

        elif i == ')':
            while ((not operatorStack.isEmpty()) and operatorStack.peek() != '('):
                d = operatorStack.pop()
                res.append(d)

            if (not operatorStack.isEmpty() and operatorStack.peek() != '('):
                return None
            else:
                operatorStack.pop()
        else:
            while ((not operatorStack.isEmpty()) and operatorStack.peek() != '(' and (
                    preceedence(operatorStack.peek()) <= preceedence(i))):
                res.append(operatorStack.pop())
            operatorStack.push(i)

    while not operatorStack.isEmpty():
        res.append(operatorStack.pop())

    expression = res

    for i in expression:
        if i not in ['+', '-', '*', '%', '^']:
            operandStack.push(float(i))
        else:
            d = operandStack.pop()
            e = operandStack.pop()

            if i == '+':
                operandStack.push(d + e)
            elif i == '-':
                operandStack.push(d - e)
            elif i == '*':
                operandStack.push(d * e)
            elif i == '/':
                operandStack.push(d / e)
            elif i == '%':
                operandStack.push(d % e)
            elif i == '^':
                operandStack.push(d ** e)

    return operandStack.pop()


main()