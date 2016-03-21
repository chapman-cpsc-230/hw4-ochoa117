"""
File: <smoothed_Heaviside>
Copyright (c) 2016 <William Ochoa>
License: MIT
<This code tests the validity of the Heaviside function.>
"""

from math import pi, sin

def H_eps(x, eps = 0.01):
    if x < -eps:
        value = 0
    elif x <= eps:
        value = 0.5*(1.0 + x/eps + sin((pi*x)/eps)/pi)
    else:
        value = 1
    return value

def test_H_eps():
    if H_eps(-1) != 0:
        print "Error: "
    eps = 0.01
    if H_eps(0) != 0.5*(1.0 + 0/eps + sin((pi*0)/eps)/pi):
        print "Error: "
    if H_eps(1) != 1:
        print "Error: "

test_H_eps()

print H_eps(-3)
print H_eps(-0.02)
print H_eps(-0.01)
print H_eps(0)
print H_eps(0.01)
print H_eps(0.02)
print H_eps(10)
