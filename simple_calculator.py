#!/usr/bin/python3

num1, operator, num2 = eval(input('Enter Calculation')).split()
num1 = int(num1)
        if operator == "-":
        print("{} + {} = {}".format(num1, operator, num2))
        elif operator == "+":
        print("{} + {} = {}".format(num1, operator, num2))
        elif operator == "*":
        print("{} + {} = {}".format(num1, operator, num2))
        elif operator == "/":
        print("{} + {} = {}".format(num1, operator, num2))
        elif operator == "%":
        print("{} + {} = {}".format(num1, operator, num2))
        elif operator == "**":
        print("{} + {} = {}".format(num1, operator, num2))
        else
        print("Use either - + * / % or ** next time")
