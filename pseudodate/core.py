#-*- coding:utf-8 -*-
"""
this module is pseudodate's core module
"""
from datetime import datetime as genuine_datetime
from datetime import *


class datetime(genuine_datetime):
    __pseudo_date = None
    __setup_date = None

    @classmethod
    def now(klass):
        now_date = genuine_datetime.now()

        if klass.__pseudo_date and klass.__setup_date:
            time_diff = now_date - __setup_date
            now_date = klass.__pseudo_date + time_diff
        return now_date

    @classmethod
    def truth_time(klass):
        return genuine_datetime.now()

    @classmethod
    def set_pseudo_date(klass, pseudo_date=None):
        if isinstance(pseudo_date, genuine_datetime) is False:
            raise TypeError("Need datetime object")
        klass.__pseudo_date = pseudo_date
        klass.__setupdate = genuine_datetime.now()

    @classmethod
    def clear_pseudo_date(klass):
        klass.__pseudo_date = None
        klass.__setup_date = None
