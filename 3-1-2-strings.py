#!/usr/bin/env python
# coding: utf-8

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# 3 times 'un', followed by 'ium'
print(3 * 'un' + 'ium')
print('Py' 'thon')
prefix = 'Py'

# can't concatenate a variable and a string literal
# print(prefix 'thon')
word = 'Python'
# character in position 0
print(word[0])
# last character
print(word[-1])
# characters from position 0 (included) to 2 (excluded)
print(word[0:2])
# characters from the beginning to position 2 (excluded)
print(word[:2])
# characters from position 4 (included) to the end
print(word[4:])
# characters from the second-last (included) to the end
print(word[-2:])

s = 'supercalifragilisticexpialidocious'
print(len(s))
