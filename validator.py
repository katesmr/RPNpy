from helper import is_operator


def is_stop_parsing_operand(ch):
    return ch.isspace() or is_operator(ch)


def split_expression(string):

    def _process_operand(index):
        supposed_operand = string[index]  # assume that the first char is always exists
        index += 1
        while index < length and not is_stop_parsing_operand(string[index]):
            supposed_operand += string[index]
            index += 1
        try:
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
    is_operand = True
    expression = []
    i = 0

    while True:
        i = _skip_spaces(i)
        if i >= length:
            break
        if is_operand:
            i = _process_operand(i)
        else:
            i = _process_operator(i)
        is_operand = not is_operand

    return expression
