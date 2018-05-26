#!/usr/bin/env python
# coding: utf-8

squares = [1, 4, 9, 16, 25]
# returns a new (shallow) copy of the list
print(squares[:])

cubes = [1, 8, 27, 64, 125]
print(cubes)
# add the cube of 7
cubes.append(7**3)
print(cubes)

letters = ['a', 'b', 'c' 'd' 'e' 'f' 'g']
# replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)
# now remove them
letters[2:5] = []
print(letters)
# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)
