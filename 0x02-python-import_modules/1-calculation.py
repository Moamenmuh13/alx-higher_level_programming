#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5

resultOfAdd = add(a, b)
resultOfsub = sub(a, b)
resultOfmul = mul(a, b)
resultOfdiv = div(a, b)

print("{} + {} = {}".format(a, b, resultOfAdd))
print("{} - {} = {}".format(a, b, resultOfsub))
print("{} * {} = {}".format(a, b, resultOfmul))
print("{} / {} = {}".format(a, b, resultOfdiv))
