from helper import is_operator, OPENED_BRACKET, CLOSED_BRACKET, TRIGONOMETRICS


def is_stop_parsing_operand(ch):
    return ch.isspace() or is_operator(ch)


def is_opened_bracket(ch):
    return OPENED_BRACKET == ch


def is_closed_bracket(ch):
    return CLOSED_BRACKET == ch


def split_expression(string):

    def _process_operand(index):
        supposed_operand = string[index]  # assume that the first char is always exists
        index += 1
        while index < length and not is_stop_parsing_operand(string[index]):
            supposed_operand += string[index]
            index += 1
        try:
            if supposed_operand in TRIGONOMETRICS:
                brackets_counter = 1
                index += 1
                begin = index
                while index < length and brackets_counter != 0:
                    if OPENED_BRACKET == string[index]:
                        brackets_counter += 1
                    elif CLOSED_BRACKET == string[index]:
                        brackets_counter -= 1
                    index += 1
                expression.append([supposed_operand, split_expression(string[begin:index-1])])
            else:
                expression.append(float(supposed_operand))
        except ValueError:
            raise Exception("'{}' is not operand".format(supposed_operand))
        return index

    def _process_operator(index):
        supposed_operator = string[index]  # assume that length of operator should be equal to one
        if is_operator(supposed_operator):
            expression.append(supposed_operator)
        else:
            raise Exception("'{}' is not operator".format(supposed_operator))
        return index + 1

    def _skip_spaces(index):
        while index < length and string[index].isspace():
            index += 1
        return index

    length = len(string)
    is_operand_flag = True
    expression = []
    i = 0

    while True:
        i = _skip_spaces(i)
        if i >= length:
            break
        if is_opened_bracket(string[i]):
            is_operand_flag = False
        elif is_closed_bracket(string[i]):
            is_operand_flag = False
            i = _process_operator(i)
            continue
        if is_operand_flag:
            i = _process_operand(i)
        else:
            i = _process_operator(i)
        is_operand_flag = not is_operand_flag

    return expression
