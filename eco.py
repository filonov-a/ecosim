#!env python
__author__ = 'aef'

from Eco.Factory import Factory

hello = "Hello World"

p = Factory("test factory", {"a": 1, "source2": 5}, {"Product": 2, "Thrash": 1})

p.Dump()
print hello
print  p.K
