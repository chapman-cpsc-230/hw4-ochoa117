"""
File: <Heaviside>
Copyright (c) 2016 <William Ochoa>
License: MIT
<This code tests the Heaviside function to see if it works.>
"""

def H(x):
    if x < 0:
        value = 0
    if x >= 0:
        value = 1
    return value

def test_H():
    if H(0) != 1:
        print "Error: "
    if H(-1) != 0:
        print "Error: "
    if H(1) != 1:
        print "Error: "

test_H()

print H(-10)
print H(-10**(-15))
print H(0)
print H(10**(-15))
print H(10)
