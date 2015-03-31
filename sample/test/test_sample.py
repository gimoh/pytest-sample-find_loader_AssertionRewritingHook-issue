#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

import sample


class TestFoo(object):
    def test_sample(self):
        output = ''.join(list(sample.Foo('module:sample.test.sample_module')))
        assert output == 'FOO = 1\n'
