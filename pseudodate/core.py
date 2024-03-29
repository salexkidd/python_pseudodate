# -*- coding:utf-8 -*-
"""
This is core module of pseudodate.
"""
from datetime import datetime as genuine_datetime


class datetime(genuine_datetime):
    """
    now function return pseudo datetime object or truth_now

    >>> from datetime import datetime as genuine_datetime
    >>> past_date = genuine_datetime(2000, 1, 1)
    >>> datetime.set_pseudo_date(past_date)
    >>> pseudo_date = datetime.now()
    >>> pseudo_date.year
    2000
    >>> pseudo_date.month
    1
    >>> pseudo_date.day
    1
    >>> pseudo_date.hour
    0
    >>> pseudo_date.minute
    0
    """

    __pseudo_date = None
    __setup_date = None

    @staticmethod
    def now():
        """
        This function provide specific pseude date or genuine datetime
        """
        now_date = datetime.truth_now()
        _pesudo_date = datetime.__pseudo_date
        _setup_date = datetime.__setup_date

        if isinstance(_pesudo_date, genuine_datetime) and \
                isinstance(_setup_date, genuine_datetime):

            time_diff = now_date - datetime.__setup_date
            sum_date = datetime.__pseudo_date + time_diff
            now_date = datetime(
                sum_date.year,
                sum_date.month,
                sum_date.day,
                sum_date.hour,
                sum_date.minute,
                sum_date.second,
                )
        return now_date

    @staticmethod
    def truth_now():
        """
        This function provide genuine datetime.
        """
        return genuine_datetime.now()

    @classmethod
    def set_pseudo_date(klass, pseudo_date=None):
        """
        This function set spcific pseudo datetime.
        """
        if isinstance(pseudo_date, genuine_datetime) is False:
            raise TypeError("set_pseudo_date function need a datetime object")
        klass.__pseudo_date = pseudo_date
        klass.__setup_date = klass.truth_now()

    @classmethod
    def clear_pseudo_date(klass):
        """
        This function clear pseudo datetime and setup time.
        """
        klass.__pseudo_date = None
        klass.__setup_date = None


def _doctest():
    """
    Call doctest
    """
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    _doctest()
