#!/usr/bin/env python
# coding: utf-8

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# show that duplicates have been removed
print(basket)
# fast membership testing
print('orange' in basket)

# Demonstraate set operations on unique letters from two words
a = set('abracaadabra')
b = set('alacazam')
# unique letters in a
print(a)
# letters in a but not in b
print(a - b)
# letters in a or b or both
print(a | b)
# letters in both a and b
print(a & b)
# letters in a or b but not both
print(a ^ b)
