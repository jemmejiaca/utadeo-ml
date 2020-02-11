# -*- coding: utf-8 -*-
"""
Universidad Jorge Tadeo Lozano
MIAD - Machine Learning
Python Workshop No. 1
Author: J. Mauricio Mejía Castro
"""
import sys
import sklearn as skl
import scipy as sp
import numpy as np
import matplotlib as plt
import pandas as pd

import random as rnd
import math

print("Python: {}".format(sys.version))
print("Sklearn: {}".format(skl.__version__))
print("Numpy: {}".format(np.__version__))
print("Scipy: {}".format(sp.__version__))
print("Matplotlib: {}".format(plt.__version__))
print("Pandas: {}".format(pd.__version__))

#print(help(rnd))

""" --- Basic Python --- """

# 1. Numbers
print(3 / 2)
print(3 / float(2))
print(3 % 2)
print(3.0 // 2.0)
print(2 ** 3)
print(4 ** 0.5)
print(math.sqrt(4))
print(2 + 10 * 10 + 3)
print( (2 + 10) * (10 + 3))

# 2. Variables
a = 10
print("a = %s" % (a))
a = a + 10
print("a = %s" % (a))
a += 10
print("a = %s" % (a))
b = c = a
print("a = %s, b = %s, c = %s" % (a, b, c))
a, b, c = 1, 2, "jhon"
print("a = %s, b = %s, c = %s" % (a, b, c))
my_dogs = 2
print(my_dogs)
my_dogs = ['Sammy','Frankie']
print(my_dogs)
del my_dogs

# 3. Strings
my_str = 'Hello World!'
print(my_str[0])
print(my_str[2:5])
print(my_str[2:5])
print(my_str[2:])
print(my_str * 2)
print(my_str + 'TEST')
print(my_str.split())
print(my_str.upper())
print('Carlos: {}'.format(my_str))
print( "%s, %s" % (my_str, "I'm Carlos!"))
print('I wrote %s programs today.' %3.75)
print('I wrote %d programs today.' %3.75)
print('I wrote %5.2f programs today.' %3.75)
print('First: %s, Second: %5.2f, Third: %r' %('hi!', 3.1415, 'bye!'))
print('First: {2}, Second: {1}, Third: {0}'.format('fox','brown','quick'))
print('First Object: {a}, Second Object: {b}, Third Object: {c}'.format(a = 1,
    b = 'Two', c = 12.3))
print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:8}'.format('Apples', 3.))
print('{0:8} | {1:8}'.format('Oranges', 10))
 
# 4. Array list
my_list





