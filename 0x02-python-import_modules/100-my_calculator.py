#!/bin/python3
import sys
from calculator_1 import add, sub, mul, div
size = len(sys.argv)

if size != 4:
    print('Usage: {} <a> <operator> <b>'.format(argv[0]))
    sys.exit(1)

    opp = {"+":add, "-":sub, "*":mul, "/":div}
    if argv[2] in ops:
        num1 = int(argv[1])
        num2 = int(argv[3])
        opp = ops[argv[2]]
        result = opp(num1, num2)
        print('{:d} {:s} {:d} = {:d}'.format(num1, argv[2], num2, result))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    exit(0)
