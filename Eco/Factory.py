# coding=utf-8
__author__ = 'aef'

import pprint


class Factory:
    T = 1  # Длительность цикла производства
    N = 1  # Количество параллельных циклов.
    source = {}
    production = {}

    def __init__(self, n, src, prod):
        self.name = n
        self.source = src
        self.production = prod
        self.pp = pprint.PrettyPrinter(indent=2)
        return

    def __del__(self):
        return

    def MakeCycle(self):
        self.pp.pprint(self.source)
        return

    def Dump(self):
        print "Factory \"%s\" :" % self.name
        self.pp.pprint(self.K)
        self.pp.pprint(self.source)
        return

    def getName(self):
        return self.name
