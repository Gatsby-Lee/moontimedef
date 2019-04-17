moontimedef
===========

This `moontimedef` is a module having Time Defintions.


How to install
--------------

.. code-block:: bash

    pip install moontimedef


How to use
----------

.. code-block:: python

    # get all TimeType
    >>> from mtimedef import TimeType
    >>> TimeType.get_list()
    [<TimeType.not_defined: -1>, <TimeType.hour: 10>, <TimeType.day: 20>, <TimeType.week: 30>, <TimeType.biweek: 40>, <TimeType.month: 50>, <TimeType.quarter: 60>, <TimeType.semiyear: 70>, <TimeType.year: 80>]

    # create a TimeType object with value
    >>> t1 = TimeType(10)
    >>> t1
    <TimeType.hour: 10>
    # comparing TimeType object
    >>> t1 == 10
    False
    >>> t1 == TimeType.hour
    True

    # get short(lower case) name
    >>> t1.get_shortlower_name()
    'hh'
    # get upper case name
    >>> t1.get_uppercase_name()
    'HOUR'


Why built this?
---------------

I spend lots of time to crawl data from WEB or API.

One of the common modules I've used is Time Definitions like Week, Month, Year, or etc.


Design Decisions
----------------

Simple and Reusable


Simple: Keep cores only related to Time Definitions.

Reusable: Keep low level so it can be used as libary.
