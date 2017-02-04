import math


def is_operator(ch):
    return ch in PRIORITY_OPERATORS

OPENED_BRACKET = '('
CLOSED_BRACKET = ')'
EXPONENTIATION = '^'
MULTIPLICATION = '*'
DIVISION = '/'
MINUS = '-'
PLUS = '+'

COS = "cos"
SIN = "sin"
TAN = "tan"

# float("inf") will get infinity
PRIORITY_OPERATORS = {
    OPENED_BRACKET: float("inf"),
    CLOSED_BRACKET: float("inf"),
    COS: 4,
    EXPONENTIATION: 3,
    MULTIPLICATION: 2,
    DIVISION: 2,
    PLUS: 1,
    MINUS: 1,
}

MAP_OPERATORS = {
    EXPONENTIATION: lambda x, y: x ** y,
    MULTIPLICATION: lambda x, y: x * y,
    DIVISION: lambda x, y: x / y,
    PLUS: lambda x, y: x + y,
    MINUS: lambda x, y: x - y,
}

TRIGONOMETRICS = {
    COS: lambda x: math.cos(x),
    SIN: lambda x: math.sin(x),
    TAN: lambda x: math.tan(x),
}
