def is_operator(ch):
    return ch in PRIORITY_OPERATORS


OPENED_BRACKET = '('
CLOSED_BRACKET = ')'

# float("inf") will get infinity
PRIORITY_OPERATORS = {
    OPENED_BRACKET: float("inf"),
    CLOSED_BRACKET: float("inf"),
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
}

MAP_OPERATORS = {
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
}
