#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pkgutil import find_loader


class Foo(object):
    def __init__(self, input):
        self.input = input

    def handle_module(self, mod):
        l = find_loader(mod)
        n = getattr(l, 'fullname', getattr(l, 'name', None))
        return l.get_source(n)

    def __iter__(self):
        op, _, param = self.input.partition(':')
        func = getattr(self, 'handle_{}'.format(op.lower()))
        yield func(param)
