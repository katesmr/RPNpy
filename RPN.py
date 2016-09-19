from helper import PRIORITY_OPERATORS, is_operator, OPENED_BRACKET, CLOSED_BRACKET, MAP_OPERATORS, TRIGONOMETRICS


def _infix_to_postfix(expression):

    stack_operators = []
    stack = []

    for token in expression:
        if type(token) is list:  # sub expression
            func = token[0]
            sub_expression = token[1]
            stack.append(TRIGONOMETRICS[func](run(sub_expression)))
        elif is_operator(token):
            if CLOSED_BRACKET == token:
                tmp = stack_operators.pop()
                while OPENED_BRACKET != tmp:
                    stack.append(tmp)
                    tmp = stack_operators.pop()
            elif OPENED_BRACKET == token:
                stack_operators.append(token)
            else:
                if len(stack_operators):
                    if PRIORITY_OPERATORS[token] <= PRIORITY_OPERATORS[stack_operators[-1]]:
                        if OPENED_BRACKET != stack_operators[-1]:
                            stack.append(stack_operators.pop())
                stack_operators.append(token)
        else:
            stack.append(token)

    while len(stack_operators) > 0:
        stack.append(stack_operators.pop())

    return stack


def _rpn(postfix_expression):
    length = len(postfix_expression)
    i = 0

    while i < length:
        token = postfix_expression[i]

        if token in MAP_OPERATORS:
            index_right_operand = i - 2
            index_left_operand = i - 1
            res = MAP_OPERATORS[token](postfix_expression[index_right_operand], postfix_expression[index_left_operand])
            postfix_expression.insert(i + 1, res)
            postfix_expression = postfix_expression[:index_right_operand] + postfix_expression[i + 1:]
            length = len(postfix_expression)
            j = postfix_expression.index(res)
            i = j + 1
            if j > length:
                break
            continue
        i += 1
    return postfix_expression[0]


def run(expression):
    assert len(expression) > 0, "There no expression!"
    return _rpn(_infix_to_postfix(expression))

