#!/usr/bin/env python
# coding: utf-8

import math

# prints '00012'
print('12'.zfill(5))
# prints '-003.14'
print('-3.14'.zfill(7))

print('We are the {} who say "{}!'.format('knights', 'Ni'))
print('{0} and {1}'.format('spam', 'eggs'))
print('This {food} is {adjective}.'.format(
    food='spam', adjective='absolutely horrible'))
print('The story of {0}, {1}, and {other}.'.format(
    'Bill', 'Manfred', other='Georg'))
# prints "My hovercraft is full of 'eels'"
print('My hovercraft is full of {!r}'.format('eels'))
# prints 'The value of PI is approximately 3.142.
print('The value of PI is approximately {0:.3f}.'.format(math.pi))
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(
    **{
        'Sjoerd': 4127,
        'Jack': 4098,
        'Dcab': 8637678
    }))
