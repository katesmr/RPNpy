import validator, RPN


if '__main__' == __name__:
    try:
        print(RPN.run(validator.split_expression(input())))
    except Exception as err:
        print("There was an error:", err)
