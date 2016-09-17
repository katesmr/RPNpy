from helper import PRIORITY_OPERATORS, is_operator, OPENED_BRACKET, CLOSED_BRACKET, MAP_OPERATORS


def infix_to_postfix(expression):

    def _bracket_counter_comparison():
        if opened_brackets_counter != closed_brackets_counter:
            raise Exception("Count of opened brackets not equal count of closed brackets!")

    stack_operators = []
    stack = []
    opened_brackets_counter = 0
    closed_brackets_counter = 0

    for token in expression:
        if is_operator(token):
            if CLOSED_BRACKET == token:
                tmp = stack_operators.pop()
                closed_brackets_counter += 1
                while OPENED_BRACKET != tmp:
                    stack.append(tmp)
                    tmp = stack_operators.pop()
            elif OPENED_BRACKET == token:
                stack_operators.append(token)
                opened_brackets_counter += 1
            else:
                if len(stack_operators):
                    if PRIORITY_OPERATORS[token] <= PRIORITY_OPERATORS[stack_operators[-1]]:
                        if OPENED_BRACKET != stack_operators[-1]:
                            stack.append(stack_operators.pop())
                stack_operators.append(token)
        else:
            if not str(token).isspace():
                stack.append(token)

    while len(stack_operators) > 0:  # in func ??
        stack.append(stack_operators.pop())

    _bracket_counter_comparison()

    return stack


def run(postfix_expression):
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
    return postfix_expression


r = infix_to_postfix([7, '*', 3, '+', '(', 4, '-', 2, '*', 5, ')'])
e = infix_to_postfix(['(', 8, '+', 2, '*', 5, ')', '/', '(', 1, '+', 3, '*', 2, '-', 4, ')'])
print(run(r))
print(run(e))
