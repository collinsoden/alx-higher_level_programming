#!/usr/bin/python3

if __name__ == "__main__":
    #Import all functions from calculator
    import calculator_1 as calc
    a = 10
    b = 5
    print("{} + {} = {}\n".format((a, b, calc.add(a, b))))
    print("{} - {} = {}\n".format((a, b, calc.sub(a, b))))
    print("{} * {} = {}\n".format((a, b, calc.mul(a, b))))
    print("{} / {} = {}\n".format((a, b, calc.div(a, b))))
