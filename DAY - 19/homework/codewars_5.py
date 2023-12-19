def basic_op(operator, value1, value2):
    res = 0
    for i in operator:
        if i == "*":
            res = value1 * value2
        elif i == "+":
            res = value1 + value2
        elif i == "-":
            res = value1 - value2
        else:
            res = value1 / value2
    return res
            