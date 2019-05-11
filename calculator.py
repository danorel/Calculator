def calculate(expr):
    sign, first, second = expr.split(",")
    result = 0
    if sign == "+":
        return int(first) + int(second)
    if sign == "-":
        return int(first) - int(second)
    if sign == "*":
        return int(first) * int(second)
    if sign == "/":
        if (second == 0):
            raise AttributeError("Division by zero exception")
        else:
            return float(first) / float(second)


with open("computing.txt") as file:
    for expr in file:
        result = calculate(expr)
        print("The result of operating expression {expression} is: {result}".format(expression=expr, result=result))
