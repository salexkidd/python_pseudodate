#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pseudodate import datetime
import time

n = datetime.now()
p = datetime(2011, 1, 1)

datetime.set_pseudo_date(p)
print datetime.now()
time.sleep(3)
print datetime.now()
