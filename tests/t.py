#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
from core import datetime
from datetime import datetime as genuine_datetime


class PseudoDateTest(unittest.TestCase):
    def setUp(self):
        datetime.set_pseudo_date(
            genuine_datetime(2000, 1, 1, 0, 0, 0)
            )

    def tearDown(self):
        datetime.clear_pseudo_date()

    def test_pesudo_date(self):
        properties = ('year', 'month', 'day', 'hour', 'minute',)
        values = (2000, 1, 1, 0, 0, 0,)
        pseudo_date = datetime.now()

        for p, v in zip(properties, values):
            assert getattr(pseudo_date, p) == v, '%s is different' % (p)


class PseudoDateSuite(unittest.TestSuite):
    def __init__(self):
        tests = ('test_pesudo_date',)
        unittest.TestSuite.__init__(
            self,
            map(PseudoDateTest, tests)
            )

if __name__ == "__main__":
    alltests = PseudoDateSuite()
    unittest.TextTestRunner(verbosity=2).run(alltests)
