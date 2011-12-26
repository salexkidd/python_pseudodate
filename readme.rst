======================================================================
python-pseudodate by salexkidd (http://twitter.com/salexkidd)
======================================================================

.. toctree::

About
____________________________________
python-pseudodate provide a pseudo date.
If may be useful if the system time to debug.

Example
____________________________________
If you want to get the datetime.now() to date in the future, try this.

>>> from pseudodate import datetime
>>> datetime.now()
datetime.datetime(2011, 12, 26, 22, 39, 42, 892208) #got now datetime object
>>> future_date = datetime(2000, 1, 1)
>>> datetime.set_pseudo_date(future_date)
>>> datetime.now()
datetime.datetime(3000, 1, 1, 0, 0, 00, 357854)
>>> import time
>>> time.sleep(5)
datetime.datetime(3000, 1, 1, 0, 5, 00, 391603)
