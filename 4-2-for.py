#!/usr/bin/env python
# coding: utf-8

# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# Loop over a slice copy of the entire list.
for w in words[:]:
    if 6 < len(w):
        words.insert(0, w)
print(words)
